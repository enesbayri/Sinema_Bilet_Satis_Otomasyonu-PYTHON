from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox,QLabel
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QIcon
from data import filmler
from koltukGoruntulemeEkrani import koltukEkrani


class filmgoruntule(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Filmler")
        self.setFixedSize(1600,800)
        self.filmListesiUIOlustur()
    
    def filmListesiUIOlustur(self):
        grid=QGridLayout()
        for index, film in enumerate(filmler):
            resimYolu=film.resimYolu
            buton=QPushButton()
            buton.setIcon(QIcon(f"FilmAfisleri/{resimYolu}"))
            buton.setIconSize(QSize(300,300))
            buton.setFixedSize(QSize(300,300))
            buton.setStyleSheet("background-color:black;")
            buton.clicked.connect(self.filmTiklandi(film))

            row,col=divmod(index,3)
            grid.addWidget(buton,row,col)

        self.setLayout(grid)
    
    def filmTiklandi(self,film):
        def filmtiklandiCagrisi():
            self.koltuklar=koltukEkrani(film)
            self.koltuklar.show()
            
        return filmtiklandiCagrisi


