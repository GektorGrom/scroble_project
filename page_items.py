#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html, cssselect
import requests
from termcolor import colored

# Main get part
def create_Itmes(url_sections):
    array_list=[]
    page = requests.get(url_sections)
    tree=html.fromstring(page.text)
    x=tree.cssselect("table.regular-ad")
    next_page='http://www.kijiji.ca'+tree.cssselect("div.bottom-bar>div.pagination>a[title~=Next]")[0].get('href')
    for desription in x:
        empty_dic={
                "name":desription.cssselect("td.description a")[0].text.strip(),
                "url":desription.cssselect("td.description a")[0].get('href'),
                "discription":desription.cssselect("td.description p")[0].text.encode('utf-8').strip(),
                "price":desription.cssselect("td.price")[0].text.strip(' ,$\t\n\r ,') # converte str to float
        }
        array_list.append(empty_dic)
    return array_list, next_page