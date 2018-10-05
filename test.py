import urllib.request
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def url_open(url):
     req = urllib.request.Request(url)
     req.add_header('User-Agent' ,'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400')
     response = urllib.request.urlopen(req)
     html = response.read()
     return html

def get_page(url):
     html = url_open(url).decode('utf-8')
     a = html.find('current-comment-page') + len('current-comment-page">[')
     b = html.find(']',a)
     return (html[a:b])

def find_imgs(url):
      urls = [url]      
      img_url=[]
      driver =webdriver.PhantomJS(executable_path=r'F:\pip\phantomjs-2.1.1-windows\bin\phantomjs.exe')
      for url in urls:
          driver.get(url)
          data = driver.page_source
          soup = BeautifulSoup(data, "lxml")
          images = soup.select("a.view_img_link")

          for i in images:               
              z=i.get('href')
              if str('gif') in str(z):
                 pass
              else:
                  http_url = "http:" + z
                  img_url.append(http_url)
                  print("http:%s" % z)
 
      return img_url

def save_imags(folder,img_addrs):
     for each in img_addrs:
         filename=each.split('/')[-1]
         with open(filename,'wb') as f:
             img=url_open(each)
             f.write(img)
             time.sleep(5)
         

def download_mm(folder = 'OOXX1',pages=1000):
     os.mkdir(folder)
     os.chdir(folder)                          #将该文件夹设置为当前文件夹
     url = 'http://jandan.net/ooxx/'
     page_num = int(get_page(url))
     for i in range(35,pages): 
         page_num = 377-i
         if page_num<=0:
              break
         page_url = url +'page-'+ str(page_num) + '#comments'
         print(page_url)
         img_addrs = find_imgs(page_url)
         save_imags(folder,img_addrs)
         
if __name__ == '__main__':
     download_mm()
