
from translate import Translator
import speech_recognition as sr
from gtts import gTTS
import os
# import sounddevice as sd
# import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGraphicsView,QGraphicsScene
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        MainWindow.setWindowIcon(QtGui.QIcon('Icon.png'))
        MainWindow.setStyleSheet("background-image: url(Icon.png)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.setWindowIcon(QtGui.QIcon('icon.png'))

        #exit button

        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(300, 520, 75, 31))
        self.exitButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(18)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        # heading1

        self.headLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.headLabel1.setGeometry(QtCore.QRect(100, 0, 211, 31))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(20)
        font.setUnderline(True)
        self.headLabel1.setFont(font)
        self.headLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.headLabel1.setObjectName("headLabel1")

        #input language combobox

        self.inputlangbox = QtWidgets.QComboBox(self.centralwidget)
        self.inputlangbox.setGeometry(QtCore.QRect(140, 130, 181, 22))
        self.inputlangbox.setMaxVisibleItems(10)
        self.inputlangbox.setObjectName("inputlangbox")
        self.inputlangbox.addItem(' ')
        self.inputlangbox.addItem('English')
        self.inputlangbox.addItem('Italian')
        self.inputlangbox.addItem('French')
        self.inputlangbox.addItem('Spanish')
        self.inputlangbox.addItem('German')
        self.inputlangbox.addItem('Hungarian')
        self.inputlangbox.addItem('Russian')
        self.inputlangbox.addItem('Czech')
        self.inputlangbox.addItem('Greek')
        self.inputlangbox.addItem('Polish')
        self.inputlangbox.addItem('Portuguese')
        self.inputlangbox.addItem('Turkish')
        self.inputlangbox.addItem('Romanian')
        self.inputlangbox.addItem('Swedish')
        self.inputlangbox.addItem('Danish')


        # Speak Button

        self.speakbttn = QtWidgets.QPushButton(self.centralwidget)
        self.speakbttn.setGeometry(QtCore.QRect(30, 250, 51, 31))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(11)
        self.speakbttn.setFont(font)
        self.speakbttn.setObjectName("speakbttn")
        self.speakbttn.clicked.connect(self.SpeakBttnClicked)


        # label for what is your language

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        # label to show the input language

        self.inputlabel = QtWidgets.QLabel(self.centralwidget)
        self.inputlabel.setGeometry(QtCore.QRect(139, 250, 250, 31))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(14)
        self.inputlabel.setFont(font)
        self.inputlabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputlabel.setObjectName("inputlabel")
        self.inputlabel.setStyleSheet("background-color: rgba(255,255,255);")

        #the second heading

        self.headlabel2 = QtWidgets.QLabel(self.centralwidget)
        self.headlabel2.setGeometry(QtCore.QRect(90, 40, 251, 20))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(12)
        font.setUnderline(True)
        self.headlabel2.setFont(font)
        self.headlabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.headlabel2.setObjectName("headlabel2")

        #label for the output

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 200, 111, 21))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")

        # combobox to select the output language

        self.outputlangbox = QtWidgets.QComboBox(self.centralwidget)
        self.outputlangbox.setGeometry(QtCore.QRect(140, 200, 181, 22))
        self.outputlangbox.setObjectName("outputlangbox")
        self.outputlangbox.addItem(' ')
        self.outputlangbox.addItem('English')
        self.outputlangbox.addItem('Italian')
        self.outputlangbox.addItem('French')
        self.outputlangbox.addItem('Spanish')
        self.outputlangbox.addItem('German')
        self.outputlangbox.addItem('Hungarian')
        self.outputlangbox.addItem('Russian')
        self.outputlangbox.addItem('Czech')
        self.outputlangbox.addItem('Greek')
        self.outputlangbox.addItem('Polish')
        self.outputlangbox.addItem('Portuguese')
        self.outputlangbox.addItem('Turkish')
        self.outputlangbox.addItem('Romanian')
        self.outputlangbox.addItem('Swedish')
        self.outputlangbox.addItem('Danish')


        # the label for the translated to

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(20, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(12)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")

        # label to contain the output text

        self.outlabel = QtWidgets.QLabel(self.centralwidget)
        self.outlabel.setGeometry(QtCore.QRect(139, 320, 250, 31))
        self.outlabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        font = QtGui.QFont()
        font.setFamily("icon-ui")
        font.setPointSize(14)
        self.outlabel.setFont(font)
        self.outlabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outlabel.setObjectName("outlabel")
        self.outlabel.setStyleSheet("background-color: rgba(255,255,255);")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # speak Button Function

    def SpeakBttnClicked(self):

        combotxt1 = self.outputlangbox.currentText()
        combotxt2 = self.inputlangbox.currentText()
        print(combotxt1)
        print(combotxt2)

        # output conversion

        if combotxt1 == "German":
            op = "de"
        if combotxt1 == "English":
            op = "en"
        if combotxt1 == "Russian":
            op = "ru"
        if combotxt1 == "Italian":
            op = "it"
        if combotxt1 == "French":
            op = "fr"
        if combotxt1 == "Hungarian":
            op = "hu"
        if combotxt1 == "Greek":
            op = "el"
        if combotxt1 == "Czech":
            op = "cs"
        if combotxt1 == "Spanish":
            op = "es"
        if combotxt1 == "Polish":
            op = "pl"
        if combotxt1 == "Portuguese":
            op = "pt-PT"
        if combotxt1 == "Turkish":
            op = "tr"
        if combotxt1 == "Romanian":
            op = "ro"
        if combotxt1 == "Swedish":
            op = "sv"
        if combotxt1 == "Danish":
            op = "da"

        #input conversion

        if combotxt2 == "German":
            inp = "de"
        if combotxt2 == "English":
            inp = "en"
        if combotxt2 == "Russian":
            inp = "ru"
        if combotxt2 == "Italian":
            inp = "it"
        if combotxt2 == "French":
            inp = "fr"
        if combotxt2 == "Hungarian":
            inp = "hu"
        if combotxt2 == "Greek":
            inp = "el"
        if combotxt2 == "Czech":
            inp = "cs"
        if combotxt2 == "Spanish":
            inp = "es"
        if combotxt2 == "Polish":
            inp = "pl"
        if combotxt2 == "Portuguese":
            inp = "pt-PT"
        if combotxt2 == "Turkish":
            inp = "tr"
        if combotxt2 == "Romanian":
            inp = "ro"
        if combotxt2 == "Swedish":
            inp = "sv"
        if combotxt2 == "Danish":
            inp = "da"

        # voice output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak :")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                translator= Translator(from_lang = inp , to_lang = op)
                translation = translator.translate(text)
                self.inputlabel.setText(text)
                self.outlabel.setText(translation)
                mytext = translation
                language = op
                myobj = gTTS(text = mytext, lang=language, slow=False)
                myobj.save("testcase1.mp3")
                os.system("fmedia testcase1.mp3 --background")
            except:
                print("Sorry could not recognize what you said")
                self.inputlabel.setText("Sorry! Can't recognise")
                self.outlabel.setText("Sorry! Can't recognise")
        # translator= Translator(from_lang = inp , to_lang = op)
        # translation = translator.translate(text)
        #print (translation)
        #self.inputlabel.setText(text)
        #self.outlabel.setText(translation)
        # voice output
        #mytext = translation
        #language = op
        #myobj = gTTS(text = mytext, lang=language, slow=False)
        #myobj.save("testcase1.mp3")
        #os.system("fmedia testcase1.mp3 --background")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speak GO - European version"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.headLabel1.setText(_translate("MainWindow", "Speak Go"))
        self.speakbttn.setText(_translate("MainWindow", "Speak"))
        self.label1.setText(_translate("MainWindow", "Your Language"))
        self.headlabel2.setText(_translate("MainWindow", "Made for the European Union"))
        self.label2.setText(_translate("MainWindow", "Translate to"))
        self.label3.setText(_translate("MainWindow", "Translated text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
