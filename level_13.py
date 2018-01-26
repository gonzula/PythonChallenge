#!/usr/bin/env python3

# url: http://www.pythonchallenge.com/pc/return/disproportional.html

import requests

number = 'Bert'

url = 'http://www.pythonchallenge.com/pc/phonebook.php'
data = '''<?xml version="1.0"?>
<methodCall>
  <methodName>phone</methodName>
  <params>
    <param>
        <value><string>%s</string></value>
    </param>
  </params>
</methodCall>''' % (number, )

req = requests.post(url, data=data)

print(req.text)
