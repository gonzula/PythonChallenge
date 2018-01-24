#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/return/5808.html

import requests
import io
import PIL.Image

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
un = 'huge'
pw = 'file'
auth = un, pw
req = requests.get(url, auth=auth)
img_io = io.BytesIO(req.content)
img = PIL.Image.open(img_io)

pixels = img.load()


half = img.size[0] // 2, img.size[1] // 2
img1 = PIL.Image.new('RGB', half, 'black')
img2 = PIL.Image.new('RGB', half, 'black')

pixels1 = img1.load()
pixels2 = img2.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (i + j) % 2:
            pixels1[i // 2, j // 2] = pixels[i, j]
        else:
            pixels2[i // 2, j // 2] = pixels[i, j]

img1.show()
img2.show()

# next: http://www.pythonchallenge.com/pc/return/evil.html
