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
categoryQry = Category.Query.all()
categories = {source.name: source for source in categoryQry}

def createCategory_selected(name):
    if name in categories:
        return categories[name]

    source = Category(**locals())
    source.save()

    categories[source.name] = source

    return source

def create_parse_Category(name, url):
    article = Category(**locals())
    return article

def create_list_items(list_url):
    current_url='http://www.kijiji.ca'+list_url[1]
    create_Itmes.category=createCategory_selected(list_url[0])
    print colored(list_url[0], 'blue', attrs=['underline'])
    for x in xrange(0,DEEP):
        num='--------------------page #'+str(x+1)+'--------------------'
        if current_url:
            print num
            print colored(current_url, 'grey')
            items=create_Itmes(current_url)
            batcher.batch_save(items[0])
            current_url = items[1]

def push_data(city_url):
    print 'start pushing data'
    for k, m in createCategory(city_url).iteritems():
        # global sector_name
        createArticle.sector_name=k
        print colored(k, 'red',attrs=['bold'])
        map (create_list_items, m)


push_data(CITY)