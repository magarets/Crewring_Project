from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.naver.com' # url
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

for link in bs.findAll('a'):
    if 'href' in link.attrs: # find Hyperlink
        print(link.attrs['href'])