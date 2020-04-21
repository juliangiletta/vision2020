
# coding: utf-8

# # Practico 4 - Manipulación de imágenes
# 
# Escribir un programa que permita seleccionar un rectángulo de una imagen, luego:
# 
# * con la letra “g” guarda la imagen dentro del rectángulo en el disco,
# * con la letra “r” restaura la imagen original y permite realizar nuevamente la selección,
# * con la “q” finaliza.

# In[59]:


import cv2
import numpy as np


# In[60]:


drawing = False # true if mouse is pressed
ix, iy = -1, -1
fx, fx = -1, -1


# In[61]:


def crop_rectangle(event, x, y, flags, param):
    global ix, iy, fx, fy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:            
            fx, fy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (fx, fy), (0, 255, 0) , 1)


# In[62]:


img = cv2.imread('../practico2/hojas.png', 1)
aux_img = img.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', crop_rectangle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        crop_img = img[iy:fy, ix:fx]
        cv2.imwrite('recorte.png', crop_img)
        break
    elif k == ord('r'):
        img = aux_img.copy()
    elif k == ord('q'):
        break
cv2.destroyAllWindows()

