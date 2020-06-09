import cv2
import numpy as np

#Coordenadas para la trasnformacion afin

points1 = [[-1, -1], [-1, -1], [-1, -1]] 
points2 = [[-1, -1], [-1, -1], [-1, -1]]
i = 0

# selecciona puntos en la imagen

def selec_points(event, x, y, flags, param):
    global points2, draw, i
    
    
    if event == cv2.EVENT_LBUTTONUP:
        if i == 0 :
            points2[0] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = i + 1
        elif i == 1 :
            points2[1] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = i + 1
        elif i == 2 :
            points2[2] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = 0

#ejecuta la transformacion

def Trans_affin(image):
    h, w = image.shape[:2]
    pts1 = np.float32([[0,0], [w, 0], [w,h]])
    pts2 = np.float32([[points2[0]], [points2[1]], [points2[2]]])
    M = cv2.getAffineTransform(pts1, pts2)
    final = cv2.warpAffine(image, M, (w,h))
    return final

img1 = cv2.imread('persona.jpg', 1)
img2 = cv2.imread('barbijo.png', 1)

# extraigo dimensiones de imagen 1 y redimensiono 2 para poder hacer la mascara despues de transformada
(h, w) = img1.shape[:2]
img2 = cv2.resize(img2, (w, h))


img1_aux = img1.copy() #imagen auxiliar para que los puntos dibujados cuando clickeo no formen parte de la imagen final
cv2.namedWindow('Persona')
cv2.imshow('Persona', img1_aux)
cv2.setMouseCallback('Persona', selec_points)

while(1):
    cv2.imshow('Persona', img1_aux)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('a'):       
        img_transf = Trans_affin(img2)
        
        #hago una mascara para poder poner la segunda imagen 
        
        mask = img_transf.copy()
        mask[mask != 0] = 255
        mask = cv2.bitwise_not(mask)
        mask = cv2.bitwise_and(mask, img1)
        
        final = cv2.bitwise_or(mask, img_transf)
        cv2.imwrite('Resultado.jpg', final)
        cv2.namedWindow('Resultado')
        cv2.imshow('Resultado', final)       
    elif k == ord('q'):
        break

cv2.waitKey(0)      
cv2.destroyAllWindows()