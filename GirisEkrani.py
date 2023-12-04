from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox,QLabel
from PyQt5.QtCore import QSize,Qt
from filmGoruntulemeEkrani import filmgoruntule


name=""      #"enesbayri1"
password=""  #"cinemax1"

class Girisekrani(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bilet Satis")
        self.setFixedSize(400,150)

        vbox=QVBoxLayout()

        #kullanici adi----------------------------------
        hboxKullaniciAdi= QHBoxLayout()
        self.kullaniciAdiLineEdit=QLineEdit()
        self.kullaniciAdiLineEdit.setFixedSize(QSize(200,20))
        self.kullaniciAdiLabel=QLabel("Kullanici Adi: ")

        hboxKullaniciAdi.addWidget(self.kullaniciAdiLabel)
        hboxKullaniciAdi.addWidget(self.kullaniciAdiLineEdit)

        vbox.addLayout(hboxKullaniciAdi)

        #sifre------------------------------------------
        hboxSifre=QHBoxLayout()

        self.sifreLineEdit=QLineEdit()
        self.sifreLineEdit.setFixedSize(QSize(200,20))
        self.sifreLineEdit.setEchoMode(QLineEdit.Password)
        self.sifreLabel=QLabel("Sifre: ")
        
        hboxSifre.addWidget(self.sifreLabel)
        hboxSifre.addWidget(self.sifreLineEdit)

        vbox.addLayout(hboxSifre)

        #buton----------------------------------------
        self.buton=QPushButton()
        self.buton.setText("Giris Yap")
        self.buton.setFixedSize(QSize(100,30))
        self.buton.clicked.connect(self.GirisYap)
        
        vbox.addWidget(self.buton,alignment= Qt.AlignmentFlag.AlignCenter)

        
        
        self.setLayout(vbox)

    def GirisYap(self):
        if self.kullaniciAdiLineEdit.text()==name and self.sifreLineEdit.text()==password:
            self.filmlerigor=filmgoruntule()
            self.filmlerigor.show()
            self.close()
            
        else:
            QMessageBox.warning(self,"HATA","Kullanici bilgileri hatali!")

