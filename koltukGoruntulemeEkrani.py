from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox,QLabel,QMenuBar,QAction,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon,QColor
from data import filmler
from biletSatisEkrani import satisEkrani


class koltukEkrani(QWidget):

    def __init__(self,film):
        super().__init__()

        self.film=film
        self.secilenKoltuklar=[]


        self.setWindowTitle("Koltuklar: "+film.filmAdi)
        self.setGeometry(300,200,1600,800)
        self.pencereGoruntusu()
        self.menuOlustur()
    
    def pencereGoruntusu(self):
        layout=QVBoxLayout()
        self.grid=QGridLayout()

        for koltuk in self.film.koltukBilgileri:
            koltukNo=koltuk.koltukNo
            koltukDurumu=koltuk.koltukDurum

            buton=QPushButton(f"{koltukNo}")
            buton.setFixedSize(QSize(160,80))
            buton.clicked.connect(self.biletSecCagrisi(koltukNo))

            if koltukDurumu:
                buton.setEnabled(False)
                buton.setStyleSheet("background-color: red; color:white;")
            else:
                buton.setEnabled(True)
                buton.setStyleSheet("background-color: green; color:white;")

            row,col=divmod(koltukNo-1,5)
            self.grid.addWidget(buton,row,col)
        
        self.biletAlButon=QPushButton("Bilet Al")
        self.biletAlButon.clicked.connect(self.biletAl)
        self.biletAlButon.setFixedSize(150,50)
        self.biletAlButon.setStyleSheet("background-color:gray;color:white")
        self.biletAlButon.setEnabled(False)


        layout.addLayout(self.grid)
        layout.addWidget(self.biletAlButon,alignment=Qt.AlignmentFlag.AlignCenter)



        self.setLayout(layout)


        
    
    def biletSecCagrisi(self,secilenkoltukNo):
        def biletSec():
            secilenkoltuk=self.grid.itemAt(secilenkoltukNo-1).widget()
            if secilenkoltukNo not in self.secilenKoltuklar:
                self.secilenKoltuklar.append(secilenkoltukNo)
                secilenkoltuk.setStyleSheet("background-color: yellow;color:white")
                if len(self.secilenKoltuklar)==1:
                    self.biletAlButon.setStyleSheet("background-color: green;color:white")
                    self.biletAlButon.setEnabled(True)
            else:
                self.secilenKoltuklar.remove(secilenkoltukNo)
                secilenkoltuk.setStyleSheet("background-color: green;color:white")
                if len(self.secilenKoltuklar)<1:
                    self.biletAlButon.setStyleSheet("background-color:gray;color:white")
                    self.biletAlButon.setEnabled(False)

        return biletSec




    def biletAl(self):
        self.close()
        self.biletsatisEkrani=satisEkrani(film=self.film,secilenKoltuklar=self.secilenKoltuklar)
        self.biletsatisEkrani.show()


    def menuOlustur(self):
        menubar=QMenuBar(self)
        detaymenu=menubar.addMenu("Detay")
        biletgoruntuleaction=QAction("Biletleri Goruntule",self)
        detaymenu.addAction(biletgoruntuleaction)
        biletgoruntuleaction.setShortcut("Ctrl+N")
        biletgoruntuleaction.triggered.connect(self.alinanBiletleriGoruntule)

    def alinanBiletleriGoruntule(self):
        self.window=QWidget()
        self.window.show()
        self.window.setWindowTitle("Alinan biletler")
        self.window.setGeometry(150,100,800,800)
        layoutt=QHBoxLayout()
        anaLayout=QVBoxLayout()
        for koltuk in self.film.koltukBilgileri:
            
            if koltuk.koltukDurum==1:
                alinanNo=QLabel(f"{koltuk.koltukNo} - ")
                alinanKoltuklar=QLabel(f"{koltuk.alanKisi} - ")
                alinanTutar=QLabel(f"{koltuk.tutar}")


                layoutt.addWidget(alinanNo)
                layoutt.addWidget(alinanKoltuklar)
                layoutt.addWidget(alinanTutar)

                anaLayout.addLayout(layoutt)
                
                
                

        self.window.setLayout(anaLayout)
        



            

