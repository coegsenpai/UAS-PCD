#Global thresholding adalah metode dengan seluruh pixel pada citra digital dikonversi menjadi hitam dan putih dengan satu nilai thresholding
from skimage.filters import try_all_threshold
from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt


original = data.astronaut()
gray = rgb2gray(original)
plt.imshow(original)
plt.show()

fig, ax = try_all_threshold(
    gray, figsize=(10,8), verbose=false
)

fig.tight_layout()
plt.show()