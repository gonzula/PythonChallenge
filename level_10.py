#!/usr/bin/env python3

# url: http://huge:file@www.pythonchallenge.com/pc/return/bull.html

1
11
21
1211
111221
312211

def foo(n):
    if n == 0:
        return '1'

    text = foo(n-1)
    current_char = text[0]
    current_count = 1
    output = ''
    for c in text[1:]:
        if c == current_char:
            current_count += 1
        else:
            output += f'{current_count}{current_char}'
            current_count = 1
            current_char = c
    output += f'{current_count}{current_char}'
    return output

print(len(foo(30)))

# next: http://www.pythonchallenge.com/pc/return/5808.html

