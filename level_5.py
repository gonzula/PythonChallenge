#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from pprint import pprint

with open('banner.p', 'rb') as fin:
    data = pickle.load(fin)

for l in data:
    for c, n in l:
        print(c * n, end='')
    print()

# next: http://www.pythonchallenge.com/pc/def/channel.html
