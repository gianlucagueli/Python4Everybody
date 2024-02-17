import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()

tree = html.decode()
stuff = ET.fromstring(tree)

lst = stuff.findall('.//count')

sum = 0

for item in lst:
    sum = sum + int(item.text)

print(sum)