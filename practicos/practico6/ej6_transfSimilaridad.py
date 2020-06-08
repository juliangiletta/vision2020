import numpy as np
import cv2

drawing = False # true if mouse is pressed
ix, iy = -1, -1
fx, fy = -1, -1

def transf_similaridad(image, tx, ty, angle_grad, h, w, s):
    
    angle_rad = angle_grad * np.pi/180 
    
    M = np.float32([[s*np.cos(angle_rad), s*np.sin(angle_rad), tx],
                    [-s*np.sin(angle_rad), s*np.cos(angle_rad), ty]])
                     
    tran_euc = cv2.warpAffine(image, M, (w, h))
    return tran_euc

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

img = cv2.imread('hoja.png', 1)
cv2.namedWindow('image')
cv2.setMouseCallback('image', crop_rectangle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.destroyWindow("image")
        img_rec = img[iy:fy, ix:fx]
        angle = int(input('Ingrese el angulo de rotacion expresado en grados sexagesimal: '))
        tx = int(input('Ingrese la traslacion en x: '))
        ty = int(input('Ingrese la traslacion en y: '))
        s = int(input('Ingrese el factor de escala: '))
        (h, w) = (int(s*img_rec.shape[0]), int(s*img_rec.shape[1]))
        new_img = transf_similaridad(img_rec, tx, ty, angle, h, w, s)
        cv2.imwrite('resultado1.png', new_img)
        cv2.imshow('Resultado', new_img)
        break
    elif k == ord('q'):
        break


cv2.waitKey(0)      
cv2.destroyAllWindows()