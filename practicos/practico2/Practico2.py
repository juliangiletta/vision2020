
# coding: utf-8

# # Practico 2 - Vision 2020
# ### Escribir un programa en python que lea una imagen y realice un umbralizado binario, guardando el resultado en otra imagen.
# * NOTA: No usar ninguna función de las OpenCV, excepto para leer y guardar la imagen.

# In[1]:


import cv2


# Leemos la imagen y obtenemos el tamaño

# In[2]:


img = cv2.imread ('hojas.png', 0)
nf, nc = img.shape


# Recorremos la imagen como si fuera una matriz, al estar en escala de grises va a ser 2D. Si fuera RGB serian 3D.

# In[3]:


for i in range (1, nf):
	for j in range (nc):
		if img[i][j] < 200: # 200 es el umbral para mandar a 0 un pixel.
			img[i][j]=0
		else:
			img[i][j]=255


# Guarda y muestra la imagen

# In[ ]:


cv2.imwrite('resultado1.png', img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

