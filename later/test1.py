# coding=utf-8
from naoqi import ALProxy
import motion

IP = raw_input()


def main(robotIP, PORT=9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    motionProxy.weakup()  # 开机？
    postureProxy.goToPosture('StandInit', 0.5)  # 初始化站姿？
    # 此处获得x,y,z的值
    while (True):
        name = "CameraTop"
        frame = motion.FRAME_WORLD
        useSensorValues = True
        result = motionProxy.getPosition(name,frame,useSensorValues)
        print(name + "is in world" + result)
        result1 = motionProxy.getPosition('')

        motionProxy.moveTo()
        motionProxy.rest()


if __name__ == "__main__":
    main(IP)
