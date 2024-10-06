import cv2
import os
import warnings
import sys
import requests
import stat
import tarfile
import subprocess
import shutil
import platform
import psutil
import webbrowser

homedir = os.path.expanduser("~")


def getPlatform() -> str:
    """
    Returns the current OS that the app is running on
    Windows: win32
    MacOS: darwin
    Linux: linux
    """
    return sys.platform


def isFlatpak():
    return "FLATPAK_ID" in os.environ


if isFlatpak():
    cwd = os.path.join(
        os.path.expanduser("~"), ".var", "app", "io.github.tntwise.REAL-Video-Enhancer"
    )
    if not os.path.exists(cwd):
        cwd = os.path.join(
            os.path.expanduser("~"),
            ".var",
            "app",
            "io.github.tntwise.REAL-Video-EnhancerV2",
        )
else:
    cwd = os.getcwd()


def getAvailableDiskSpace() -> float:
    """
    Returns the available disk space in GB.
    """
    total, used, free = shutil.disk_usage("/")
    available_space = free / (1024**3)
    return available_space


with open(os.path.join(cwd, "frontend_log.txt"), "w") as f:
    pass

def extractTarGZ(file):
    """
    Extracts a tar gz in the same directory as the tar file and deleted it after extraction.
    """
    origCWD = os.getcwd()
    dir_path = os.path.dirname(os.path.realpath(file))
    os.chdir(dir_path)
    printAndLog("Extracting: " + file)
    tar = tarfile.open(file, "r:gz")
    tar.extractall()
    tar.close()
    removeFile(file)
    os.chdir(origCWD)

def backendDirectory():
    """
    returns cwd except when running in flatpak, then it returns the flatpak bin directory
    """

    if isFlatpak():
        return "/app/bin/backend"
    else:
        return os.path.join(cwd, "backend")


def downloadFile(link, downloadLocation):
    response = requests.get(
        link,
        stream=True,
    )
    printAndLog("Downloading: " + link)
    with open(downloadLocation, "wb") as f:
        chunk_size = 1024
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)


def downloadTempDirectory() -> str:
    tmppath = os.path.join(cwd, "temp")
    createDirectory(tmppath)
    return tmppath


def networkCheck(hostname="https://raw.githubusercontent.com") -> bool:
    """
    checks network availability against a url, default url: raw.githubusercontent.com
    """
    try:
        _ = requests.head(hostname, timeout=1)
        return True
    except requests.ConnectionError as e:
        print(str(e))
        print("No internet connection available.")
    return False


def getRAMAmount() -> str:
    """
    Returns the amount of RAM in the system.
    """
    ram = psutil.virtual_memory().total
    ram_gb = ram / (1024**3)
    return f"{ram_gb:.2f} GB"


def pythonPath() -> str:
    return (
        os.path.join(cwd, "python", "python", "python.exe")
        if getPlatform() == "win32"
        else os.path.join(cwd, "python", "python", "bin", "python3")
    )


def modelsPath() -> str:
    """
    Returns the file path for the models directory.

    :return: The file path for the models directory.
    :rtype: str
    """
    return os.path.join(cwd, "models")


def videosPath() -> str:
    """
    Returns the file path for the videos directory.

    :return: The file path for the videos directory.
    :rtype: str
    """
    if getPlatform() == "darwin":
        return os.path.join(homedir, "Desktop")
    else:
        return os.path.join(homedir, "Videos")


def copy(prev: str, new: str):
    """
    moves a folder from prev to new
    """
    if not os.path.exists(new):
        if not os.path.isfile(new):
            shutil.copytree(prev, new)
        else:
            print("WARN tried to rename a file to a file that already exists")
    else:
        print("WARN tried to rename a folder to a folder that already exists")


def move(prev: str, new: str):
    """
    moves a file from prev to new
    """
    if not os.path.exists(new):
        if not os.path.isfile(new):
            os.rename(prev, new)
        else:
            print("WARN tried to rename a file to a file that already exists")
    else:
        print("WARN tried to rename a folder to a folder that already exists")


def makeExecutable(file_path):
    st = os.stat(file_path)
    os.chmod(file_path, st.st_mode | stat.S_IEXEC)


def warnAndLog(message: str):
    warnings.warn(message)
    log("WARN: " + message)


def createDirectory(dir: str):
    if not os.path.exists(dir):
        os.mkdir(dir)


def printAndLog(message: str, separate=False):
    """
    Prints and logs a message to the log file
    separate, if True, activates the divider
    """
    if separate:
        message = message + "\n" + "---------------------"
    print(message)
    log(message=message)


def log(message: str):
    with open(os.path.join(cwd, "frontend_log.txt"), "a") as f:
        f.write(message + "\n")


def currentDirectory():
    return cwd


def removeFile(file):
    try:
        os.remove(file)
    except:
        print("Failed to remove file!")


def checkIfDeps() -> bool:
    """
    Checks if python or ffmpeg is installed, and if not returns false.
    """
    if not os.path.isfile(pythonPath()):
        return False
    return True


def downloadFile(link, downloadLocation):
    response = requests.get(
        link,
        stream=True,
    )

    with open(downloadLocation, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)


def checkValidVideo(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Couldn't open the video file '{video_path}'")
        return False

    ret, frame = cap.read()
    if not ret:
        print(f"Error: Couldn't read frames from the video file '{video_path}'")
        return False

    cap.release()

    return True


def getVideoRes(video_path) -> list[int, int]:
    """
    Takes in a video path
    Uses opencv to detect the resolution of the video
    returns [width,height]
    """
    cap = cv2.VideoCapture(video_path)

    # Get the resolution
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    resolution = [width, height]

    cap.release()

    return resolution


def get_gpu_info():
    system = getPlatform()

    if system == "win32":
        try:
            output = subprocess.check_output(
                "wmic path win32_VideoController get name", shell=True
            ).decode()
            return output.strip().split("\n")[1]
        except:
            return "Unable to retrieve GPU info on Windows"

    elif system == "darwin":  # macOS
        try:
            output = subprocess.check_output(
                "system_profiler SPDisplaysDataType | grep Vendor", shell=True
            ).decode()
            return output.strip().split(":")[1].strip()
        except:
            return "Unable to retrieve GPU info on macOS"

    elif system == "linux":
        try:
            # Try lspci command first
            output = subprocess.check_output("lspci | grep -i vga", shell=True).decode()
            return output.strip().split(":")[2].strip()
        except:
            try:
                # If lspci fails, try reading from /sys/class/graphics
                with open("/sys/class/graphics/fb0/device/vendor", "r") as f:
                    vendor_id = f.read().strip()
                return f"Vendor ID: {vendor_id}"
            except:
                return "Unable to retrieve GPU info on Linux"

    else:
        return "Unsupported operating system"


def getVendor():
    """
    Gets GPU vendor of the system
    vendors = ["Intel", "AMD", "Nvidia"]
    """
    gpuInfo = get_gpu_info()
    vendors = ["Intel", "AMD", "Nvidia"]
    for vendor in vendors:
        if vendor.lower() in gpuInfo.lower():
            return vendor


def openLink(link: str):
    """
    Opens a link in the default web browser.

    :param link: The link to open.
    :type link: str
    """
    webbrowser.open(link)


def errorAndLog(message: str):
    log("ERROR: " + message)
    raise os.error("ERROR: " + message)


def checkForWritePermissions(dir):
    """
    Checks for write permissions in the current directory.

    Also reads the flatpak-info file to see if the directory is in the current allowed r/w dirs.
    Args:
        - the directory to check if permissions are in
    """

    i = 2  # change this to 1 to debug flatpak
    if "FLATPAK_ID" in os.environ or i == 1:
        with open("/.flatpak-info", "r") as f:
            result = f.readlines()

        directories_with_permissions = []
        for i in result:
            if "filesystems=" in i:
                i = i.split(";")
                s = []
                for e in i:
                    if len(e) > 0 and i != "\n":
                        s.append(e)
                for j in s:
                    j = j.replace("filesystems=", "")
                    if j == "xdg-download":
                        j = f"{homedir}/Downloads"
                    j = j.replace("xdg-", f"{homedir}/")
                    j = j.replace("~", f"{homedir}")
                    directories_with_permissions.append(j)
        for i in directories_with_permissions:
            if dir[-1] != "/":
                dir += "/"
            log(
                f"Checking dir: {i.lower()} is in or equal to Selected Dir: {dir.lower()}"
            )

            if (
                i.lower() in dir.lower()
                or "io.github.tntwise.real-video-enhancer" in dir.lower()
                and ":ro" not in i
            ):
                return True
            else:
                if "/run/user/1000/doc/" in dir:
                    dir = dir.replace("/run/user/1000/doc/", "").split("/")
                    permissions_dir = ""
                    for index in range(len(dir)):
                        if index != 0:
                            permissions_dir += f"{dir[index]}/"
                    if homedir not in permissions_dir:
                        dir = f"{homedir}/{permissions_dir}"
                    else:
                        dir = f"/{permissions_dir}"

                log(
                    f"Checking dir: {i.lower()} is in or equal to Selected Dir: {dir.lower()}"
                )
                if (
                    i.lower() in dir.lower()
                    or "io.github.tntwise.real-video-enhancer" in dir.lower()
                    and ":ro" not in i
                ):
                    return True

        return False
    else:
        if os.access(dir, os.R_OK) and os.access(dir, os.W_OK):
            return True
        return False
