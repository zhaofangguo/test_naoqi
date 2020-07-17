import random

import cv2
import math
import numpy as np
from naoqi import ALProxy
import vision_definitions
import time
import argparse
import motion
import almath

IP = '169.254.165.5'
PORT = 9559


def getImag(IP, PORT, cameraID):
    try:
        camProxy = ALProxy("ALVideoDevice", IP, PORT)
    except Exception, e:
        print "Error in transfering ALVideoDevice"
        print str(e)
        exit(1)
    try:
        motionProxy = ALProxy("ALMotion", IP, PORT)
    except Exception, e:
        print "Error in transfering ALMotion"
        print str(e)
        exit(1)
    name = random.randint(0, 151)
    name = str(name)
    resolution = vision_definitions.kQVGA
    colorSpace = vision_definitions.kBGRColorSpace
    fps = 20
    nameID = camProxy.subscribe(name, resolution, colorSpace, fps)
    camProxy.setActiveCamera(cameraID)
    print "Is camera opened ?", camProxy.isCameraOpen(1)
    print "getting images in remote"
    while True:
        img = camProxy.getImageRemote(nameID)
        # cv2.SetData(img,imgData[6])
        ###
        imagHeader0 = np.array(img[6])
        imagHeader = map(ord, img[6])
        camProxy.releaseImage(nameID)
        imagHeader = np.reshape(imagHeader, [240, 320, 3])
        img = np.uint8(imagHeader)

        # cv2.imshow("src", img)
        return img


if __name__ == "__main__":
    getImag(IP, PORT, 1)
