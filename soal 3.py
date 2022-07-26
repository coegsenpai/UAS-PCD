#Local thresholding adalah suatu metode dimana dalam pencarian nilai ambang batas, gambar dipecah menjadi beberapa bagian gambar yang lebih kecil kemudian tiap bagian gambar tersebut akan dicari nilai ambang batasnya
from skimage import data
import matplotlib.pyplot as plt
from skimage.filters import sobel

original = data.astronaut()
gray = rgb2gray(original)
edge = sobel(gray)

plt.imshow(gray, cmap=plt.cm.gray)
plt.show()
plt.gray()
plt.imshow(edge)
plt.show