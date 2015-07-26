#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from lxml import html, cssselect
import requests
from termcolor import colored

from settings_local import *
from parse_rest.connection import register
from parse_rest.datatypes import Object as ParseObject

class Buy_and_sell(ParseObject):
       pass
class Servises(ParseObject):
       pass
class Cars_and_vehiacles(ParseObject):
       pass
class Pets(ParseObject):
       pass
class Vacation(ParseObject):
       pass
class Community(ParseObject):
       pass
class Real_estate(ParseObject):
       pass
class Jobs(ParseObject):
       pass
class Resumes(ParseObject):
       pass

def createArticle(**args):
    sector_name=createArticle.sector_name
    if sector_name=="buy and sell":
        article = Buy_and_sell(**args)
    elif sector_name=="services":
        article = Servises(**args)
    elif sector_name=="cars & vehicles":
        article = Cars_and_vehiacles(**args)
    elif sector_name=="pets":
        article = Pets(**args)
    elif sector_name=="vacation rentals":
        article = Vacation(**args)
    elif sector_name=="community":
        article = Community(**args)
    elif sector_name=="real estate":
        article = Real_estate(**args)
    elif sector_name=="jobs":
        article = Jobs(**args)
    elif sector_name=="resumes":
        article = Resumes(**args)
    return article

# Main get part
def create_Itmes(url_sections):
    array_list=[]
    page = requests.get(url_sections)
    tree=html.fromstring(page.text)
    try:
        next_page='http://www.kijiji.ca'+tree.cssselect("div.bottom-bar>div.pagination>a[title~=Next]")[0].get('href')
    except:
        print colored('next page doesnt exist','green','on_red')
        next_page=False
    for desription in tree.cssselect("table.regular-ad"):
        try:
            price=desription.cssselect("td.price")[0].text.strip(' ,$\t\n\r ,').replace(',','')
        except Exception, e:
            price="N/A"
        array_list.append(createArticle(
            name=desription.cssselect("td.description a")[0].text.strip(),
            url=desription.cssselect("td.description a")[0].get('href'),
            discription=desription.cssselect("td.description p")[0].text.encode('utf-8').strip(),
            price=price,
            category=create_Itmes.category
            ))
    return array_list, next_page