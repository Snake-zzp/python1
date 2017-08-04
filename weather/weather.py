#查找中国各地天气
#利用usrlib2 json 

import urllib
from urllib import request
from city import city
import json

web=urllib.request.urlopen('http://www.weather.com.cn')

cityname=input('你想查的城市是：\n')
citycode=city.get(cityname)
if citycode:
    try:

        url='http://www.weather.com.cn/data/cityinfo/%s.html'%citycode
        content=urllib.request.urlopen(url).read()
        data=json.loads(content)
        result=data['weatherinfo']
        str_temp=('%s\n%s~%s')%(
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print (str_temp)
    except:
        print ('查询失败')
else:
    print('没有该城市')
#print (content)














