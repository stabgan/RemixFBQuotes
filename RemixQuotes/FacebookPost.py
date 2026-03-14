#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Facebook Quote Poster

Posts random quotes to Facebook using Graph API.

@author: kaustabh
"""
import os
from facepy import GraphAPI
from webscrapper import Quotes


def main():
    # Get access token from environment variable or prompt user
    access_token = os.getenv('FB_ACCESS_TOKEN', '')
    
    if not access_token:
        print("Please set FB_ACCESS_TOKEN environment variable or edit this file")
        print("Get your token from: https://developers.facebook.com/tools/explorer")
        return
    
    try:
        web = Quotes() 
        graph = GraphAPI(access_token)
        
        message = f'"{web.randomquote()}"\nBy: {web.get_author()}'
        
        result = graph.post('me/feed', message=message)
        print(f"Successfully posted quote! Post ID: {result.get('id', 'Unknown')}")
        
    except Exception as e:
        print(f"Error posting to Facebook: {e}")


if __name__ == "__main__":
    main()

