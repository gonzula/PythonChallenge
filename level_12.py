#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/return/evil.html

import requests
import io
import PIL.Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'
un = 'huge'
pw = 'file'
auth = un, pw
req = requests.get(url, auth=auth)
data = req.content

k = 5

bins = [[] for i in range(k)]

for idx, byte in enumerate(data):
    bins[idx % k].append(byte)

bins = [bytes(i) for i in bins]
for idx, b in enumerate(bins):
    img_io = io.BytesIO(b)
    PIL.Image.open(img_io).show()

# next: http://www.pythonchallenge.com/pc/return/disproportional.html
