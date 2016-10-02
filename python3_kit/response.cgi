#!/usr/bin/python3

import cgi

from python3_kit import checksum

print('Content-type: text/html\n')
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

form = cgi.FieldStorage()
response_dict = {}

for i in form.keys():
    response_dict[i] = form[i].value
    if i == 'CHECKSUMHASH':
        checksum = form[i].value

if 'GATEWAYNAME' in response_dict:
    if response_dict['GATEWAYNAME'] == 'WALLET':
        response_dict['BANKNAME'] = 'null'

verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
print(verify)

if verify and response_dict['RESPCODE'] == '01':
    print('order successful')
else:
    print('order unsuccessful because' + response_dict['RESPMSG'])
