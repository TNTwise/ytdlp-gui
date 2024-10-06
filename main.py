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
import yt_dlp


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(
            2
        )  # i just copy pasted from rve, so i have to set it to this index
        self.__connect__()
        self.videoContainers = ("mp4", "webm")
        self.audioContainers = ("mp3", "wav")

    def __connect__(self):
        self.getDataButton.clicked.connect(self.getData)
        self.startDownloadButton.clicked.connect(lambda: self.download())

    def progress_hook(self, d):
        if d["status"] == "downloading":
            print(d)

    def download(self):
        mediaType = self.formatComboBox.currentText()
        video_url = self.inputFileText.text()
        height = self.resolutionComboBox.currentText()
        extension = self.resolutionComboBox.currentText()
        if mediaType.lower() == "video":
            ydl_opts = {
                "format": f"bestvideo[height<={height}][ext={extension}]+bestaudio/best",
                "ext": [extension],
                "progress_hooks": [self.progress_hook],  # Hook for progress reporting
            }
        elif mediaType.lower() == "audio":
            ydl_opts = {
                "format": f"bestaudio[]",  # Select the best audio format with the desired extension
                "progress_hooks": [self.progress_hook],
                "postprocessors": [
                    {  # Convert audio to the desired format
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": self.audioContainers[
                            0
                        ],  # Desired audio codec (e.g., mp3, wav)
                        "preferredquality": "192",  # Desired quality (if applicable)
                    }
                ],
            }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
        except yt_dlp.utils.DownloadError:
            RegularQTPopup(
                "Cannot download with current settings\n, please change the container!"
            )

    def getData(self):
        youtubeVideoInfoDict = self.getInfoDictFromURL()
        resolutions = self.getContentFromInfoDict(youtubeVideoInfoDict, "height")
        extensions = self.getContentFromInfoDict(youtubeVideoInfoDict, "ext")
        self.populateComboBoxes(resolutions=resolutions, extensions=extensions)

    def populateComboBoxes(self, resolutions, extensions):
        self.resolutionComboBox.addItems(resolutions)
        self.containerComboBox.addItems(extensions)

    def getContentFromInfoDict(self, info_dict, content):
        formats = info_dict.get("formats", [])
        containers = set()
        for format in formats:
            container = format.get(content)  # Get the height of the format
            if container is not None:
                containers.add(container)
        containers = sorted(containers)
        containers.reverse()
        return list(map(str, containers))  # cast every item in here to string

    def getInfoDictFromURL(self) -> dict:
        link = self.inputFileText.text()
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(link, download=False)
        return info_dict

    def getDataFromYoutubeVideo(self):
        # RegularQTPopup("Getting youtube video statistics")
        try:
            ydl_opts = {"format": "bestvideo+bestaudio/best"}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=False)
            print(info_dict)
            self.videoContainer = info_dict["ext"]
            self.inputFile = info_dict["title"] + self.videoContainer
            self.videoWidth = info_dict["width"]
            self.videoHeight = info_dict["height"]
            self.videoFps = info_dict["fps"]
            self.videoEncoder = info_dict["vcodec"]
            self.videoBitrate = info_dict["vbr"]
            self.videoFrameCount = int(info_dict["duration"] * info_dict["fps"])
            print(self.videoContainer)
        except:
            RegularQTPopup("Failed to get youtube video!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # setting the pallette

    app.setPalette(Palette())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
