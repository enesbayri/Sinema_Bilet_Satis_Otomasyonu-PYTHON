import sys
from PyQt5.QtWidgets import QApplication
from GirisEkrani import Girisekrani



app=QApplication(sys.argv)
girisEkrani=Girisekrani()
girisEkrani.show()





sys.exit(app.exec_())