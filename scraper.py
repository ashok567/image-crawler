import requests
import random
from bs4 import BeautifulSoup

def scrap_url(url):
    try:
        response = requests.get(url)
        html = response.text
        return html
    except Exception:
        print('Opps! Occurred error')
        return None


def scrap_photo(requests_url):
    soup = BeautifulSoup(requests_url, 'lxml')
    photo_url = soup.find("meta", property="og:image")
    return photo_url["content"]


def downloader(photo_url):
    num = random.randrange(1000000)
    photo_name = "insta"+str(num)
    requests_url = requests.get(photo_url)
    with open(photo_name + '.jpg', 'ab') as f:
        f.write(requests_url.content)
    print('Download completed')


def download_image(url):
    request_url = scrap_url(url)
    photo_url = scrap_photo(request_url)
    downloader(photo_url)