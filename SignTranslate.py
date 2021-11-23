# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pertama.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import time
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets
# from hasilCari import Ui_hasilPencarian
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWidgets import QStyle, QFileDialog, QWidget, QSplashScreen 
from PyQt5.QtGui import QIcon, QPixmap
global kataKata
# global textPencarianLagi




class Ui_menuPencarian(object):


    def searchING(self):
        try:
            global kataKata
            kataKata = self.textPencarian.toPlainText()
            self.textPencarian.setText("")
            print(kataKata)
            sear(self)

        except:
            menuPencarian.show()
            self.splash = QSplashScreen(QPixmap('Photo/cap.png'))
            self.splash.show()
            QTimer.singleShot(2000, self.splash.close)
            

        # global saga
        # saga()
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_hasilPencarian()
        # self.ui.setupUi(self.window)
        # self.window.show()

    def tamtam(self):
        hanz(self)


    # global search

    # def search(self):
    #     global textPencarianLagi
    #     kataKata = self.textPencarianLagi.toPlainText()
    #     self.window.hide()
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_hasilPencarian()
    #     self.ui.setupUi(self.window)
    #     self.window.show()


    def setupUi(self, menuPencarian):
        menuPencarian.setObjectName("menuPencarian")
        menuPencarian.resize(965, 496)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        menuPencarian.setFont(font)
        menuPencarian.setWindowIcon(QtGui.QIcon('Photo/log.png'))
        self.centralwidget = QtWidgets.QWidget(menuPencarian)
        self.centralwidget.setObjectName("centralwidget")
        self.tombolPencarian = QtWidgets.QPushButton(self.centralwidget)
        self.tombolPencarian.setGeometry(QtCore.QRect(570, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tombolPencarian.setFont(font)
        self.tombolPencarian.setObjectName("tombolPencarian")

        self.tombolPencarian.clicked.connect(self.searchING)

        self.textPencarian = QtWidgets.QTextEdit(self.centralwidget)
        self.textPencarian.setGeometry(QtCore.QRect(270, 280, 291, 41))


        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.textPencarian.setFont(font)
        self.textPencarian.setObjectName("textPencarian")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 50, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Photo/log.png")) #path1 (gambar log.png)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 170, 371, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Photo/output-onlinejpgtools.png")) #path2 (gambar output-onlinejpgtools.png )
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        menuPencarian.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(menuPencarian)
        self.statusbar.setObjectName("statusbar")
        menuPencarian.setStatusBar(self.statusbar)

        self.derpderp = QtWidgets.QPushButton(self.centralwidget)
        self.derpderp.setGeometry(QtCore.QRect(840, 400, 75, 75))
        self.derpderp.setObjectName("derpderp")
        self.derpderp.setIcon(QIcon("Photo/baka.png"))
        self.derpderp.setIconSize(QtCore.QSize(82,82))
        self.derpderp.clicked.connect(self.tamtam)


        self.retranslateUi(menuPencarian)
        QtCore.QMetaObject.connectSlotsByName(menuPencarian)


    def retranslateUi(self, menuPencarian):
        _translate = QtCore.QCoreApplication.translate
        menuPencarian.setWindowTitle(_translate("menuPencarian", "Sign Translate"))
        self.tombolPencarian.setText(_translate("menuPencarian", "Translate"))
        self.textPencarian.setHtml(_translate("menuPencarian", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Reference Sans Serif\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Gothic\'; font-size:12pt;\"><br /></p></body></html>"))

class Ui_hasilPencarian(object):
    global sear

    def sear(self):
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hasilPencarian()
        self.ui.setupUi(self.window)
        menuPencarian.hide()
        self.window.show()
        global sasawi
        def sasawi():
            self.window.hide()
        global tampil
        def tampil():
            self.window.show()
            pass
        # self.window.hide()
        # global glo
        # glo = self.window.hide()

    def search(self):
        try:
            global kataKata
            kataKata=self.textPencarianLagi.toPlainText()
            sasawi()
            sear(self)
        
            
        except:
            tampil()
            self.splash = QSplashScreen(QPixmap('Photo/cap.png'))
            self.splash.show()
            QTimer.singleShot(2000, self.splash.close)

    def balikan(self):
        sasawi()
        menuPencarian.show()
        # global menuPencarian
        # bara()
        # global menuPencarian
        # menuPencarian = QtWidgets.QMainWindow()
        # ui = Ui_menuPencarian()
        # ui.setupUi(menuPencarian)
        # menuPencarian.show()
        # sys.exit(app.exec_())

        # self.menuPencarian = QtWidgets.QMainWindow()
        # self.ui = Ui_menuPencarian()
        # self.ui.setupUi(self.menuPencarian)
        # self.menuPencarian.show()

        # self.app= QtWidgets.QApplication(sys.argv)
        # self.menuPencarian = QtWidgets.QMainWindow()
        # self.ui = Ui_menuPencarian()
        # self.ui.setupUi(self.menuPencarian)
        # self.menuPencarian.show()

        # self.dabo = QtWidgets.QMainWindow()
        # self.ui = Ui_menuPencarian()
        # self.ui.setupUi(self.dabo)
        # self.dabo.show()
        # # self.dabo.close()
        # global saga
        # def saga(self):
        #     self.dabo.close()


    def setupUi(self, hasilPencarian):
        print(kataKata)
        vidkata = kataKata.lower()
        print(vidkata)
        awalan= "Vocabulary/" #path3 (folder Vocabulary)
        bentukanvid=".avi"
        bentukantxt=".txt"
        tempatvid= awalan + vidkata + bentukanvid
        tempattxt= awalan + vidkata + bentukantxt

        setting_data = open(tempattxt, 'r')
        lines = setting_data.readlines()
        limited_n_ints = ''
        for i in lines:
            limited_n_ints = limited_n_ints + i
        print(limited_n_ints)


        print(tempatvid)

        hasilPencarian.setObjectName("hasilPencarian")
        hasilPencarian.resize(993, 490)

        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        hasilPencarian.setFont(font)
        self.centralwidget = QtWidgets.QWidget(hasilPencarian)
        self.centralwidget.setObjectName("centralwidget")
        hasilPencarian.setWindowIcon(QtGui.QIcon('Photo/log.png'))
        self.logosfx = QtWidgets.QLabel(self.centralwidget)
        self.logosfx.setGeometry(QtCore.QRect(60, 20, 81, 81))
        self.logosfx.setText("")
        self.logosfx.setPixmap(QtGui.QPixmap("Photo/log.png")) #path1 ()
        self.logosfx.setScaledContents(True)
        self.logosfx.setObjectName("logosfx")

        self.tulisansfx = QtWidgets.QLabel(self.centralwidget)
        self.tulisansfx.setGeometry(QtCore.QRect(150, 30, 301, 71))
        self.tulisansfx.setText("")
        self.tulisansfx.setPixmap(QtGui.QPixmap("Photo/output-onlinejpgtools.png"))
        self.tulisansfx.setScaledContents(True)
        self.tulisansfx.setObjectName("tulisansfx")

        self.textPencarianLagi = QtWidgets.QTextEdit(self.centralwidget)
        self.textPencarianLagi.setGeometry(QtCore.QRect(500, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(16)
        self.textPencarianLagi.setFont(font)
        self.textPencarianLagi.setObjectName("textPencarianLagi")

        self.tomboPencarianLagi = QtWidgets.QPushButton(self.centralwidget)
        self.tomboPencarianLagi.setGeometry(QtCore.QRect(750, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.tomboPencarianLagi.setFont(font)
        self.tomboPencarianLagi.setObjectName("tomboPencarianLagi")
        self.tomboPencarianLagi.clicked.connect(self.search)

        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(50, 120, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")

        self.labelSubText = QtWidgets.QLabel(self.centralwidget)
        self.labelSubText.setGeometry(QtCore.QRect(60, 230, 391, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelSubText.setFont(font)
        self.labelSubText.setMouseTracking(False)
        self.labelSubText.setAutoFillBackground(False)
        self.labelSubText.setLineWidth(1)
        self.labelSubText.setScaledContents(False)
        self.labelSubText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelSubText.setWordWrap(True)
        self.labelSubText.setObjectName("labelSubText")

        self.frametulisan = QtWidgets.QFrame(self.centralwidget)
        self.frametulisan.setGeometry(QtCore.QRect(20, 120, 461, 321))
        self.frametulisan.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frametulisan.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frametulisan.setLineWidth(30)
        self.frametulisan.setMidLineWidth(0)
        self.frametulisan.setObjectName("frametulisan")

        self.frametulisan_2 = QtWidgets.QFrame(self.centralwidget)
        self.frametulisan_2.setGeometry(QtCore.QRect(490, 120, 461, 321))
        self.frametulisan_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frametulisan_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frametulisan_2.setLineWidth(30)
        self.frametulisan_2.setMidLineWidth(0)
        self.frametulisan_2.setObjectName("frametulisan_2")

        self.tombolReplay = QtWidgets.QPushButton(self.frametulisan_2)
        self.tombolReplay.setGeometry(QtCore.QRect(20, 260, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.tombolReplay.setFont(font)
        self.tombolReplay.setObjectName("tombolReplay")
        self.tombolReplay.clicked.connect(self.play_video)


        self.labelSubText.setText(limited_n_ints)


        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.frameVideo = QtMultimediaWidgets.QVideoWidget(self.frametulisan_2)
        self.frameVideo.setGeometry(QtCore.QRect(19, 19, 421, 231))
        self.frameVideo.setObjectName("frameVideo")
        
        # videowidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(self.frameVideo)


        # self.playBtn.setEnabled(True)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(tempatvid)))

        self.mediaPlayer.play()



        self.horizontalSlider = QtWidgets.QSlider(self.frametulisan_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 270, 341, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0,0)
        self.horizontalSlider.sliderMoved.connect(self.set_position)

        self.homee = QtWidgets.QPushButton(self.centralwidget)
        self.homee.setGeometry(QtCore.QRect(870, 20, 70, 70))
        self.homee.setObjectName("homee")
        self.homee.setIcon(QIcon("Photo/boko.png"))
        self.homee.setIconSize(QtCore.QSize(72,72))
        self.homee.clicked.connect(self.balikan)

        self.frametulisan_2.raise_()
        self.logosfx.raise_()
        self.tulisansfx.raise_()
        self.textPencarianLagi.raise_()
        self.tomboPencarianLagi.raise_()
        self.labelTitle.raise_()
        self.labelSubText.raise_()
        self.frametulisan.raise_()
        hasilPencarian.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(hasilPencarian)
        self.statusbar.setObjectName("statusbar")
        hasilPencarian.setStatusBar(self.statusbar)

        self.retranslateUi(hasilPencarian)
        QtCore.QMetaObject.connectSlotsByName(hasilPencarian)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    def retranslateUi(self, hasilPencarian):
        _translate = QtCore.QCoreApplication.translate
        hasilPencarian.setWindowTitle(_translate("hasilPencarian", "Sign Translate"))
        self.tomboPencarianLagi.setText(_translate("hasilPencarian", "Translate"))
        self.labelTitle.setText(_translate("hasilPencarian", kataKata.upper()))

        # self.labelSubText.setText(_translate("hasilPencarian", limited_n_ints))
        self.tombolReplay.setText(_translate("hasilPencarian", "Pause"))


    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()


    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.tombolReplay.setText("Pause")


        else:
            self.tombolReplay.setText("Start")

            

    def position_changed(self, position):
        self.horizontalSlider.setValue(position)


    def duration_changed(self, duration):
        self.horizontalSlider.setRange(0, duration)


    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


# def bara():
#     # app= QtWidgets.QApplication(sys.argv)
#     global menuPencarian
#     menuPencarian = QtWidgets.QMainWindow()
#     ui = Ui_menuPencarian()
#     ui.setupUi(menuPencarian)
#     menuPencarian.show()

class Ui_tambahan(QWidget):
    global hanz
    def hanz(self):
        menuPencarian.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_tambahan()
        self.ui.setupUi(self.window)
        self.window.show()
        global sasai
        def sasai():
            self.window.close()
        # self.window.hide()
        # global glo
        # glo = self.window.hide()

    def jobno(self):
        sasai()
        menuPencarian.show()
        # self.menuPencarian = QtWidgets.QMainWindow()
        # self.ui = Ui_menuPencarian()
        # self.ui.setupUi(self.menuPencarian)
        # self.menuPencarian.show()



    def setupUi(self, tambahan):
        tambahan.setObjectName("tambahan")
        tambahan.resize(993, 490)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        tambahan.setFont(font)
        tambahan.setWindowIcon(QtGui.QIcon('Photo/log.png'))
        self.centralwidget = QtWidgets.QWidget(tambahan)
        self.centralwidget.setObjectName("centralwidget")
        self.logosfx = QtWidgets.QLabel(self.centralwidget)
        self.logosfx.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.logosfx.setText("")
        self.logosfx.setPixmap(QtGui.QPixmap("Photo/log.png"))
        self.logosfx.setScaledContents(True)
        self.logosfx.setObjectName("logosfx")
        self.framed = QtWidgets.QFrame(self.centralwidget)
        self.framed.setGeometry(QtCore.QRect(50, 110, 891, 341))
        self.framed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framed.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.framed.setLineWidth(30)
        self.framed.setMidLineWidth(0)
        self.framed.setObjectName("framed")


        self.textJudulBaru = QtWidgets.QTextEdit(self.framed)
        self.textJudulBaru.setGeometry(QtCore.QRect(240, 20, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(18)
        self.textJudulBaru.setFont(font)
        self.textJudulBaru.setObjectName("textJudulBaru")


        self.labelKata = QtWidgets.QLabel(self.framed)
        self.labelKata.setGeometry(QtCore.QRect(30, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelKata.setFont(font)
        self.labelKata.setMouseTracking(False)
        self.labelKata.setAutoFillBackground(False)
        self.labelKata.setLineWidth(1)
        self.labelKata.setScaledContents(False)
        self.labelKata.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelKata.setWordWrap(True)
        self.labelKata.setObjectName("labelKata")
        self.labelPenjelasan = QtWidgets.QLabel(self.framed)
        self.labelPenjelasan.setGeometry(QtCore.QRect(30, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelPenjelasan.setFont(font)
        self.labelPenjelasan.setMouseTracking(False)
        self.labelPenjelasan.setAutoFillBackground(False)
        self.labelPenjelasan.setLineWidth(1)
        self.labelPenjelasan.setScaledContents(False)
        self.labelPenjelasan.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelPenjelasan.setWordWrap(True)
        self.labelPenjelasan.setObjectName("labelPenjelasan")


        self.textPenjelasanBaru = QtWidgets.QTextEdit(self.framed)
        self.textPenjelasanBaru.setGeometry(QtCore.QRect(240, 90, 611, 111))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(18)
        self.textPenjelasanBaru.setFont(font)
        self.textPenjelasanBaru.setObjectName("textPenjelasanBaru")


        self.tombolOpen = QtWidgets.QPushButton(self.framed)
        self.tombolOpen.setGeometry(QtCore.QRect(330, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.tombolOpen.setFont(font)
        self.tombolOpen.setObjectName("tombolOpen")
        self.tombolOpen.clicked.connect(self.open_file)

        self.tombolTambah = QtWidgets.QPushButton(self.framed)
        self.tombolTambah.setGeometry(QtCore.QRect(480, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.tombolTambah.setFont(font)
        self.tombolTambah.setObjectName("tombolTambah")
        self.tombolTambah.clicked.connect(self.addKata)
        self.labelvid = QtWidgets.QLabel(self.framed)
        self.labelvid.setGeometry(QtCore.QRect(30, 210, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelvid.setFont(font)
        self.labelvid.setMouseTracking(False)
        self.labelvid.setAutoFillBackground(False)
        self.labelvid.setLineWidth(1)
        self.labelvid.setScaledContents(False)
        self.labelvid.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelvid.setWordWrap(True)
        self.labelvid.setObjectName("labelvid")
        self.labelPathVid = QtWidgets.QLabel(self.framed)
        self.labelPathVid.setGeometry(QtCore.QRect(240, 216, 611, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)

        self.labelPathVid.setFont(font)
        self.labelPathVid.setMouseTracking(False)
        self.labelPathVid.setAutoFillBackground(False)
        self.labelPathVid.setLineWidth(1)
        self.labelPathVid.setScaledContents(False)
        self.labelPathVid.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelPathVid.setWordWrap(True)
        self.labelPathVid.setObjectName("labelPathVid")

        self.homee = QtWidgets.QPushButton(self.centralwidget)
        self.homee.setGeometry(QtCore.QRect(870, 20, 70, 70))
        self.homee.setObjectName("homee")
        self.homee.setIcon(QIcon("Photo/boko.png"))
        self.homee.setIconSize(QtCore.QSize(72,72))
        self.homee.clicked.connect(self.jobno)

        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(100, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        tambahan.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tambahan)
        self.statusbar.setObjectName("statusbar")
        tambahan.setStatusBar(self.statusbar)

        self.retranslateUi(tambahan)
        QtCore.QMetaObject.connectSlotsByName(tambahan)

    def retranslateUi(self, tambahan):
        _translate = QtCore.QCoreApplication.translate
        tambahan.setWindowTitle(_translate("tambahan", "Sign Translate"))
        self.labelKata.setText(_translate("tambahan", "Kata            :"))
        self.labelPenjelasan.setText(_translate("tambahan", "Penjelasan    :"))
        self.tombolOpen.setText(_translate("tambahan", "Open File"))
        self.tombolTambah.setText(_translate("tambahan", "Tambah"))
        self.labelvid.setText(_translate("tambahan", "Video Animasi:"))
        self.labelPathVid.setText(_translate("tambahan", "-"))

        self.labelTitle.setText(_translate("tambahan", "Penambah Kata"))

    def open_file(self):
        global fileName
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            self.labelPathVid.setText(fileName)

    def addKata(self):
        judulBaru = self.textJudulBaru.toPlainText()
        judulBaru = judulBaru.lower()
        penjelasanBaru = self.textPenjelasanBaru.toPlainText()
        pathTujuan = "Vocabulary/"
        bentukVid=".avi"
        bentukTxt=".txt"
        print (judulBaru)
        print (penjelasanBaru)
        vidCopy = pathTujuan + judulBaru + bentukVid
        txtCopy = pathTujuan + judulBaru + bentukTxt
        shutil.copy(fileName,vidCopy)
        f= open(txtCopy,"w")
        f.write(penjelasanBaru)
        f.close()
        self.splash = QSplashScreen(QPixmap('Photo/as.png'))

        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(2000, self.splash.close)


        # if filename != '':
        #     self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        #     self.playBtn.setEnabled(True)
        #     print (filename)
        # return





if __name__ == "__main__":
    import sys
    global app
    app = QtWidgets.QApplication(sys.argv)
    splash = QSplashScreen(QPixmap('Photo/simpp.png'))
    # By default, SplashScreen will be in the center of the screen.
    # You can move it to a specific location if you want:
    # self.splash.move(10,10)
    splash.show()
    # Close SplashScreen after 2 seconds (2000 ms)
    QTimer.singleShot(1,splash.close)
    time.sleep(2)
    global bara
    def bara():
        global menuPencarian
        menuPencarian = QtWidgets.QMainWindow()
        ui = Ui_menuPencarian()
        ui.setupUi(menuPencarian)
        menuPencarian.show()
        global mandep
        sys.exit(app.exec_())  
        
    
    bara()
    # mandep()

    
