#!/usr/bin/python3

from python3_kit import checksum

print('Content-type: text/html\n')

MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'
TRANSACTION_URL = 'https://pguat.paytm.com/oltp-web/processTransaction'
data_dict = {
    'MID': 'WorldP64425807474247',
    'ORDER_ID': 'dddgfgfeeed',
    'TXN_AMOUNT': '1',
    'CUST_ID': 'acfff@paytm.com',
    'INDUSTRY_TYPE_ID': 'Retail',
    'WEBSITE': 'worldpressplg',
    'CHANNEL_ID': 'WEB',
}

param_dict = data_dict.copy()
param_dict['CHECKSUMHASH'] = checksum.generate_checksum(
    data_dict,
    MERCHANT_KEY
)

print('<h1>Merchant Check Out Page</h1></br>')
print('<form method="post" action="{}" name="f1">'.format(TRANSACTION_URL))
print('<table border="1">')
print('<tbody>')
for key in param_dict:
    print(
        '<input type="hidden" name="{}" value="{}">'.format(
            key.strip(),
            param_dict[key].strip()
        )
    )
print('</tbody>')
print('</table>')
print('<script type="text/javascript">')
print('document.f1.submit();')
print('</script>')
print('</form>')
