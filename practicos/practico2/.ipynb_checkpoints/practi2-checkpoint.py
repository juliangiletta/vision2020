{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Practico 2 - Vision 2020\n",
    "### Escribir un programa en python que lea una imagen y realice un umbralizado binario, guardando el resultado en otra imagen.\n",
    "* NOTA: No usar ninguna función de las OpenCV, excepto para leer y guardar la imagen."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Leemos la imagen y obtenemos el tamaño"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = cv2.imread ('hojas.png', 0)\n",
    "nf, nc = img.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Recorremos la imagen como si fuera una matriz, al estar en escala de grises va a ser 2D. Si fuera RGB serian 3D."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range (1, nf):\n",
    "\tfor j in range (nc):\n",
    "\t\tif img[i][j] < 200: # 200 es el umbral para mandar a 0 un pixel.\n",
    "\t\t\timg[i][j]=0\n",
    "\t\telse:\n",
    "\t\t\timg[i][j]=255"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Guarda y muestra la imagen"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imwrite('resultado1.png', img)\n",
    "cv2.imshow('image',img)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.17"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
