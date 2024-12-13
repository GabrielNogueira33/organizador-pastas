import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow): # Meu construtor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha primeira GUI") # Aqui eu posso decidir o título da janela
        self.setGeometry(700, 300, 500, 500) # Esses números são respectivamente x, y, width, height e eles servem para decidir onde minha tela vai aparecer primeiro e suas medidas
        self.setWindowIcon(QIcon()) # Só deixar a imagem dentro do parenteses de QIcon para mudar o ícone

        label = QLabel("Hello world", self)
        label.setFont(QFont("Arial", 25))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color:purple;"
                            "background-color:black") # Usando o stylesheet dá pra editar que nem no css
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter ) # Alinhando horizontalmente e verticalmente no centro

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()