import cv2
import numpy as np

points1 = [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]
i = 0

def selec_points(event, x, y, flags, param):
    global points1, draw, i
    
    
    if event == cv2.EVENT_LBUTTONUP:
        if i == 0 :
            points1[0] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = i + 1
        elif i == 1 :
            points1[1] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = i + 1
        elif i == 2 :
            points1[2] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = i + 1
        elif i == 3 :
            points1[3] = x, y
            cv2.circle(img1_aux, (x, y), 5, (0, 255, 0) , -1)
            i = 4

def Trans_perspectiva(image, img1):
    h, w = image.shape[:2]
    pts1 = np.float32([[points1[0]], [points1[1]], [points1[2]], [points1[3]]])
    pts2 = np.float32([[0,0], [w, 0], [w,h], [0, h]])
    print(pts1)
    M = cv2.getPerspectiveTransform(pts1, pts2)
    final = cv2.warpPerspective(img1, M, (w,h))
    return final

img1 = cv2.imread('cartel_perspectiva.jpg', 1)
img2 = np.zeros((415, 766, 3), np.uint8)


img1_aux = img1.copy()
cv2.namedWindow('Cartel en ruta')
cv2.imshow('Cartel en ruta', img1_aux)

while(1):
    cv2.imshow('Cartel en ruta', img1_aux)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('h'):       
        cv2.setMouseCallback('Cartel en ruta', selec_points) 
    elif i == 4:
        img_transf = Trans_perspectiva(img2, img1)
        cv2.imwrite('Resultado.jpg', img_transf)
        cv2.namedWindow('Resultado')
        cv2.imshow('Resultado', img_transf) 
        i = 0
    elif k == ord('q'):
        break

cv2.waitKey(0)      
cv2.destroyAllWindows()