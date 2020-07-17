# coding=utf-8
from picture import ImagProgress
# 该函数是判断面前障碍物的三个颜色，返回矩形的【x，y，w，h】

def judge(filename2):
    flag3 = ImagProgress(filename2, 3)[2] * ImagProgress(filename2, 3)[3]
    flag1 = ImagProgress(filename2, 1)[2] * ImagProgress(filename2, 1)[3]
    flag2 = ImagProgress(filename2, 2)[2] * ImagProgress(filename2, 2)[3]
    if max(flag1, flag2, flag3) == flag1:
        print 'blue'
        return ImagProgress(filename2, 1)
    elif max(flag1, flag2, flag3) == flag2:
        print 'yellow'
        return ImagProgress(filename2, 2)
    else:
        print 'red'
        return ImagProgress(filename2, 3)
