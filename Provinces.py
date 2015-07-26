# In Progress
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from lxml import html, cssselect
import requests
from termcolor import colored
# import urllib2
import requests
from termcolor import colored
print colored("---------привет мир--------", 'red')

from settings_local import *
from parse_rest.datatypes import Object as ParseObject

class Provinces(ParseObject):
    pass

page = requests.get('http://www.kijiji.ca/')
tree=html.fromstring(page.text)

for x in tree.xpath('//*[@id="LocationMenus"]/div[2]/section/ul/li'):
    # if x.xpath('/a'):
    print x.xpath('/a').text