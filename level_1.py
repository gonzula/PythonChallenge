#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/def/map.html

import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

k = 2

src = string.ascii_lowercase
dst = string.ascii_lowercase[k:] + string.ascii_lowercase[:k]

table = text.maketrans(src, dst)
print(text.translate(table))
print('map'.translate(table))

# next: http://www.pythonchallenge.com/pc/def/ocr.html
