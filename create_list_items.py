#!/usr/bin/env python
# -*- coding: utf-8 -*-
from page_items import create_Itmes, createArticle
from kijiji import createCategory
from termcolor import colored
from parse_rest.connection import ParseBatcher
from parse_rest.datatypes import Object as ParseObject

batcher = ParseBatcher()
# GLOBAL VARIABLES
CITY='http://www.kijiji.ca/h-red-deer/1700136'
DEEP=7
class Category(ParseObject):
       pass
def create_parse_Category(name, url):
    article = Category(**locals())
    return article

def create_list_items(list_url):
    current_url='http://www.kijiji.ca'+list_url[1]
    new_category=create_parse_Category(name=list_url[0],
        url=list_url[1]
        )
    new_category.save()
    print list_url[0]
    for x in xrange(0,DEEP):
        if current_url:
            print current_url
            items=create_Itmes(current_url)
            batcher.batch_save(items[0])
            current_url = items[1]

def push_data(city_url):
    print 'start pushing data'
    for k, m in createCategory(city_url).iteritems():
        # global sector_name
        createArticle.sector_name=k
        print k
        map (create_list_items, m)


push_data(CITY)