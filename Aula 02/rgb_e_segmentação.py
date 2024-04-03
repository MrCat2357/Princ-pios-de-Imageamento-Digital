# -*- coding: utf-8 -*-
"""RGB e Segmentação.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IwzDkzkBjGcsGL3Rk98nYhQWePdejC_A
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab.patches import cv2_imshow
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
# %matplotlib inline

img = cv2.imread("/content/wizard.jpg")

from google.colab import drive
drive.mount('/content/drive')

# Dividir a imagem em seus canais de cor
r, g, b = cv2.split(img)

"""Visualizando as imagens"""

#Original
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

#Red
cv2_imshow(r)

#Green
cv2_imshow(g)

#Blue
cv2_imshow(b)

"""EXIBINDO NAS ESCALAS ORIGINAIS DO RED, GREEN E BLUE"""

# Criar imagens coloridas para cada canal
blue_img = np.zeros_like(img)
blue_img[:,:,0] = b  # Atribui o canal azul ao canal azul da imagem

green_img = np.zeros_like(img)
green_img[:,:,1] = g  # Atribui o canal verde ao canal verde da imagem

red_img = np.zeros_like(img)
red_img[:,:,2] = r  # Atribui o canal vermelho ao canal vermelho da imagem

cv2_imshow(red_img)  # Canal Vermelho

cv2_imshow(green_img)  # Canal Verde

cv2_imshow(blue_img)  # Canal Azul

"""SEGMENTAÇÃO DA IMAGEM SELECIONADA

CONVERSÃO DA ESCALA RGB PARA HSV
"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab.patches import cv2_imshow
import cv2
import numpy as np
from PIL import Image
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

image = cv2.imread('/content/arroz.jpg')

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Exibir a imagem convertida para HSV
cv2_imshow(image_hsv)

cv2.waitKey(0)

cv2.destroyAllWindows()

"""SEGMENTAÇÃO PELA ESCALA DE CINZA"""

import cv2
from google.colab.patches import cv2_imshow

# Carregar a imagem
image = cv2.imread('/content/arroz.jpg')

# Converter a imagem para tons de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar a limiarização (thresholding)
_,binary_image = cv2.threshold(gray_image, 90, 255, cv2.THRESH_BINARY)

# Exibir a imagem original e a imagem binarizada
cv2_imshow(image)
cv2_imshow(binary_image)

# Dividir a imagem em seus canais de cor
r, g, b = cv2.split(image)

#Red
cv2_imshow(r)

#Green
cv2_imshow(g)

#Blues
cv2_imshow(b)

"""MUDANDO AS CORES DA SEGMENTAÇÃO"""

limite = 100 # Escolher algum valor entre 0 e 255
# Aplicar a limiarização
_, mask_orange = cv2.threshold(gray_image, limite, 255, cv2.THRESH_BINARY)
mask_purple = cv2.bitwise_not(mask_orange)  # Inverter a máscara para obter a máscara roxa

# Definir as cores laranja e roxa
cor_laranja = (0, 165, 255)  # (B, G, R)
cor_roxa = (128, 0, 128)  # (B, G, R)

# Aplicar as cores à imagem original
image_colored = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
image_colored[mask_orange > 0] = cor_laranja
image_colored[mask_purple > 0] = cor_roxa

# Exibir a imagem colorida
cv2_imshow(image_colored)