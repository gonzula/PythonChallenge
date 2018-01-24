#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/def/oxygen.html

import PIL.Image
import requests
import io
import re

def is_printable_ascii(p):
    return 32 <= p <= 126

def is_gray(p):
    return p[0] == p[1] == p[2]

req = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
img_io = io.BytesIO(req.content)
img = PIL.Image.open(img_io)

position = (2, 48)
offset = 7
pixels = img.load()

gray_pixels = []
while position[0] < img.size[0]:
    p = pixels[position]
    if is_gray(p) and is_printable_ascii(p[0]):
        gray_pixels.append(p[0])
    position = position[0] + offset, position[1]

text = ''.join(chr(p) for p in gray_pixels)

match = re.search(r'\[(?:\d+(?:,\s+)?)+\]', text)
list_str = match.group(0)
numbers = eval(list_str)
next_level = ''.join(chr(x) for x in numbers)

text = text.replace(list_str, next_level)
print(text)

# next: http://www.pythonchallenge.com/pc/def/integrity.html
