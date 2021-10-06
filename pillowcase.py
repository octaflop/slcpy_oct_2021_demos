from PIL import Image

im = Image.open("slc.jpg")

print(im.format, im.size, im.mode)