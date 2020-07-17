# coding=utf-8
from naoqi import ALProxy


def main(robotIP, PORT):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    lists = motionProxy.getSensorNames()
    for single_list in lists:
        print single_list


if __name__ == "__main__":
    print('调试状态')
