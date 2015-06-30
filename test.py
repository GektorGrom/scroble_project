#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "привет мир"
from lxml import html
# import urllib2
import requests
from termcolor import colored

page = requests.get('http://www.kijiji.ca')
tree=html.fromstring(page.text)
html =tree.xpath('//text()')
print html