#-*- coding: utf-8 -*
# version python2.7
#!/usr/bin/env python

#download HTML
import urllib2,urllib,gzip,StringIO,re,sys
from bs4 import BeautifulSoup as bs

def download_html(url):
    print "Download url...",url
#模拟浏览器
    header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'en-US,en;q=0.8',
    'cache-control':'max-age=0',
    'user_agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    try:
        req = urllib2.Request(url,headers = header)
        response = urllib2.urlopen(req)
        reheader = response.info()
        body = response.read()
    except urllib2.URLError as e:
        print "Download Error：",e.reason
        body = None
    encoding = reheader.get("Content-Encoding")
    if encoding == "gzip":
        content = gz_decoding(body).strip()
    else:
        content = body.strip()
    return content
#解压
def gz_decoding(data):
    compressdstream = StringIO.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressdstream)
    data2 = gziper.read()
    return data2

#analysis content

def get_url(key, page = 1):
    print 'get urls...'
    keyword = urllib.quote(key.strip())
    urls = []
    i=1
    while(i<=page):
        url = "https://list.tmall.com/search_product.htm?type=pc&q=%s&totalPage=100&sort=s&style=g&from=mallfp..pc_1_suggest&suggest=0_1&jumpto=%d#J_Filter"%(keyword,i)
        urls.append(url)
        i = i + 1
    return urls
#解析
def xls(key,url):
    keyword = urllib.quote(key.strip())
    html = download_html(url)
    soup = bs(html,"lxml")
    global price
    res = soup.select(".product-iWrap")
    p = re.compile(r"([\s\S]*?)<\/p>", re.I | re.M)
    t = re.compile(r"([\s\S]*?)<\/p>", re.I | re.M)
    c = re.compile(r"([\s\S]*?)<\/span>", re.I | re.M)
    for i in res:
        try:
            price = re.sub(r'<[^>]+>','',p.search(str(i)).group(1)).decode('utf-8').encode(type).strip()
            title = re.sub(r'<[^>]+>','',t.search(str(i)).group(1)).decode('utf-8').encode(type).strip()
            count = re.sub(r'<[^>]+>','',c.search(str(i)).group(1)).decode('utf-8').encode(type).strip()
        except:
            pass
        with open(key+'.xls','a') as f:
            txt = '%s\t%s\t%s\n'%(title,price,count)
            f.write(txt)

type = sys.getfilesystemencoding()

key = raw_input("Please input product:")

urls = get_url(key)
f = open(key+".xls","w")
firstline = "商品名称\t价格\t销量\n"
f.write(firstline.decode("utf-8").encode(type))
f.close()
for u in urls:
    xls(key,u)

pp = []
cc = []
pp = pp.append(price)
cc = cc.append(count)
int_price = [int(x) for x in pp]
int_count = [int(x) for x in cc]
print int_price

import matplotlib.pyplot as plt
plt.plot(int_count,int_price,'ro')
plt.axis([0,200,0,300])
plt.show()

print 'End!