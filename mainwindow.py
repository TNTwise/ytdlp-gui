# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QStackedWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 712)
        MainWindow.setStyleSheet(
            "\n"
            "\n"
            "QMainWindow {\n"
            "   color:black;\n"
            "   background-color:black;\n"
            "border:1px;\n"
            "}\n"
            "QLabel{\n"
            "	color: #fff;\n"
            "}\n"
            "QLineEdit{\n"
            "color: #fff;\n"
            "}\n"
            "#centralwidget{\n"
            "	background-color:#1f232a;\n"
            "}\n"
            "#leftMenuSubContainer{\n"
            "	background-color:#16191d;\n"
            "   border-radius: 30px;\n"
            "}\n"
            "#bottomMenuSubContainer{\n"
            "	background-color:#2c313c;\n"
            "   border-radius: 30px;\n"
            "}\n"
            "\n"
            "QProgressBar{\n"
            "    background-color:#2c313c;\n"
            "	border-radius: 10px;\n"
            "\n"
            "}\n"
            " QProgressBar::chunk {\n"
            "     background-color:white;\n"
            "	text-align:left;\n"
            "	border-radius: 10px;\n"
            "	\n"
            " }\n"
            "QStackedWidget{\n"
            "	background-color:#16191d;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 25px;\n"
            "}\n"
            "QPlainTextEdit{\n"
            "    background-color:#2c313c;\n"
            "	border-radius: 30px;\n"
            "\n"
            "}\n"
            "QPushButton{\n"
            "    background-color:#2c313c;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "    color: #fff;\n"
            "}\n"
            "QPushButton:checked{\n"
            ""
            "	background-color:#676e7b;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color:#343b47;\n"
            "}\n"
            "\n"
            "QCheckBox{\n"
            "color:#fff;\n"
            "background-color:#fff;\n"
            "}\n"
            ""
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.centralWidget = QWidget(self.centralwidget)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainWindowContainer = QWidget(self.centralWidget)
        self.mainWindowContainer.setObjectName("mainWindowContainer")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mainWindowContainer.sizePolicy().hasHeightForWidth()
        )
        self.mainWindowContainer.setSizePolicy(sizePolicy)
        self.mainWindowContainer.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.mainWindowContainer)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.mainWindowContainer)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet("")
        self.homePage = QWidget()
        self.homePage.setObjectName("homePage")
        self.homePage.setStyleSheet(
            "QWidget{\n"
            "background-color:#16191d\n"
            "\n"
            "}\n"
            "QPushButton{\n"
            "    background-color:#2c313c;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "    color: #fff;\n"
            "}\n"
            "QPushButton:checked{\n"
            "	background-color:#676e7b;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color:#343b47;\n"
            "}\n"
            "QPushButton::toolTip{\n"
            "background-color:#676e7b;\n"
            "}"
        )
        self.gridLayout_2 = QGridLayout(self.homePage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget.addWidget(self.homePage)
        self.morePage = QWidget()
        self.morePage.setObjectName("morePage")
        self.morePage.setStyleSheet("QWidget{\n" "background-color:#16191d\n" "\n" "}")
        self.gridLayout_6 = QGridLayout(self.morePage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedWidget.addWidget(self.morePage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName("mainPage")
        self.mainPage.setStyleSheet(
            "QWidget{\n"
            "background-color:#16191d\n"
            "\n"
            "}\n"
            "QLineEdit{\n"
            "background-color:#2c313c;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "QTextEdit{\n"
            "background-color:#2c313c;\n"
            "border-radius: 10px;\n"
            "padding:5px 10px;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "    background-color:#2c313c;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "}\n"
            "QPushButton:checked{\n"
            "	background-color:#676e7b;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color:#343b47;\n"
            "}\n"
            "\n"
            "QComboBox{\n"
            "background-color:#2c313c;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QProgressBar{\n"
            "    background-color:#2c313c;\n"
            "	border-radius: 10px;\n"
            "\n"
            "}\n"
            " QProgressBar::chunk {\n"
            "     background-color:white;\n"
            "	text-align:left;\n"
            "	border-radius: 10px;\n"
            "	\n"
            " }\n"
            "QCheckBox::indicator{\n"
            "border : 1px solid white;\n"
            "border-radius: 2px;\n"
            "}\n"
            "QCheckBox::indicator::checked{\n"
            "background-color:white;\n"
            "}\n"
            "QDoubleSpinBox{\n"
            "	bac"
            "kground-color:#2c313c;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "	color:white;\n"
            "}\n"
            "QDoubleSpinBox::up-arrow {\n"
            "       \n"
            "		image: url(:/icons/icons/arrow-up.svg); \n"
            "    }\n"
            "QDoubleSpinBox::down-arrow {\n"
            "\n"
            "        image: url(:/icons/icons/arrow-down.svg); \n"
            "		\n"
            "    }\n"
            "QDoubleSpinBox::up-button {\n"
            "        width: 20px;\n"
            "        height: 15px;\n"
            "    }\n"
            "QDoubleSpinBox::down-button {\n"
            "        width: 20px;\n"
            "        height: 15px;\n"
            "    }\n"
            ""
        )
        self.gridLayout_3 = QGridLayout(self.mainPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.processContainer = QWidget(self.mainPage)
        self.processContainer.setObjectName("processContainer")
        self.processContainer.setMaximumSize(QSize(16000, 16777215))
        self.processContainer.setStyleSheet(
            "*:disabled{\n" " \n" "	color:gray;\n" "}"
        )
        self.verticalLayout_7 = QVBoxLayout(self.processContainer)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_2 = QScrollArea(self.processContainer)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 817, 334))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.processSettingsContainer = QWidget(self.scrollAreaWidgetContents_2)
        self.processSettingsContainer.setObjectName("processSettingsContainer")
        self.verticalLayout_17 = QVBoxLayout(self.processSettingsContainer)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.inputFileContainer = QWidget(self.processSettingsContainer)
        self.inputFileContainer.setObjectName("inputFileContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.inputFileContainer)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.inputFileText = QLineEdit(self.inputFileContainer)
        self.inputFileText.setObjectName("inputFileText")
        self.inputFileText.setMinimumSize(QSize(0, 30))
        self.inputFileText.setMaximumSize(QSize(16777215, 30))
        self.inputFileText.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.inputFileText)

        self.getDataButton = QPushButton(self.inputFileContainer)
        self.getDataButton.setObjectName("getDataButton")
        self.getDataButton.setMinimumSize(QSize(0, 30))
        self.getDataButton.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(15)
        self.getDataButton.setFont(font)
        self.getDataButton.setStyleSheet("")

        self.horizontalLayout_4.addWidget(self.getDataButton)

        self.verticalLayout_17.addWidget(self.inputFileContainer)

        self.outputFileContainer = QWidget(self.processSettingsContainer)
        self.outputFileContainer.setObjectName("outputFileContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.outputFileContainer)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.outputFileSelectButton = QPushButton(self.outputFileContainer)
        self.outputFileSelectButton.setObjectName("outputFileSelectButton")
        self.outputFileSelectButton.setEnabled(False)
        self.outputFileSelectButton.setMinimumSize(QSize(0, 30))
        self.outputFileSelectButton.setMaximumSize(QSize(16777215, 30))
        self.outputFileSelectButton.setFont(font)
        self.outputFileSelectButton.setStyleSheet("")

        self.horizontalLayout_5.addWidget(self.outputFileSelectButton)

        self.outputFileText = QLineEdit(self.outputFileContainer)
        self.outputFileText.setObjectName("outputFileText")
        self.outputFileText.setEnabled(False)
        self.outputFileText.setMinimumSize(QSize(0, 30))
        self.outputFileText.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_5.addWidget(self.outputFileText)

        self.verticalLayout_17.addWidget(self.outputFileContainer)

        self.widget_3 = QWidget(self.processSettingsContainer)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_12)

        self.formatComboBox = QComboBox(self.widget_3)
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.setObjectName("formatComboBox")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.formatComboBox.sizePolicy().hasHeightForWidth()
        )
        self.formatComboBox.setSizePolicy(sizePolicy1)
        self.formatComboBox.setMinimumSize(QSize(0, 0))
        self.formatComboBox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_11.addWidget(self.formatComboBox)

        self.verticalLayout_17.addWidget(self.widget_3)

        self.widget = QWidget(self.processSettingsContainer)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font)

        self.horizontalLayout.addWidget(self.label_7)

        self.resolutionComboBox = QComboBox(self.widget)
        self.resolutionComboBox.setObjectName("resolutionComboBox")
        sizePolicy1.setHeightForWidth(
            self.resolutionComboBox.sizePolicy().hasHeightForWidth()
        )
        self.resolutionComboBox.setSizePolicy(sizePolicy1)
        self.resolutionComboBox.setMinimumSize(QSize(250, 0))
        self.resolutionComboBox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.resolutionComboBox)

        self.verticalLayout_17.addWidget(self.widget)

        self.widget_5 = QWidget(self.processSettingsContainer)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_14)

        self.containerComboBox = QComboBox(self.widget_5)
        self.containerComboBox.setObjectName("containerComboBox")
        sizePolicy1.setHeightForWidth(
            self.containerComboBox.sizePolicy().hasHeightForWidth()
        )
        self.containerComboBox.setSizePolicy(sizePolicy1)
        self.containerComboBox.setMinimumSize(QSize(250, 0))
        self.containerComboBox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_13.addWidget(self.containerComboBox)

        self.verticalLayout_17.addWidget(self.widget_5)

        self.gridLayout_4.addWidget(self.processSettingsContainer, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.widget_2 = QWidget(self.processContainer)
        self.widget_2.setObjectName("widget_2")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_13 = QVBoxLayout(self.widget_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.videoInfoContainer = QWidget(self.widget_2)
        self.videoInfoContainer.setObjectName("videoInfoContainer")
        self.videoInfoContainer.setMinimumSize(QSize(0, 0))
        self.videoInfoContainer.setMaximumSize(QSize(16777215, 300))
        self.videoInfoContainer.setStyleSheet(
            "QWidget {\n"
            "	background-color:#1f232a;\n"
            "	border-radius:10px;\n"
            "}"
        )
        self.verticalLayout_10 = QVBoxLayout(self.videoInfoContainer)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.videoInfoTextEdit = QTextEdit(self.videoInfoContainer)
        self.videoInfoTextEdit.setObjectName("videoInfoTextEdit")
        self.videoInfoTextEdit.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.videoInfoTextEdit.sizePolicy().hasHeightForWidth()
        )
        self.videoInfoTextEdit.setSizePolicy(sizePolicy)
        self.videoInfoTextEdit.setMinimumSize(QSize(0, 0))
        self.videoInfoTextEdit.setMaximumSize(QSize(16777215, 160))
        font1 = QFont()
        font1.setPointSize(20)
        self.videoInfoTextEdit.setFont(font1)
        # if QT_CONFIG(accessibility)
        self.videoInfoTextEdit.setAccessibleDescription("")
        # endif // QT_CONFIG(accessibility)
        self.videoInfoTextEdit.setStyleSheet(
            "QTextEdit{\n"
            "background-color:#343b47;\n"
            "color:white;\n"
            "}\n"
            "QTextEdit:disabled{color:white;}"
        )
        self.videoInfoTextEdit.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.videoInfoTextEdit.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.videoInfoTextEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.videoInfoTextEdit)

        self.verticalLayout_13.addWidget(self.videoInfoContainer)

        self.verticalLayout_7.addWidget(self.widget_2)

        self.bottomMenuSubContainer = QWidget(self.processContainer)
        self.bottomMenuSubContainer.setObjectName("bottomMenuSubContainer")
        self.bottomMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.bottomMenuSubContainer.setStyleSheet(
            "#bottomMenuSubContainer{\n"
            "background-color:#1f232a\n"
            "}\n"
            "#progressBar{\n"
            "background-color:#343b47\n"
            "}\n"
            "#startRenderButton{\n"
            "background-color:#343b47\n"
            "}\n"
            "#startRenderButton:hover{\n"
            "background-color:#676e7b\n"
            "}"
        )
        self.horizontalLayout_2 = QHBoxLayout(self.bottomMenuSubContainer)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startDownloadButton = QPushButton(self.bottomMenuSubContainer)
        self.startDownloadButton.setObjectName("startDownloadButton")
        self.startDownloadButton.setEnabled(True)
        self.startDownloadButton.setMaximumSize(QSize(59, 16777215))
        self.startDownloadButton.setStyleSheet("")
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/arrow-down-circle.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.startDownloadButton.setIcon(icon)
        self.startDownloadButton.setIconSize(QSize(55, 40))
        self.startDownloadButton.setCheckable(True)
        self.startDownloadButton.setChecked(False)

        self.horizontalLayout_2.addWidget(self.startDownloadButton)

        self.progressBar = QProgressBar(self.bottomMenuSubContainer)
        self.progressBar.setObjectName("progressBar")
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.verticalLayout_7.addWidget(self.bottomMenuSubContainer)

        self.gridLayout_3.addWidget(self.processContainer, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.mainPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName("settingsPage")
        self.settingsPage.setStyleSheet(
            "QWidget{\n"
            "background-color:#16191d\n"
            "\n"
            "}\n"
            "QLineEdit{\n"
            "background-color:#2c313c;\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "QTextEdit{\n"
            "background-color:#2c313c;\n"
            "border-radius: 10px;\n"
            "padding:5px 10px;\n"
            "}\n"
            "\n"
            "QPushButton{\n"
            "    background-color:#2c313c;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "}\n"
            "QPushButton:checked{\n"
            "	background-color:#676e7b;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color:#343b47;\n"
            "}\n"
            "\n"
            "QComboBox{\n"
            "background-color:#2c313c;\n"
            "	text-align:left;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "color:white;\n"
            "}\n"
            "\n"
            "QProgressBar{\n"
            "    background-color:#2c313c;\n"
            "	border-radius: 10px;\n"
            "\n"
            "}\n"
            " QProgressBar::chunk {\n"
            "     background-color:white;\n"
            "	text-align:left;\n"
            "	border-radius: 10px;\n"
            "	\n"
            " }\n"
            "QCheckBox::indicator{\n"
            "border : 1px solid white;\n"
            "border-radius: 2px;\n"
            "}\n"
            "QCheckBox::indicator::checked{\n"
            "background-color:white;\n"
            "}\n"
            "\n"
            "Line{\n"
            "color:whi"
            "te;\n"
            "background-color:white;\n"
            "}\n"
            "QDoubleSpinBox{\n"
            "	background-color:#2c313c;\n"
            "	padding:5px 10px;\n"
            "	border-radius: 10px;\n"
            "	color:white;\n"
            "}\n"
            "QDoubleSpinBox::up-arrow {\n"
            "       \n"
            "		image: url(:/icons/icons/arrow-up.svg); \n"
            "    }\n"
            "QDoubleSpinBox::down-arrow {\n"
            "\n"
            "        image: url(:/icons/icons/arrow-down.svg); \n"
            "		\n"
            "    }\n"
            "QDoubleSpinBox::up-button {\n"
            "        width: 20px;\n"
            "        height: 15px;\n"
            "    }\n"
            "QDoubleSpinBox::down-button {\n"
            "        width: 20px;\n"
            "        height: 15px;\n"
            "    }\n"
            ""
        )
        self.verticalLayout_14 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.stackedWidget.addWidget(self.settingsPage)

        self.horizontalLayout_3.addWidget(self.stackedWidget)

        self.verticalLayout_2.addWidget(self.mainWindowContainer)

        self.gridLayout.addWidget(self.centralWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.inputFileText.setText("")
        self.inputFileText.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Paste YouTube link here", None)
        )
        self.getDataButton.setText(
            QCoreApplication.translate("MainWindow", "Get Data", None)
        )
        self.outputFileSelectButton.setText(
            QCoreApplication.translate("MainWindow", "Select Output Folder", None)
        )
        self.label_12.setText(QCoreApplication.translate("MainWindow", "Format", None))
        self.formatComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", "Video", None)
        )
        self.formatComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", "Audio", None)
        )

        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "Resolution", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Container", None)
        )
        self.videoInfoTextEdit.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "hr { height: 1px; border-width: 0; }\n"
                'li.unchecked::marker { content: "\\2610"; }\n'
                'li.checked::marker { content: "\\2612"; }\n'
                "</style></head><body style=\" font-family:'Sans Serif'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Title: </p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Highest resolution:</p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Frame Count:</p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margi'
                'n-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
                None,
            )
        )
        self.startDownloadButton.setText("")

    # retranslateUi
