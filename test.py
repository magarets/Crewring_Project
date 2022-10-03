import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup

def crawlingHyperlink(url):
    
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.findAll('a'):
        if 'href' in link.attrs: # find Hyperlink
            print(link.attrs['href'])
            
def crawlingWeb(url):
    res = requests.get(url)
    
    if res.status_code == 200:
        print(res.text)
        

def main():
    
    url = 'https://www.naver.com' # url
    #crawlingHyperlink(url)
    crawlingWeb(url)

if __name__ == '__main__':
    main()