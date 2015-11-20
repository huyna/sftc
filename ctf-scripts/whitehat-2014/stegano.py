__author__ = 'HuyNA'
import Image
ct = 450
buf = 10
oldImg = Image.open("f100.png")
newImg = Image.new("RGB", (ct + buf, oldImg.size[0]/ct + buf), "#FFFFFF")
y = 0
for i in range(oldImg.size[0]):
    newImg.putpixel((i % ct, y), oldImg.getpixel((i, 0)))
    if i % ct == 0:
        y += 1