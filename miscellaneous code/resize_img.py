from configparser import Interpolation
import cv2 as cv
import numpy as np
import os
folderpath = "./rps images"
mylist = os.listdir(folderpath)
images = []
for img in mylist:
    actual_path_img = cv.imread(f'{folderpath}/{img}')
    images.append(actual_path_img)
for img1 in images:
    print(img1.shape)
i = 0
for img2 in images:
    finalimg = cv.resize(img2, (200, 200), interpolation=cv.INTER_AREA)
    # now we upload the resized images and manually delete the old pics.
    cv.imwrite(folderpath, finalimg)
    cv.waitKey(0)
