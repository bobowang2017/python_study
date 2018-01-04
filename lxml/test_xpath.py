# -*- coding: utf-8 -*-
import urllib2
import sys
from lxml import etree

reload(sys)
sys.setdefaultencoding("utf-8")

baseURL = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=530&bj=160000&sj=044&sg=73adc3d946504978b45b5b002a2a0e41&p=2"
head = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
request = urllib2.Request(baseURL, headers=head)
response = urllib2.urlopen(request)
pageCode = response.read().decode('utf-8')
tree = etree.HTML(pageCode)
items = tree.xpath("//*[@id='newlist_list_content_table']/table")
for index, item in enumerate(items):
    if index == 0:
        continue
    position = item.xpath("./tr[1]/td[1]/div/a/text()")
    company = item.xpath("./tr[1]/td[3]/a[1]/text()")
    salary = item.xpath("./tr[1]/td[4]/text()")
    city = item.xpath("./tr[1]/td[5]/text()")
    publishTime = item.xpath("./tr[1]/td[6]/span/text()")
    print("position=" + str(position) + "| company=" + str(company) + "|salary=" + str(salary) + "|city=" + str(city) + "|publishTime=" + str(publishTime))
