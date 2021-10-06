from cv2 import cv2
import  numpy as np
import math
import matplotlib.pyplot as plt

flower = cv2.imread("ayu.png")
flower = cv2.resize(flower, (800,600))
s = flower.shape

flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.10, beta=-20)


def Hist(image):
    H=np.zeros(shape=(256, 1))
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            k=image[i,j]
            H[k, 0]=H[k,0]+1
            return H

        histg = Hist(flowerGray)
        plt.plot(histg)
        x =  histg.reshape(1,256)
        y = np.array([])
        y = np.append(y,x[0,0])

        for i in range(255):
            k = x[0, i+1]+y[i]
            y = np.append(y,k)
        y = np.round((y/(s[0]*s[1]))*(255-1))

        for i in range(s[0]):
            for j in range(s[1]):
                k = flowerGray[i,j]
                flowerGray[i,j] = y[k]
        equal = Hist(flowerGray)
        plt.plot(equal)
        plt.show(0)
        cv2.imshow('myequalize', flowerGray)
        cv2.waitKey()