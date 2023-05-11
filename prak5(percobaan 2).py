import numpy as np #Mengimport library NumPy dengan alias np untuk melakukan operasi array pada gambar.
import imageio
import cv2#Mengimport library OpenCV untuk melakukan operasi gambar.
import matplotlib.pyplot as plt#Mengimport library Matplotlib untuk menampilkan gambar.

img = cv2.imread("aadc.jpeg")#Membaca gambar dengan nama "aadc.jpeg" menggunakan fungsi imread()

img_height =img.shape[0]# Mengambil ukuran tinggi gambar dan memasukkannya ke dalam variabel img_height.
img_width = img.shape[1]#Mengambil ukuran lebar gambar dan memasukkannya ke dalam variabel img_width.
img_channel = img.shape[2]#Mengambil jumlah channel gambar dan memasukkannya ke dalam variabel img_channel.

img_type = img.dtype#Mengambil tipe data gambar dan memasukkannya ke dalam variabel img_type.

img_brightness = np.zeros(img.shape, dtype= np.uint8)#Membuat array kosong dengan ukuran yang sama dengan gambar dan menetapkan tipe data uint8

def brighter(nilai):#Mendefinisikan fungsi brighter dengan satu parameter input nilai.
    for y in range(0, img_height):#Looping untuk setiap baris (y) pada gambar.
        for x in range(0, img_width):# Looping untuk setiap kolom (x) pada gambar.
            red= img[y][x][0]#Mendapatkan nilai pixel merah pada koordinat (x, y).
            green= img[y][x][1]# Mendapatkan nilai pixel hijau pada koordinat (x, y).
            blue= img[y][x][2]#Mendapatkan nilai pixel biru pada koordinat (x, y).
            gray= (int(red)+ int(green)+int(blue))/3#Menghitung nilai rata-rata dari ketiga channel warna pada pixel (x, y).
            gray += nilai#Menambahkan nilai parameter input nilai ke dalam nilai rata-rata warna pada pixel (x, y).
            if gray >255:#Mengecek apakah nilai gray lebih besar dari 255.
                gray= 255# Jika nilai gray lebih besar dari 255, maka nilai gray akan diset menjadi 255.
            if gray<0:#Mengecek apakah nilai gray kurang dari 0.
                gray = 0#Jika nilai gray kurang dari 0, maka nilai gray akan diset menjadi 0.
            img_brightness[y][x] = (gray, gray, gray)#Menetapkan nilai pixel baru pada koordinat (x, y) pada gambar hasil.
#menampilkan gambar dengan parameter -100
brighter(-100)# Memanggil fungsi brighter dengan parameter input -100.
plt.imshow(img_brightness)#Menampilkan gambar hasil pada plot.
plt.title("brightness -100")
plt.show()

brighter(25)# Memanggil fungsi brighter dengan parameter input 25.
plt.imshow(img_brightness)#Menampilkan gambar hasil pada plot.
plt.title("Brigtness 100")
plt.show()

#rgb
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)#membuat array numpy kosong dengan dimensi yang sama dengan citra asli dan tipe data unsigned integer 8-bit.
#fungsi untuk brightness rgb dengan nilai parameter

def rgbbrighter(nilai):#mendefinisikan fungsi rgbbrighter yang menerima parameter nilai.
    for y in range(0, img_height):
        for x in range(0, img_width):#erasi semua pixel pada gambar dengan mengakses nilai baris y dan kolom x dari gambar.
            red=img[y][x][0]#mengambil nilai kanal merah untuk pixel di koordinat (x, y).
            red+= nilai#menambahkan nilai parameter nilai ke kanal merah untuk pixel di koordinat (x, y).
            if red > 255:
                red = 255
            if red < 0:
                red = 0#memastikan bahwa nilai kanal merah tidak melebihi 255 atau kurang dari 0.
            green = img[y][x][1]#mengambil nilai kanal hijau dan biru untuk pixel di koordinat (x, y).
            green += nilai#menambahkan nilai parameter nilai ke kanal hijau dan biru untuk pixel di koordinat (x, y).
            if green > 255:
                green = 255
            if green < 0:
                green = 0# memastikan bahwa nilai kanal hijau dan biru tidak melebihi 255 atau kurang dari 0.
            blue = img[y][x][2]#mengambil nilai kanal hijau dan biru untuk pixel di koordinat (x, y).
            blue += nilai#menambahkan nilai parameter nilai ke kanal hijau dan biru untuk pixel di koordinat (x, y).
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0# memastikan bahwa nilai kanal hijau dan biru tidak melebihi 255 atau kurang dari 0.
            img_rgbbright[y][x] = (red, green, blue)#menetapkan nilai piksel yang diubah ke array gambar yang baru dibuat.
#menampilkan
rgbbrighter(-100)#memanggil fungsi rgbbrighter dengan parameter -100 dan 100
plt.imshow(img_rgbbright)#enampilkan citra baru yang dihasilkan.
plt.title("Brightness -100")# menampilkan judul citra yang sesuai untuk masing-masing citra baru.
plt.show()#menampilkan citra pada plot matplotlib.
rgbbrighter(100)#memanggil fungsi rgbbrighter dengan parameter -100 dan 100
plt.imshow(img_rgbbright)#enampilkan citra baru yang dihasilkan.
plt.title("Brightness 100")#menampilkan judul citra yang sesuai untuk masing-masing citra baru.
plt.show()#menampilkan citra pada plot matplotlib.

#membuat matriks nol dengan ukuran yang sama dengan gambar
img_contrass = np.zeros(img.shape, dtype=np.uint8)
#fungsi untuk kontras dengan nilai parameter
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):# mendapatkan nilai RGB dari setiap piksel gambar
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]## menghitung nilai rata-rata RGB untuk membuat citra abu-abu
            gray = (int(red) + int(green) + int(blue)) / 3# mengalikan citra abu-abu dengan nilai kontras
            gray *= nilai# menentukan nilai maksimum 255 untuk masing-masing komponen warna
            if gray > 255:
                gray = 255# menyimpan nilai kontras baru untuk setiap piksel gambar
            img_contrass[y][x] = (gray, gray, gray)

# menampilkan gambar dengan kontras 2
contrass(2)
plt.imshow(img_contrass)
plt.title("Contrass 2")
plt.show()
#menampilkan gambar dengan kontras 3
contrass(3)
plt.imshow(img_contrass)
plt.title("Contrass 3")
plt.show()

img_contrasrgb = np.zeros(img.shape, dtype=np.uint8)#Membuat array kosong dengan ukuran yang sama dengan gambar input
# fungsi rgb
def rgbcontrass(nilai):#Fungsi untuk menambahkan kontras pada gambar dengan parameter nilai
    for y in range(0, img_height):## Looping untuk setiap pixel pada gambar
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255#memastikan bahwa nilai kanal merah tidak melebihi 255 .
            green = img[y][x][1]#memastikan bahwa nilai kanal merah tidak melebihi 255 .
            green += nilai
            if green > 255:
                green = 255#memastikan bahwa nilai kanal hijau tidak melebihi 255 .
            blue = img[y][x][2]#memastikan bahwa nilai kanal merah tidak melebihi 255 .
            blue += nilai
            if blue > 255:
                blue = 255#memastikan bahwa nilai kanal biru tidak melebihi 255 .
            img_contrasrgb[y][x] = (red, green, blue)


# menampilkan
rgbcontrass(20)#Menambahkan kontras pada gambar dengan nilai 20
plt.imshow(img_contrasrgb)
plt.title("contrass 20")
plt.show()
rgbcontrass(100)#Menambahkan kontras pada gambar dengan nilai 100
plt.imshow(img_contrasrgb)
plt.title("contrass 100")
plt.show()


#autocontrass
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)#Membuat array kosong dengan tipe data uint8 berukuran sama dengan citra

def autocontrass():#Fungsi untuk kontras otomatis
    xmax = 300
    xmin = 0
    d = 0
    # Mencari nilai maksimum dan minimum dari citra
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    # Menghitung faktor skala
    d = xmin-xmax
    # Menetapkan nilai kontras baru pada setiap piksel
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)
#Memanggil fungsi autocontrass() untuk menghasilkan gambar kontras otomatis
autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")
plt.show()


