import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = str(input('Enter URL: '))
count = int(input('Enter count: '))
position = int(input('Enter position: '))

while count >= 0 :
    print("Retrieving:" + url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    tmp_pos = 0
    for tag in tags:
        tmp_pos = tmp_pos + 1
        if(tmp_pos == position) :
            url = tag.get('href', None)
    count = count - 1


