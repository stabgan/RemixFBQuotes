#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 01:18:34 2018

@author: kaustabh
"""
from facepy import GraphAPI
from webscrapper import Quotes

#enter your access_token inside the quotes from https://developers.facebook.com/tools/explorer
ACCESS_TOKEN = '' 

web = Quotes() 
graph = GraphAPI(ACCESS_TOKEN)

message = "\" "+web.randomquote()+"\""+"\n By : "+web.author

graph.post('me/feed', message = message)

