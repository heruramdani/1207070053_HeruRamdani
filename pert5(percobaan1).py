
import cv2
import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert

import numpy as np

#Percobaan 1
astronautImage = imread('aadc.jpeg')
cameraImage = imread('uin.png')

astroCropped = astronautImage.copy()
astroCropped = astroCropped[0:256,64:320]

cameraCropped = cameraImage.copy()
cameraCropped = cameraCropped[64:256,128:320]

print('Astro Ori Shape : ',astronautImage.shape)
print('Astro Crop Shape : ',astroCropped.shape)

print('Camera Ori Shape : ',cameraImage.shape)
print('Camera Crop Shape : ',cameraCropped.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(astronautImage)
ax[0].set_title("Citra Input 1")

ax[1].imshow(cameraImage, cmap='gray')
ax[1].set_title('Citra Input 2')

ax[2].imshow(astroCropped)
ax[2].set_title("Citra Output 1")

ax[3].imshow(cameraCropped, cmap='gray')
ax[3].set_title('Citra Output 2')
#plt.show()

#percobaan 2
inv = invert(astroCropped)
print('Shape Input : ', astroCropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(astroCropped)
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
#plt.show()

#percobaan 3
copyCamera = cameraCropped.copy().astype(float)

shape = copyCamera.shape
output1 = np.empty(shape)

for baris in range(0, shape[0] - 1):
    for kolom in range(0, shape[1] - 1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] / 192

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(cameraCropped, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].hist(cameraCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')
ax[3].hist(output1.ravel(), bins=192)
ax[3].set_title('Histogram Input')
print(output1.shape)
plt.show()