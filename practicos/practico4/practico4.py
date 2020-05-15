
# coding: utf-8

# # Practico 4 - Manipulación de imágenes
# 
# Escribir un programa que permita seleccionar un rectángulo de una imagen, luego:
# 
# * con la letra “g” guarda la imagen dentro del rectángulo en el disco,
# * con la letra “r” restaura la imagen original y permite realizar nuevamente la selección,
# * con la “q” finaliza.


import cv2
import numpy as np


drawing = False # true if mouse is pressed
ix, iy = -1, -1 #coordenadas de inicio
fx, fx = -1, -1 #coordenadas de fin



def crop_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing
	
    if event == cv2.EVENT_LBUTTONDOWN: #aprieto click y guardo coordenadas inicio
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE: 
        if drawing is True:            
            fx, fy = x, y
    elif event == cv2.EVENT_LBUTTONUP: #suelto click y guardo coordenadas fin
        drawing = False
        cv2.rectangle(img, (ix, iy), (fx, fy), (0, 255, 0) , 1)


img = cv2.imread('hoja.png', 1)
aux_img = img.copy() #Guardo copia para restauracion
cv2.namedWindow('image')
cv2.setMouseCallback('image', crop_rectangle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'): #Si aprieto g guardo imagen desde punto inicial a final
        crop_img = img[iy:fy, ix:fx]
        cv2.imwrite('recorte.png', crop_img)
        break
    elif k == ord('r'): # si aprieto k cargo la imagen guardada
        img = aux_img.copy()
    elif k == ord('q'): # si aprieto q termino el programa
        break
cv2.destroyAllWindows()
