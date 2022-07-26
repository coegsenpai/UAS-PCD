from PIL import Image
from matplotlib import pyplot as plt

original = Image.open("./images.jpg")

flipvertical = original.transpose(method=Image.FLIP_TOP_BOTTOM)
fliphorizontal = original.transpose(method=Image.FLIP_LEFT_RIGHT)

fig, axes = plt.subplot(1,3, figsize=(8,4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("original")
ax[1].imshow(flipvertical)
ax[1].set_title("flipvertical")
ax[2].imshow(fliphorizontal)
ax[2].set_title("fliphorizontal")

fig.tight_layout()
plt.show()
