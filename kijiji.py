#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "привет мир"
from lxml import html
# import urllib2
import requests
from termcolor import colored

def printall(x):
    print colored(x[0], 'blue'),'@',colored(x[1],'magenta')

def combineLists(list1,list2):
    listy=[]
    for index in xrange(0,len(list1),1):
        listy.append([list1[index],list2[index]])
    return listy

# Main get part


# def get_ul(sect):
#     ul=[]
#     for x in xrange(1,(sect+1)):
#         path='//*[@id="Categories"]/section['+str(x)+']/ul'
#         ul.append(tree.xpath(path))
#     return ul

def createCategory(URL):
    page = requests.get(URL)
    print colored(page.status_code,'green')
    print colored(page.encoding,'green')
    tree=html.fromstring(page.text)
    sections = len(tree.xpath('//*[@id="Categories"]/section'))
    temp_dic={}
    ul=[]
    for x in xrange(1,(sections+1)):
        path='//*[@id="Categories"]/section['+str(x)+']/ul'
        ul.append(tree.xpath(path))
    # create list of podcategory
    for x in xrange(1,(sections+1)):
        for z in xrange(1,(len(ul[(x-1)])+1)):
            category_name=tree.xpath('//*[@id="Categories"]/section['+str(x)+']/ul['+str(z)+']/li/h2/a/text()')
            category_selected=(tree.xpath('//*[@id="Categories"]/section['+str(x)+']/ul['+str(z)+']/li/a/text()'))
            url_selected=(tree.xpath('//*[@id="Categories"]/section['+str(x)+']/ul['+str(z)+']/li/a/@href'))
            temp_dic.update({str(category_name)[2:-2]:combineLists(category_selected,url_selected)})
    print colored("Category DONE!", 'magenta')
    return temp_dic

# for k, m in createCategory('http://www.kijiji.ca/h-red-deer/1700136').iteritems():
#     print colored(k,'green')
#     print '=============='
#     map(printall, m)
#     # print m