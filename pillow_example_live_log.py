# coding: utf-8
from PIL import Image
im = Image.open("slc.jpg")
print(im.format)
im.palette
get_ipython().run_line_magic('pinfo', 'im')
im.getexif()
exif = im.getexif()
help(exif)
get_ipython().run_line_magic('pinfo', 'exif')
str(exif)
im
from PIL import ImageFilter
out = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
out.save('edge_enhance.jpg')
out = im.filter(ImageFilter.BLUR).filter(ImageFilter.EMBOSS)
out.save('emboss_blur.jpg')
out = im.filter(ImageFilter.BLUR)
out.save('just_blur.jpg')
out = im.filter(ImageFilter.BLUR).filter(ImageFilter.BLUR)
out.save('just_blur.jpg')
out = im.filter(ImageFilter.SMOOTH_MORE)
out.save('smooth_more.jpg')
out.getdata()
d = out.getdata()
d
d.bands
im.width
im.height
out = im.resize((im.width // 3, im.height // 3))
out.save('resizedslc.jpg')
out.width
out.height
6048 // 3
6048 / 3
6049 / 3
6049 // 3
6044 // 3
6044 / 3
round(6044 / 3)
floor(6044 / 3)
import math
math.floor(6044 / 3)
hi = "unicode thing haha"
thing = b"byte thing"
type(hi)
type(thing)
get_ipython().run_line_magic('save', 'ipython_log 1-47')
