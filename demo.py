# encoding: utf-8
import cv2 as cv
import math
import numpy as np
import random

from distance import getdistance, getangle
from judge import judge
from naoqi import ALProxy
import vision_definitions
import time
import argparse
import motion
import almath

PORT = 9559


def main(IP, PORT, cameraID):  # cameraID是摄像头序号，有0,1表示上下两个摄像头
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
    postureProxy = ALProxy('ALRobotPosture', IP, PORT)
    motionProxy.wakeUp()
    postureProxy.goToPosture('StandInit', 0.5)
    resolution = vision_definitions.kQVGA
    colorSpace = vision_definitions.kBGRColorSpace
    fps = 20
    name = random.randint(0, 151)
    name = str(name)
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

        cv.imshow("src", img)
        rotation1 = motionProxy.getAngles('HeadYaw', True)
        rotation2 = motionProxy.getAngles('HeadPitch', True)
        anglelist = getangle(judge(img), rotation1, rotation2)
        print anglelist[0]
        print anglelist[1]
        motionProxy.setStiffnesses("Head", 1.0)
        names = "HeadYaw"
        angleLists = anglelist[0] * almath.TO_RAD
        timeLists = 1.0
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, timeLists, isAbsolute)
        names1 = "HeadPitch"
        angleLists1 = anglelist[1] * almath.TO_RAD
        timeLists1 = 1.0
        isAbsolute1 = True
        motionProxy.angleInterpolation(names1, angleLists1, timeLists1, isAbsolute1)
        time.sleep(1.0)
        theta = str(motionProxy.getAngles('HeadPitch', True))
        theta = theta[1:5]
        theta = float(theta)
        theta = theta * almath.TO_RAD
        print theta
        distanceX = getdistance(theta)
        time.sleep(4.0)
        print distanceX
        # 返回距离值

        # -------------------------------------------------------------------------------------------

        cv.waitKey(1)
        motionProxy.setStiffnesses("Head", 0.0)

        # return img


if __name__ == "__main__":
    IP = input("输入IP")
    IP = str(IP)
    main(IP, PORT, 0)  # 摄像头序号为1，调用底部相机
