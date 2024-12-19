
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
cv2.imshow("Imagem", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
#cv2.imwrite(pathImage[0], imagem)

#binarização
img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0)
# aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255,
cv2.THRESH_BINARY_INV)
resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])
cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)

#detecção de elementos
#Passo 1: Conversão para tons de cinza
imgCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
#Passo 2: Blur/Suavização da imagem
imgSuave = cv2.blur(imgCinza, (7, 7))
#Passo 3: Binarização resultando em pixels brancos e pretos
T = mahotas.thresholding.otsu(imgSuave)
bin = imgSuave.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin)
#Passo 4: Detecção de bordas com Canny
bordas = cv2.Canny(bin, 70, 150)
#Passo 5: Identificação e contagem dos contornos da imagem
#cv2.RETR_EXTERNAL = conta apenas os contornos externos
(lx, objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#A variável lx (lixo) recebe dados que não são utilizados
escreve(img, "Imagem em tons de cinza", 0)
escreve(suave, "Suavizacao com Blur", 0)
escreve(bin, "Binarizacao com Metodo Otsu", 255)
escreve(bordas, "Detector de bordas Canny", 255)
temp = np.vstack([
np.hstack([img, suave]),
np.hstack([bin, bordas])
])
cv2.imshow("Quantidade de objetos: "+str(len(objetos)), temp)
cv2.waitKey(0)
imgC2 = img.copy()
cv2.imshow("Imagem Original", img)
cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
escreve(imgC2, str(len(objetos))+" objetos encontrados!")
cv2.imshow("Resultado", imgC2)
cv2.waitKey(0)