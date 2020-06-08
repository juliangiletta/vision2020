import numpy as np
import cv2

drawing = False # true if mouse is pressed
ix, iy = -1, -1
fx, fx = -1, -1

def transf_euclidiana(image, tx, ty, angle_grad, h, w):
   
    angle_rad = angle_grad * np.pi/180 
    
    M = np.float32([[np.cos(angle_rad), np.sin(angle_rad), tx],
                    [-np.sin(angle_rad), np.cos(angle_rad), ty]]20)
                 
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
    if k == ord('e'):
        cv2.destroyWindow("image")
        img_rec = img[iy:fy, ix:fx]

        (h, w) = (img_rec.shape[0], img_rec.shape[1])
        angle = int(input('Ingrese el angulo de rotacion expresado en grados sexagesimal: '))
        tx = int(input('Ingrese la traslacion en x: '))
        ty = int(input('Ingrese la traslacion en y: '))
        new_img = transf_euclidiana(img_rec, tx, ty, angle, h, w)
        cv2.imwrite('resultado1.png', new_img)
        cv2.destroyWindow("image")
        break
    elif k == ord('q'):
        break


cv2.imshow('Resultado', new_img)
cv2.waitKey(0)      
cv2.destroyAllWindows()