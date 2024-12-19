
# Importação das bibliotecas
# cv2 = OpenCV
import cv2
import numpy as np
import mahotas
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
print(pathImage[0])

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

# Mostra a imagem com a função imshow
#cv2.imshow("Imagem", imagem)
#cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
#cv2.imwrite(pathImage[0], imagem)

#binarização
img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0)
# aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
resultado = np.vstack([np.hstack([suave, bin])])
cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)

#detecção de elementos
#Passo 1: Conversão para tons de cinza
imgCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#Passo 2: Blur/Suavização da imagem
imgSuave = cv2.blur(imgCinza, (7, 7))
#Passo 3: Binarização resultando em pixels brancos e pretos
limites = mahotas.thresholding.otsu(imgSuave)
bin = imgSuave.copy()
bin[bin > limites] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin)
#Passo 4: Detecção de bordas com Canny
bordas = cv2.Canny(bin, 70, 150)
#Passo 5: Identificação e contagem dos contornos da imagem
#cv2.RETR_EXTERNAL = conta apenas os contornos externos
(lx, objetos) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#A variável lx (lixo) recebe dados que não são utilizados
cv2.imshow("Bordas",bordas)
cv2.waitKey(0)