#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/def/channel.html

from zipfile import ZipFile
import re

fname = 'channel.zip'
input_zip = ZipFile(fname)
files = {name[:-4]: (
    input_zip.read(name).decode('utf-8'),
    input_zip.getinfo(name).comment.decode('utf-8')
    )
         for name in input_zip.namelist()}

p = '90052'
comments = []
patt = r'Next nothing is (\d+)'

while True:
    comments.append(files[p][1])
    text = files[p][0]
    print(text)
    match = re.search(patt, text)
    if not match:
        break
    p = match.group(1)

print(''.join(comments))

# next: http://www.pythonchallenge.com/pc/def/oxygen.html
