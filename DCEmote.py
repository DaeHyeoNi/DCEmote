import requests
from bs4 import BeautifulSoup
from os.path import basename
from os.path import isdir
from os import mkdir
from magic import from_buffer
from shutil import rmtree


emote_name = '쭐어#60302'

if __name__ == "__main__":
    url = 'https://dccon.dcinside.com/hot/1/title/' + emote_name

    print('Started Download ' + emote_name)

    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    img = soup.find_all('img', {'class': 'thumb_img'})

    # get extension from file header
    buf = from_buffer(requests.get(img[0].get('src')).content)
    extension = 'jpg'
    if 'JPEG' not in buf:
        extension = 'png'
    
    # make image download directory or if exists delete old images
    path = "./img/"
    if not isdir(path):                                                           
        mkdir(path)
    else:
        rmtree(path)
        mkdir(path)

    # download images
    for i, j in enumerate(img):
        link = j.get('src')
        filename = basename('{}.{}'.format(i, extension))
        with open(path + filename, "wb") as f:
            print('Download ' + filename)
            f.write(requests.get(link).content)
    
    print('The download operation is complete.')
