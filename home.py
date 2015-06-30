#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "привет мир"
from lxml import html
# import urllib2
import requests
from termcolor import colored


def printall(x):
    print colored(x[0].encode('utf-8'), 'magenta'), 'by', colored(getAuthor(x[1]), 'blue')

def getAuthor(x):
    page=requests.get(x)
    tree=html.fromstring(page.text)
    author=tree.xpath('//*[@id="main"]/div/h3/text()')
    return str(author)[2:-2]

def combineLists(list1,list2):
    listy=[]
    for index in xrange(0,len(list1),1):
        # print list2[index]
        listy.append([list1[index],list2[index]])
    return listy


page = requests.get('http://jesse.co.ua')
print colored(page.status_code,'red')
print colored(page.encoding,'green')
tree=html.fromstring(page.text)
posts = tree.xpath('//*[@id="index"]/article/h2/a/text()')
posts_links = tree.xpath('//*[@id="index"]/article/h2/a/@href')
feed=posts+posts_links
map(printall, combineLists(posts,posts_links))
