# coding=utf-8
import almath
import vision_definitions
from naoqi import ALProxy
from distance import getangle
from distance import getdistance
from move import move
from judge import judge
import cv2 as cv
import numpy as np
from image import getImag


def main(RobotID, PORT=9559):
    motionProxy = ALProxy('ALMotion', RobotID, PORT)
    postureProxy = ALProxy('ALRobotPosture', RobotID, PORT)
    flag = 1
    while True:  # not flag and flag2 != 3:
        img = getImag(RobotID, PORT, 0)
        # -------------------------------调整角度对准中心点-------------------------------------------------
        rotation1 = motionProxy.getAngles('HeadYaw', True)
        rotation2 = motionProxy.getAngles('HeadPitch', True)
        anglelist = getangle(judge(img), rotation1, rotation2)
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
        theta = motionProxy.getAngles('HeadPitch') * almath.TO_RAD
        # -----------------------------------------获取距离-------------------------------------------------
        distanceX = getdistance(theta)
        print distanceX
        # 返回距离值
        cv.imshow("src", img)
        # -------------------------------------------------------------------------------------------
        print distanceX  # 调试使用
        move(distanceX, flag, RobotID, PORT)
        # flag = - flag
        # result = motionProxy.getRobotVelocity()
        # if result[0] == 0 and result[1] == 0 and result[2] == 0:
        #     judgement = True
        # else:
        #     judgement = False
        cv.waitKey(1)
        # return img


if __name__ == "__main__":
    IP = input("输入IP")
    IP = str(IP)
    main(IP)
