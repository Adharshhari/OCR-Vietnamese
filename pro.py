import cv2
import numpy as np
from glob import glob
import pandas as pd
from matplotlib import pyplot as plt

pic=glob('../input/arundemo/*.PNG')

img=cv2.imread(pic[0])

plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) 
plt.show()


img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img, interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) 
plt.show()
text=pytesseract.image_to_string(img)
print(text)