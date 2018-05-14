import urllib.request
import os

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36')
    response=urllib.request.urlopen(url)
    html=response.read()

    return html
    

def get_page(url):
    url_open(url).decode('utf-8')


    a=html.find('current-comment-page')+23
    b=html.find(']',a)

    return html[a:b]
    
def find_image(url):
    html=url_open(url).deocde('utf-8')
    img_addrs =[]


    a=html.find('img src=')
    b=html.find('.jpg',a,a+255)
    if b!=-1:
        img_addrs.appedn(html[a+9:b+4])
    else:
        b =a+9
        a=html.find('img src=',b)
    for each in img_addrs:
        print(each)
    


def save(folder,img_addrs):
    pass


def download_mm(folder='ooxx',page=10):
    os.mkdir(folder)
    os.chdir(folder)

    url="http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -=i
        page_url=url+'page-'+str(page_num)+'#comments'
        img_addrs= find_imgs(page_url)
        save_imgs(folder,img_addrs)


if __name__=='__main__':
    download_mm()
