import numpy as np
import cv2
import glob


def get_mean_pixels():
    B_pixel_value = 0
    G_pixel_value = 0
    R_pixel_value = 0

    print("Get train/holdout files.")
    src_dir = 'D:/competition/some_picture/'
    samples = glob.glob(src_dir+"*.png")
    num = len(samples)
    print('image quantity is: ', num)
    for item in samples:
        img = cv2.imread(item, cv2.IMREAD_ANYCOLOR)
        B_pixel_value += img[:, :, 0].mean()
        G_pixel_value += img[:, :, 1].mean()
        R_pixel_value += img[:, :, 2].mean()
    # print('pixel_value sum is:', pixel_value)
    print('B avg pixel value is:', B_pixel_value / num)
    print('G avg pixel value is:', G_pixel_value / num)
    print('R avg pixel value is:', R_pixel_value / num)


if __name__ == '__main__':
    get_mean_pixels()