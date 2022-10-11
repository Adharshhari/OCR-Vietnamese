import cv2
import numpy as np
from glob import glob
import pandas as pd
from matplotlib import pyplot as plt

pic=glob('../input/arundemo/*.PNG')

img=cv2.imread(pic[0])

plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # optional line of code, just to hide tick values on X and Y axis if needed
plt.show()