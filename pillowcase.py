from PIL import Image

im = Image.open("slc.jpg")

print(im.format, im.size, im.mode)

# How about in iPython / Jupyter?