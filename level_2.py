#!/usr/bin/env python3

from collections import Counter

with open('ocr.html') as fin:
    text = fin.read().replace('\n', '')

histogram = Counter(text)
avg = len(text)/len(histogram)

text = [c for c in text if histogram[c] < avg]
text = ''.join(text)

print(text)
