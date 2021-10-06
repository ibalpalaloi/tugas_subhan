import numpy as np
import cv2

img = cv2.imread("ayu.png")

img_1 = 255 - img

cv2.imshow("Gambar Asli", img)
cv2.imshow("Gambar Transormasi Negatif", img_1)

cv2.waitKey()
cv2.destroyAllWindows()