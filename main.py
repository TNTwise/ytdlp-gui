from PySide6 import QtSvg # import because windows doenst work without this
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
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve
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
        self.stackedWidget.setCurrentIndex(2) # i just copy pasted from rve, so i have to set it to this index
        self.__connect__()

    def __connect__(self):
        self.getDataButton.clicked.connect(self.getData)
    
    def getData(self):
        youtubeVideoInfoDict = self.getInfoDictFromURL()
        resolutions = self.getResolutions(youtubeVideoInfoDict)

    def getResolutions(self, info_dict) -> list:
        formats = info_dict.get('formats', []) 
        resolutions = set()
        for format in formats:
            resolution = format.get('height')  # Get the height of the format
            if resolution and resolution > 178:
                resolutions.add(resolution)
        resolutions = sorted(resolutions)
        resolutions.reverse()
        return resolutions
            
    def getInfoDictFromURL(self) -> dict:
        link = self.inputFileText.text()
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(link, download=False)
        return info_dict
    

    def getResolutionOptions(self) -> dict:
        pass

    def getDataFromYoutubeVideo(self):
        #RegularQTPopup("Getting youtube video statistics")
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
