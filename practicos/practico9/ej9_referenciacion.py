import cv2
import numpy as np

points1 = [[85, 167], [402, 219], [394, 527], [41, 506]]
i = 0


def Trans_perspectiva(image, img1):
    h, w = img1.shape[:2] 
    pts1 = np.float32([[points1[0]], [points1[1]], [points1[2]], [points1[3]]])
    print(pts1)
    pts2 = np.float32([[0,0], [350, 0], [350,350], [0, 350]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    final = cv2.warpPerspective(img1, M, (w,h))
    return final

img1 = cv2.imread('ej9_referenciacion.png', 1)
img2 = np.zeros((img1.shape[0], img1.shape[1], 3), np.uint8)


img1_aux = img1.copy()
img1_aux = cv2.putText( img1_aux , 'pulse para medir:', ( 0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
img1_aux = cv2.putText( img1_aux , '1-tarjeta; 2-goma; 3-moneda', ( 0, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)


while(1):

    cv2.imshow('Seleccionar que quiero medir', img1_aux)
    k = cv2.waitKey(0) & 0xFF
    img_transf = Trans_perspectiva(img2, img1)
    if k == ord('1'):
        #ancho... 195 pixeles = 5,57 cm
        img_transf = cv2.line(img_transf, (380,30), (575, 27), (255,0,0))
        img_transf = cv2.putText( img_transf , 'w=5,57cm', ( 410, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
        #alto... 300 pixeles = 8,57 cm
        img_transf = cv2.line(img_transf, (575,30), (575, 330), (255,0,0))
        img_transf = cv2.putText( img_transf , 'h=8,57cm', ( 425,165), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
        cv2.imwrite('Resultado.jpg', img_transf)
        cv2.namedWindow('Resultado')
        cv2.imshow('Resultado', img_transf) 

    if k == ord('2'):
        #ancho... 200 pixeles = 5,71 cm
        img_transf = cv2.line(img_transf, (64,413), (264,413), (255,0,0))
        img_transf = cv2.putText( img_transf , 'w=5,71cm', (100,413), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
        #alto... 67 pixeles = 1,91 cm
        img_transf = cv2.line(img_transf, (265,415), (265,482), (255,0,0))
        img_transf = cv2.putText( img_transf , 'h=1,91cm', (265,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
        cv2.imwrite('Resultado.jpg', img_transf)
        cv2.namedWindow('Resultado')
        cv2.imshow('Resultado', img_transf) 

    if k == ord('3'):
        #diametro moneda 1 peso... 80 pixeles = 2,286 cm
        img_transf = cv2.line(img_transf, (355,426), (355,466), (255,0,0))
        img_transf = cv2.putText( img_transf , 'r=1,14cm', (355,446), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
        #diametro moneda 50... 88 pixeles = 2,514 cm
        img_transf = cv2.line(img_transf, (447,378), (447,422), (255,0,0))
        img_transf = cv2.putText( img_transf , 'r=1,26cm', (447,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2 , cv2.LINE_AA)
        cv2.imwrite('Resultado.jpg', img_transf)
        cv2.namedWindow('Resultado')
        cv2.imshow('Resultado', img_transf) 
    elif k == ord('q'):
        break

cv2.waitKey(0)      
cv2.destroyAllWindows()


#puntos del cuadrado de glace [[[ 85. 169.]]  [[402. 219.]] [[396. 524.]] [[ 44. 504.]]]