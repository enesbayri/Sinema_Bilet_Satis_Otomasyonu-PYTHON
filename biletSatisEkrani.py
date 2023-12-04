from PyQt5.QtWidgets import QWidget,QRadioButton,QPushButton,QGridLayout,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox,QLabel,QMenuBar,QAction,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon,QColor
from data import filmler
import json

class satisEkrani(QWidget):

    def __init__(self,film,secilenKoltuklar):
        super().__init__()
        self.film=film
        self.secilenKoltuklar=secilenKoltuklar

        self.lineEditliste=[]
        self.secilenKoltukSayisi=len(secilenKoltuklar)
        dinamikformuzunlugu=self.secilenKoltukSayisi*180
        self.toplamTutar=20.0*self.secilenKoltukSayisi

        self.setFixedSize(400,dinamikformuzunlugu)

        self.setWindowTitle(film.filmAdi)
        self.formOlustur()

    
    
    def formOlustur(self):
        layout=QVBoxLayout()
        
        for koltukNo in self.secilenKoltuklar:
            koltukNoLabel=QLabel()
            koltukNoLabel.setText(f"Koltuk No:  {koltukNo}")
            layout.addWidget(koltukNoLabel)
            
            hboxKullanicibilgisi=QHBoxLayout()
            isimSoyisimLabel=QLabel("Isim Soyisim: ")
            isimSoyisimLineEdit=QLineEdit()
            self.lineEditliste.append(isimSoyisimLineEdit)
            hboxKullanicibilgisi.addWidget(isimSoyisimLabel)
            hboxKullanicibilgisi.addWidget(isimSoyisimLineEdit)
            
            layout.addLayout(hboxKullanicibilgisi)

        hboxbiletbilgisi=QHBoxLayout()
        tamBiletRadioButon=QRadioButton("Tam Bilet")
        tamBiletRadioButon.setChecked(True)
        tamBiletRadioButon.toggled.connect(self.biletTuru)

        ogrenciBiletRadioButon=QRadioButton("Ogrenci Bilet")
        ogrenciBiletRadioButon.toggled.connect(self.biletTuru)
        hboxbiletbilgisi.addWidget(tamBiletRadioButon)
        hboxbiletbilgisi.addWidget(ogrenciBiletRadioButon)
        layout.addLayout(hboxbiletbilgisi)

        self.toplamTutarLabel=QLabel()
        self.toplamTutarLabel.setText(f"Toplam Tutar: {self.toplamTutar}")
        layout.addWidget(self.toplamTutarLabel)

        self.biletAlButon=QPushButton("Bilet Al")
        self.biletAlButon.clicked.connect(self.biletAlTiklandi)
        
        layout.addWidget(self.biletAlButon)
        
        
        self.setLayout(layout)

    def biletTuru(self):
        radiobuton=self.sender()
        if radiobuton.isChecked() and radiobuton.text()=="Ogrenci Bilet":
            self.toplamTutar=15.0*self.secilenKoltukSayisi
            
        elif radiobuton.isChecked() and radiobuton.text()=="Tam Bilet":
            self.toplamTutar=20.0*self.secilenKoltukSayisi
        
        self.toplamTutarLabel.setText(f"Toplam Tutar: {self.toplamTutar}")

    def biletAlTiklandi(self):
        for lineEdit in self.lineEditliste:
            
            if len(lineEdit.text())==0:
                QMessageBox.warning(self,"HATA!","Eksik bilgiler mevcut")
                return
        kullaniciCevabi=QMessageBox.question(self,"Bilet Satis",f"Toplam Tutar: {self.toplamTutar}. Bilet alimini onayliyor musunuz?",QMessageBox.Yes | QMessageBox.No)
        if kullaniciCevabi==QMessageBox.Yes:
            self.biletAl()

    def biletAl(self):
        dosya=open("data.json","r")
        veri=json.load(dosya)
        dosya.close()

        for index,lineEdit in enumerate(self.lineEditliste):
            secilenkoltukno=self.secilenKoltuklar[index]
            veri[f"{self.film.filmAdi}"]["koltukBilgileri"][secilenkoltukno-1]["koltukDurumu"]=1
            veri[f"{self.film.filmAdi}"]["koltukBilgileri"][secilenkoltukno-1]["alanKisi"]=lineEdit.text()
            veri[f"{self.film.filmAdi}"]["koltukBilgileri"][secilenkoltukno-1]["tutar"]=self.toplamTutar/self.secilenKoltukSayisi
        
            id=self.film.id
            filmler[id-1].koltukBilgileri[secilenkoltukno-1].koltukDurum=1
            filmler[id-1].koltukBilgileri[secilenkoltukno-1].alanKisi=lineEdit.text()
            filmler[id-1].koltukBilgileri[secilenkoltukno-1].tutar=self.toplamTutar/self.secilenKoltukSayisi

        
        dosya=open("data.json","w+")
        dosya.write(json.dumps(veri,indent=4))
        dosya.close()

        QMessageBox.information(self,"Basarili","Bilet basariyla alindi!")
        self.close()
