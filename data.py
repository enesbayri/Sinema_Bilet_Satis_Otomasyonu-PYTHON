import json


class Koltuk:
    
    def __init__(self,no,durum,alan,tutar):
        self.koltukNo=no
        self.koltukDurum=durum
        self.alanKisi=alan
        self.tutar=tutar

class Film:
    def __init__(self,isim,resim,id,koltukbilgileri):
        self.filmAdi=isim
        self.resimYolu=resim
        self.id=id
        self.koltukBilgileri=koltukbilgileri

def veriyiAl():
    dosya=open("data.json")
    veri=json.load(dosya)
    filmListesi=[]

    for filmismi in veri.keys():
        film=veri[filmismi]
        koltukBilgileri=[Koltuk(koltuk["koltukNo"],koltuk["koltukDurumu"],koltuk["alanKisi"],koltuk["tutar"]) for koltuk in film["koltukBilgileri"]]
        filmListesi.append(Film(filmismi,film["image"],film["id"],koltukBilgileri))

    return filmListesi

filmler=veriyiAl()
