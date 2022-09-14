import time

# from tools import *
from oak_Cam import *

# if __name__ == '__main__':
    # oakCam = OakCam(lrcheck=True, extended=True, subpixel=False,
    #                         median=dai.StereoDepthProperties.MedianFilter.KERNEL_3x3)
    # camMsg = oakCam.get_msg()
    # t0 = time.time()
    #
    # while True:
    #     RGB, D, IMU = next(camMsg)
    #     timestamp = time.time() - t0
    #
    #     RGBD = np.zeros((360, 640, 4))
    #     RGBD[:, :, :3] = RGB
    #     RGBD[:, :, 3] = D
    #     np.save(f'./out/{timestamp}-0-all', RGBD)
    #
    #     number = 1
    #     for bbox in track(RGB):  # bbox = [c, id, name, conf, xyxy, color]
    #         np.save(f'./out/{timestamp}-0-{number}-{bbox[2]}', RGBD[bbox[4][1]:bbox[4][3]+1, bbox[4][0]:bbox[4][2]]+1)
while True:
    t0 = time.time()
    RGBD = np.zeros((360, 640, 4))
    RGBD[:, :, 0] = RGBD[:, :, 3]
    RGBD[:, :, 1] = RGBD[:, :, 1]
    RGBD[:, :, 2] = RGBD[:, :, 0]
    RGBD[:, :, 3] = RGBD[:, :, 2]
    print(f'\rtime:{time.time() - t0:.10f}ms', end='')
