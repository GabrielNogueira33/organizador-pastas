import pandas as pd
import shutil 
import os


logsArquivos = {
  'pastas': ["imagens", "videos", "jogos"],
  'arquivos': [9, 12, 20]
}

logs = pd.DataFrame(logsArquivos)

print(logs)

path = "/"
 
listarDiretorio = os.listdir(path)

print(listarDiretorio)

def moverArquivo():

    shutil.move('arquivo1.txt', 'testes/')

    print("1 arquivo foi movido")

def copiarArquivo():

    shutil.copy('arquivo1.txt', 'testes/')

    print("1 arquivo foi copiado")

def removerDiretorio():

    shutil.rmtree()