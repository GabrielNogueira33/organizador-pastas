#import organizador #importe esse arquivo para o arquivo da interface gráfica se comunicar com o organizador
import sys 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

#Lembrando que o self é o this do python

class MainWindow(QMainWindow): # Meu construtor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha primeira GUI") # Aqui eu posso decidir o título da janela
        self.setGeometry(700, 300, 500, 500) # Esses números são respectivamente x, y, width, height e eles servem para decidir onde minha tela vai aparecer primeiro e suas medidas
        self.setWindowIcon(QIcon()) # Só deixar a imagem dentro do parenteses de QIcon para mudar o ícone
        self.initUI()    

    def initUI(self):
            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            self.label = QLabel("Hello world", self)
            self.label2 = QLabel("Este é meu aplicativo",self)

            self.button = QPushButton("clique aqui", self)
            self.button.clicked.connect(self.apertarBotao)

            self.button.setGeometry(150,200,200,100)
            self.button.setStyleSheet("font-size:22px")

            self.label.setFont(QFont("Arial", 25))
            self.label.setGeometry(0, 0, 500, 100)
            self.label.setStyleSheet("color:purple;"
                            "background-color:black") # Usando o stylesheet dá pra editar que nem no css
        
            self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter ) # Alinhando horizontalmente e verticalmente no centro

            self.label2.setStyleSheet("color:orangered;"
                            "background-color:gray") # Usando o stylesheet dá pra editar que nem no css
        
            self.label2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter ) # Alinhando horizontalmente e verticalmente no centro

            vbox = QVBoxLayout()

            vbox.addWidget(self.label)
            vbox.addWidget(self.label2)

            central_widget.setLayout(vbox)
    
    def apertarBotao(self):
        print("arquivos modificado com sucesso!")
        self.button.setText("Sucesso!")
        self.button.setDisabled(True)
        self.label.setText("Finalizado!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()