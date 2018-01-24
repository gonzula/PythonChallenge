#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/def/linkedlist.html

import requests
import re

p = '12345'
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
patt = r'and the next nothing is (\d+)'

while True:
    req = requests.get(url, params={'nothing': p})
    text = req.text
    print(text)
    match = re.search(patt, text)
    if not match:
        if 'Yes. Divide by two and keep going.' in text:
            p = int(p) // 2
            continue
        break
    p = match.group(1)

# next: http://www.pythonchallenge.com/pc/def/peak.html
