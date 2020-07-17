# coding=utf-8
from naoqi import ALProxy
from cmath import pi


# 该函数使机器人绕过障碍物并回到中心轴上，回到中心轴部分未实现


def move(distanceX, flag, ID, PORT=9559):
    distanceTofoot = 0
    motionProxy = ALProxy('ALMotion', ID, PORT)
    postureProxy = ALProxy('ALRobotPosture', ID, PORT)
    motionProxy.wakeUp()
    postureProxy.goToPosture('StandInit', 0.5)
    if distanceX > 50:
        motionProxy.moveTo(distanceX - 50, 0, 0)
        motionProxy.sleep(2)
    while distanceTofoot <= distanceX:
        X = 0.04
        legNamel = ["LLeg"]
        legNamer = ["RLeg"]
        distanceTofoot += X
        print distanceTofoot  # 
        Y = 0.1
        Theta = 0.1 * int(flag)
        footSteps = [[X, Y, Theta]]
        fractionMaxSpeed = [0.4]
        clearExisting = False
        motionProxy.setFootStepsWithSpeed(legNamel, footSteps, fractionMaxSpeed, clearExisting)
        motionProxy.setFootStepsWithSpeed(legNamer, footSteps, fractionMaxSpeed, clearExisting)
        # footSteps = [[X, Y, -Theta]]
        # motionProxy.setFootStepsWithSpeed(legNamel, footSteps, fractionMaxSpeed, clearExisting)
        # motionProxy.setFootStepsWithSpeed(legNamer, footSteps, fractionMaxSpeed, clearExisting)
        motionProxy.moveTo(distanceX, 20 * flag, -pi / 2)  # 测试使用moveTo函数来代替设置双脚函数
    # motionProxy.waitUntilMoveIsFinished()
    motionProxy.move(0, 0, 0)  # motionProxy.sleep(3)
    postureProxy.rest()


if __name__ == "__main__":
    IP = input("输入IP")
    IP = str(IP)
    move(30, 1, IP)
    move(30, -1, IP)
