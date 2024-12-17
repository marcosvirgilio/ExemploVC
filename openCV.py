
# Importação das bibliotecas
# cv2 = OpenCV
import cv2
# pathlib = Dialogo de seleção de imagem
import pathlib

from tkinter import filedialog as fd

def open_file_selection():
    filetypes = (
        ('Image files', '*.jpg;*.JPG'),
    )
    files = fd.askopenfilenames(
        filetypes=filetypes,
        initialdir='/'
    )
    return files

pathImage = open_file_selection()
print(pathImage)

# Leitura da imagem com a função imread()
imagem  = cv2.imread(pathImage[0])

print('Largura em pixels: ', end='')
print(imagem.shape[1])
#largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0])
#altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])