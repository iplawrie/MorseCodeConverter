import sys
import os
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from MorseConverter import *
from Sound import *

class UI_MainWindow(object):
    def setupUI(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        #Base layout for left and right side of window
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 961, 581))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        #Vertical layout for text input
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        #top text input box
        self.Input = QTextEdit(self.horizontalLayoutWidget)
        self.Input.setObjectName(u"Input")
        self.Input.lineWrapMode()
        self.Input.setFontPointSize(14)
        self.Input.setPlaceholderText("Please put text here")
        self.verticalLayout_2.addWidget(self.Input)

        #bottom text input box
        self.Output = QTextEdit(self.horizontalLayoutWidget)
        self.Output.setObjectName(u"Output")
        self.Output.lineWrapMode()
        self.Output.setFontPointSize(16)
        self.Output.setPlaceholderText("Please put morse here")
        self.verticalLayout_2.addWidget(self.Output)

        #add section to base layout
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        #vertical layout for right side buttons
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        #convert text to morse button
        #self.submit = QPushButton(self.horizontalLayoutWidget)
        #elf.submit.setObjectName(u"submit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        #self.submit.setSizePolicy(sizePolicy)
        #self.verticalLayout.addWidget(self.submit)

        #play morse sound
        self.playsound = QPushButton(self.horizontalLayoutWidget)
        self.playsound.setObjectName(u"playsound")
        sizePolicy.setHeightForWidth(self.playsound.sizePolicy().hasHeightForWidth())
        self.playsound.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.playsound)

        #combo box to select audio to play for morse
        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.clear()
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(20, 20))
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox.addItem('Default')
        self.comboBox.addItems(self.getFolderName())

        #add section to base layout
        self.horizontalLayout.addLayout(self.verticalLayout)

        #status bar at bottom of window
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #button presses
        self.morse = MorseConverter()
        #self.submit.clicked.connect(self.outputMorse)
        self.Input.textChanged.connect(self.outputMorse)
        self.Output.textChanged.connect(self.outputText)
        self.playsound.clicked.connect(self.morseSound)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        #self.submit.setText(QCoreApplication.translate("MainWindow", u"Convert ", None))
        self.playsound.setText(QCoreApplication.translate("MainWindow", u"Play Sound ", None))
        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"New Item", None))
    # retranslateUi

    #perform operations
    def outputMorse(self):
        self.Output.textChanged.disconnect(self.outputText)
        text = self.Input.toPlainText()
        try:
            morse = self.morse.morsify(text)
            self.Output.setPlainText(morse)
        except KeyError:
            self.Output.setPlainText("'Bad Input'")
        finally:
            self.Output.textChanged.connect(self.outputText)

    def outputText(self):
        self.Input.textChanged.disconnect(self.outputMorse)
        morse = self.Output.toPlainText()
        try:
            text = self.morse.unmorsify(morse)
            self.Input.setPlainText(text.lower())
        except KeyError:
            self.Input.setPlainText("'Bad Input'")
        finally:
            self.Input.textChanged.connect(self.outputMorse)

    def morseSound(self):
        print("currently playing " + self.comboBox.currentText())
        soundChoice = self.comboBox.currentText()
        if soundChoice == "Default":
            sound = Sound()
        else:
            sound = Sound("./Sounds/"+soundChoice)
        morse = self.Output.toPlainText()
        if morse != "" and morse != "'Bad Input'":
            sound.playSound(morse)

    def getFolderName(self):
        folder = "./Sounds"
        subfolders = [f.name for f in os.scandir(folder) if f.is_dir()]
        return subfolders


if __name__== "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = UI_MainWindow()
    ui.setupUI(window)
    window.setWindowTitle("MIS2100 Morse Converter")
    window.show()
    sys.exit(app.exec_())
