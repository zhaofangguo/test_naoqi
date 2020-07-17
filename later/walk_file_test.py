# -*- encoding: UTF-8 -*-

import math
import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Example showing the moveTo command
    # The units for this command are meters and radians
    distanceTofoot = 0
    distanceX = 100
    while distanceTofoot <= distanceX:
        legName = ["LLeg"]
        X = 0.04
        distanceTofoot += X
        print distanceTofoot  # 调试使用
        Y = 0.1
        Theta = 0.3 # 正值向左，负值向右
        footSteps = [[X, Y, Theta]]
        fractionMaxSpeed = [0.6]
        clearExisting = False
        motionProxy.setFootStepsWithSpeed(legName, footSteps, fractionMaxSpeed, clearExisting)
    # motionProxy.move(0, 0, 0)
    # distanceTofoot = 0
    # while distanceTofoot <= distanceX:
        legName = ["RLeg"]
        X = 0.04
        distanceTofoot += X
        Y = 0.1
        Theta = 0.3
        footSteps = [[X, Y, Theta]]
        fractionMaxSpeed = [0.6]
        clearExisting = False
        motionProxy.setFootStepsWithSpeed(legName, footSteps, fractionMaxSpeed, clearExisting)
    motionProxy.move(0, 0, 0)
    motionProxy.sleep(int(3))
    # Will block until move Task is finished

    ########
    # NOTE #
    ########
    # If moveTo() method does nothing on the robot,
    # read the section about walk protection in the
    # Locomotion control overview page.

    # Go to rest position
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.165.5",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)