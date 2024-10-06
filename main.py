from PySide6 import QtSvg  # import because windows doenst work without this
from mainwindow import Ui_MainWindow
import sys
import os

# patch for macos
if sys.platform == "darwin":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # this goes one step up, and goes into the actual directory. This is where backend will be copied to.
    os.chdir("..")
import subprocess
import re
import math
import certifi
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QGraphicsOpacityEffect,
    QWidget,
)
from QtCustom import RegularQTPopup
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QThread
from PySide6.QtGui import QIcon
from mainwindow import Ui_MainWindow  # Import the UI class from the converted module
from PySide6 import QtSvg  # Import the QtSvg module so svg icons can be used on windows

# other imports
from QTStyle import Palette
from QtCustom import SettingUpBackendPopup, DownloadProgressPopup, DisplayCommandOutputPopup
from Util import pythonPath, backendDirectory, makeExecutable, currentDirectory, extractTarGZ, getPlatform
from platform import machine


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(
            2
        )  # i just copy pasted from rve, so i have to set it to this index
        self.__connect__()
        self.downloadPython()
        self.pipInstall(["yt-dlp"])
        

    def __connect__(self):
        self.getDataButton.clicked.connect(self.getData)
        self.startDownloadButton.clicked.connect(lambda: self.download())

    def downloadPython(self):
        if not os.path.exists(pythonPath()):
            os.makedirs(os.path.join(currentDirectory(), "python"), exist_ok=True)
            link = "https://github.com/indygreg/python-build-standalone/releases/download/20240814/cpython-3.11.9+20240814-"
            pyDir = os.path.join(
                currentDirectory(),
                "python",
                "python.tar.gz",
            )
            match getPlatform():
                case "linux":
                    link += "x86_64-unknown-linux-gnu-install_only.tar.gz"
                case "win32":
                    link += "x86_64-pc-windows-msvc-install_only.tar.gz"
                case "darwin":
                    if machine() == "arm64":
                        link += "aarch64-apple-darwin-install_only.tar.gz"
                    else:
                        link += "x86_64-apple-darwin-install_only.tar.gz"
            # probably can add macos support later
            print("Downloading Python")
            DownloadProgressPopup(
                link=link, downloadLocation=pyDir, title="Downloading Python"
            )

            # extract python
            extractTarGZ(pyDir)

            # give executable permissions to python
            makeExecutable(pythonPath())
    def pipInstall(
        self, deps: list
    ):  # going to have to make this into a qt module pop up
        command = [
            pythonPath(),
            "-m",
            "pip",
            "install",
            "-U",
            "--no-warn-script-location",
            "--cache-dir=" + os.path.join(currentDirectory(), "pip_cache"),
        ] + deps
        # totalDeps = self.get_total_dependencies(deps)
        totalDeps = len(deps)
        print("Downloading Deps: " + str(command))
        print("Total Dependencies: " + str(totalDeps))

        DisplayCommandOutputPopup(
            command=command,
            title="Download Dependencies",
            progressBarLength=totalDeps,
        )
        command = [
            pythonPath(),
            "-m",
            "pip",
            "cache",
            "purge",
        ]
        DisplayCommandOutputPopup(
            command=command,
            title="Purging Cache",
            progressBarLength=1,
        )
        
    def getData(self):
        link = self.inputFileText.text()
        resolutions = self.getResolutionsFromBackend(link)
        self.populateComboBoxes(resolutions=resolutions)

    def populateComboBoxes(self, resolutions):
        self.resolutionComboBox.addItems(resolutions)

    def getResolutionsFromBackend(self,link):
        
        self.process = subprocess.Popen(
            [
                pythonPath(),
                os.path.join(backendDirectory(), "backend.py"),
                "--getAvailableHeights",
                "--url",
                link,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )
        self.process.wait()
        totalOutput = ""
        for line in iter(self.process.stdout.readline, ""):
            totalOutput += line
        
        output = totalOutput
        # hack to filter out bad find
        new_out = ""
        for word in output:
            if "objc" in word:
                continue
            new_out += word + " "
        output = new_out
        # Find the part of the output containing the backends list
        start = output.find("[")
        end = output.find("]") + 1
        backends_str = output[start:end]

        # Convert the string representation of the list to an actual list
        backends:list[str] = eval(backends_str)
        n = []
        for i in backends:
            n.append(str(i.strip().replace(" ", "")))
        return n

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # setting the pallette

    app.setPalette(Palette())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
