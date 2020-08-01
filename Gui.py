import sys
import urllib
from PyQt5.QtWidgets import QApplication, QWidget , QLineEdit , QPushButton , QHBoxLayout , QVBoxLayout , QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore 
from Down_func import Video_downloader
from multiprocessing import Process , Queue
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import pytube
from threading import Thread


class Pencere():
    def __init__(self):
        self.count = []
        app = QApplication(sys.argv)
        w = QWidget()
        w.move(500, 100)
        qss="style.qss"
        with open(qss,"r") as fh:
            w.setStyleSheet(fh.read())
        w.setMaximumSize(350 , 400)
        w.setMinimumSize(350 , 400)
        w.setWindowTitle('Youtube mp3 Downloader by Dark')
        self.link_line = QLineEdit(w)
        self.link_line.setPlaceholderText("link")
        self.link_line.setText("")
        self.link_line.textChanged.connect(self.basla)
        self.button = QPushButton(w)
        self.button.clicked.connect(self.down_basla)
        self.button.setText("Yüklə")
        self.resim_label = QLabel(w)
        self.pixmap = QPixmap('resim.png')
        self.resim_label.setPixmap(self.pixmap)
        self.label_copy = QLabel(w)
        self.label_copy.setText("DARK Copyright")
        self.label_copy.setAlignment(Qt.AlignCenter)
        self.basliq = QLabel(w)
        self.basliq.resize(300 , 10)
        self.basliq.setText("")
        self.button.setEnabled(False)
        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox2.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        hbox4 = QHBoxLayout()
        hbox4.setAlignment(Qt.AlignCenter)
        hbox4.addWidget(self.basliq)
        hbox.addWidget(self.link_line)
        hbox1.addWidget(self.button)
        hbox2.addWidget(self.resim_label)
        hbox3.addWidget(self.label_copy)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox3)
        w.setLayout(vbox)
        w.show()

        sys.exit(app.exec_())
    def deyis(self):
        try:
            self.a = Video_downloader(self.link_line.text())
            self.button.setEnabled(True)
            url , ad =  self.a.thumb()
            data = urllib.request.urlopen(url).read()
            self.pixmap.loadFromData(data)
            smaller_pixmap = self.pixmap.scaled(330, 285, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.resim_label.setPixmap(smaller_pixmap)
            self.basliq.setText(ad[0:-4])
            print(ad[0:-4])
            print("isledi")
        except pytube.exceptions.RegexMatchError:
            self.button.setEnabled(False) 
            self.basliq.setText("")
            self.pixmap = QPixmap('resim.png')
            self.resim_label.setPixmap(self.pixmap)
    def basla(self):
        p = Thread(target=self.deyis)
        p.start()
    def down_basla(self):
        p = Thread(target=self.download_video)
        p.start()

    def download_video(self):

        self.button.setEnabled(False)
        try:
            if self.link_line.text() in self.count:
                pass
            else:
                self.a.downloader()
                self.count.append(self.link_line.text())
        except:
            self.link_line.setPlaceholderText("Linkde yanlışlıq ola bilər yeniden yoxlayın")
        self.button.setEnabled(True)


if __name__ == '__main__':
    Pencere()
        
               

