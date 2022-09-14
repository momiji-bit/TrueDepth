import oak_Cam
import depthai as dai
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

global img, D
global point1, point2
global average


def on_mouse(event, x, y, flag, param):
    global img, point1, point2, average
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and (flag & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img2, point1, (x, y), (0, 255, 0), 1)
        cv2.waitKey(1)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 2)
        img3 = img[point1[1]:point2[1], point1[0]:point2[0]]
        if len(img3)>0:
            cv2.imshow('out', img3)
            slice = D[point1[1]:point2[1], point1[0]:point2[0]]
            slice = slice.flatten()
            plt.hist(np.array(slice), bins=1000, range=(0,10000))
            plt.show()
    cv2.imshow('Demo', img2)


if __name__ == '__main__':
    oakCam = oak_Cam.OakCam(lrcheck=True, extended=True, subpixel=False,
                            median=dai.StereoDepthProperties.MedianFilter.KERNEL_3x3)
    camMsg = oakCam.get_msg()
    cv2.namedWindow('Demo')
    RGB, D, IMU = next(camMsg)

    while True:
        RGB, D, IMU = next(camMsg)
        # slice = D
        # slice = slice.flatten()
        # plt.hist(np.array(slice), bins=1000, range=(0, 10000))
        # # cv2.setMouseCallback('Demo', on_mouse)
        # plt.show()
        cv2.imshow('Demo', RGB)
        cv2.waitKey(1)




