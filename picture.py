import cv2 as cv
import numpy as np


def ImagProgress(filename, flag):
    Image = filename
    # Image = cv.imread(filename)
    Image_Gau = cv.GaussianBlur(Image, (9, 9), 0)
    Image_HSV = cv.cvtColor(Image_Gau, cv.COLOR_BGR2HSV)
    if flag == 1:  # blue limitition
        lowarray = np.array([95, 43, 46])
        higharray = np.array([105, 255, 255])
    elif flag == 2:  # yellow limitition
        lowarray = np.array([26, 43, 46])
        higharray = np.array([34, 255, 255])
    else:  # red limitition
        lowarray = np.array([156, 43, 46])
        higharray = np.array([180, 255, 255])
    dst = cv.inRange(Image_HSV, lowarray, higharray)
    diale = cv.copyTo(dst, dst)
    element = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
    openImage = cv.morphologyEx(diale, cv.MORPH_OPEN, element)
    MedirImag = cv.medianBlur(dst, 9)
    x, y, w, h = cv.boundingRect(MedirImag)
    cv.rectangle(MedirImag, (x, y), (x + w, y + h), (255, 255, 255), 2)
    # cv.namedWindow('yuzhi', cv.WINDOW_NORMAL)
    # cv.namedWindow('zhongzhi', cv.WINDOW_NORMAL)
    cv.namedWindow('zhong', cv.WINDOW_NORMAL)
    # cv.imshow('yuzhi', dst)
    # cv.imshow('zhongzhi', MedirImag)
    cv.imshow('zhong', MedirImag)
    data = [x, y, w, h]
    # cv.waitKey(0)
    # return flag
    return data



