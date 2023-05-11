#Mengimport library yang diperlukan yaitu cv2, matplotlib, skimage.data, skimage.io, skimage.color, dan skimage.util.
import cv2
import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
#Mengimport numpy dan memberikan alias np pada numpy.
import numpy as np

#Percobaan 1
# Load and crop two images
astronautImage = imread('aadc.jpeg')#Membaca citra dengan menggunakan imread() pada library skimage.io dan dimasukkan ke dalam variabel astronautImage dan cameraImage.
cameraImage = imread('uin.png')

astroCropped = astronautImage.copy()#Melakukan cropping pada citra astronautImage dan cameraImage dengan copy() dan slicing pada indeks piksel untuk mendapatkan bagian dari citra yang diinginkan.
astroCropped = astroCropped[0:256,64:320]

cameraCropped = cameraImage.copy()#Melakukan cropping pada citra astronautImage dan cameraImage dengan copy() dan slicing pada indeks piksel untuk mendapatkan bagian dari citra yang diinginkan.
cameraCropped = cameraCropped[64:256,128:320]

# Print the shapes of the original and cropped images
print('Astro Ori Shape : ',astronautImage.shape)#Menampilkan bentuk matriks dari citra asli dan citra hasil cropping menggunakan shape.
print('Astro Crop Shape : ',astroCropped.shape)

print('Camera Ori Shape : ',cameraImage.shape)
print('Camera Crop Shape : ',cameraCropped.shape)
# Display the original and cropped images using subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 12))#Membuat plot gambar menggunakan subplot dengan ukuran 2x2 dengan judul yang sudah diberikan. Terdapat 4 gambar, 2 gambar asli dan 2 gambar hasil cropping yang telah disiapkan.
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
#Invert the input image
inv = invert(astroCropped)
#Print the input and output image shape
print('Shape Input : ', astroCropped.shape)
print('Shape Output : ',inv.shape)

#Plot the input and output images along with their histograms
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
#Meng-copy citra cameraCropped ke dalam variabel copyCamera dengan tipe data float
copyCamera = cameraCropped.copy().astype(float)
#Mendapatkan ukuran citra dan membuat array kosong dengan ukuran yang sama dengan citra
shape = copyCamera.shape
output1 = np.empty(shape)
#Looping untuk setiap piksel pada citra
for baris in range(0, shape[0] - 1):
    for kolom in range(0, shape[1] - 1):# Memperoleh koordinat piksel pada citra yang akan diubah nilai
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] / 192# Menghitung nilai brightness baru dengan membagi nilai brightness pada
#Menampilkan citra input, histogram input, citra output brightness, dan histogram output
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
print(output1.shape)#Menampilkan ukuran citra output pada variabel output1 dan menampilkan gambar
plt.show()