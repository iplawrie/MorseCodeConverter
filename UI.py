import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from MorseConverter import *
from MorseDict import MorseDict
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
        self.Input.setPlaceholderText("Please put sentence to be converted here")
        self.verticalLayout_2.addWidget(self.Input)

        #bottom text input box
        self.Output = QTextEdit(self.horizontalLayoutWidget)
        self.Output.setObjectName(u"Output")
        self.Output.lineWrapMode()
        self.Output.setFontPointSize(16)
        self.Output.setPlaceholderText("Morse will be converted here")
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
        self.submit = QPushButton(self.horizontalLayoutWidget)
        self.submit.setObjectName(u"submit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.submit)

        #play morse sound
        self.playsound = QPushButton(self.horizontalLayoutWidget)
        self.playsound.setObjectName(u"playsound")
        sizePolicy.setHeightForWidth(self.playsound.sizePolicy().hasHeightForWidth())
        self.playsound.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.playsound)

        #combo box to select audio to play for morse
        self.comboBox = QComboBox(self.horizontalLayoutWidget)
       #self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(20, 20))
        self.verticalLayout.addWidget(self.comboBox)

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
        self.sound = Sound()
        self.submit.clicked.connect(self.outputMorse)
        self.playsound.clicked.connect(self.morseSound)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"Convert ", None))
        self.playsound.setText(QCoreApplication.translate("MainWindow", u"Play Sound ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"New Item", None))
    # retranslateUi

    #perform operations
    def outputMorse(self):
        morse = MorseConverter(MorseDict)
        text = self.Input.toPlainText()
        self.Output.setPlainText(morse.morsify(text))
        print("The input is '{}'".format(morse.morsify(self.Input.toPlainText())))

    def morseSound(self):
        morse = self.Output.toPlainText()
        if morse != "":
            self.sound.playSound(morse)

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = UI_MainWindow()
    ui.setupUI(window)
    window.setWindowTitle("MIS2100 Morse Converter")
    window.show()
    sys.exit(app.exec_())
