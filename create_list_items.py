#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_items import create_Itmes
print "привет мир"
from termcolor import colored

deep_pages=4
list_url='http://www.kijiji.ca/b-cars-trucks/red-deer/convertible__coupe__hatchback__other+body+type__sedan__wagon/c174l1700136a138'
def create_list_items(deep_pages, list_url):
    result=[]
    for x in xrange(0,deep_pages):
        if result!=[]:
            result=result+create_Itmes(list_url)[0]
            _, list_url = create_Itmes(list_url)
        else:
            result = result+create_Itmes(list_url)[0]
            list_url = create_Itmes(list_url)[1]
    return result

y = create_list_items(2,list_url)
for x in y:
    print colored(x['name'],'green') , x['discription'], colored(x['price'],'red')
print len(y)