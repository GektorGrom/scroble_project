#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "привет мир"
from lxml import html
# import urllib2
import requests
from termcolor import colored

def local_print(**args):
    y=2
    print(**args)
local_print(name='s', price=45)