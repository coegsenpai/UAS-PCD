#edge detection adalah cara-cara matematis untuk mengenali titik-titik dalam citra digital yang kecerahanya berubah drastis atau memiliki diskontinuitas
from skimage import data
import matplotlib.pyplot as plt
from skimage.filters import sobel
from skimage.color import rgb2gray

original = data.astronaut()
gray = rgb2gray(original)
edge = sobel(gray)

plt.imshow(gray, cmap=plt.cm.gray)
plt.show()

plt.imshow(edge)
plt.show