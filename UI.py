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
        MainWindow.resize(1000, 1000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 961, 581))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Input = QTextEdit(self.horizontalLayoutWidget)
        self.Input.setObjectName(u"Input")
        self.Input.setFontPointSize(14)

        self.verticalLayout_2.addWidget(self.Input)

        self.Output = QTextEdit(self.horizontalLayoutWidget)
        self.Output.setObjectName(u"Output")
        self.Output.setFontPointSize(16)
        self.verticalLayout_2.addWidget(self.Output)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.submit = QPushButton(self.horizontalLayoutWidget)
        self.submit.setObjectName(u"submit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit.sizePolicy().hasHeightForWidth())
        self.submit.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.submit)

        self.playsound = QPushButton(self.horizontalLayoutWidget)
        self.playsound.setObjectName(u"playsound")
        sizePolicy.setHeightForWidth(self.playsound.sizePolicy().hasHeightForWidth())
        self.playsound.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.playsound)

        self.comboBox = QComboBox(self.horizontalLayoutWidget)
       #self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

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
        self.Output.setPlainText(morse.morsify(self.Input.toPlainText()))
        print("The input is '{}'".format(morse.morsify(self.Input.toPlainText())))

    def morseSound(self):
        text = self.Output.toPlainText()
        if text != "":
            self.sound.playSound(text)

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = UI_MainWindow()
    ui.setupUI(window)
    window.show()
    sys.exit(app.exec_())