import oak_Cam
import depthai
import cv2


if __name__ == '__main__':
    oakCam = oak_Cam.OakCam()
    camMsg = oakCam.get_msg()
    while True:
        RGB, D, IMU = next(camMsg)


