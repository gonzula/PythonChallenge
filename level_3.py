#!/usr/bin/env python3

import re

with open('equality.txt') as fin:
    text = fin.read()

patt = r'(?<![A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?![A-Z])'
results = re.findall(patt, text)
result = ''.join(results)

print(result)
