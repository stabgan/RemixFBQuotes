#!/usr/bin/env python3
"""Fetch a random quote and post it as a Facebook status using the Graph API."""

import sys

from facepy import GraphAPI
from webscrapper import Quotes


def main():
    # Enter your access_token from https://developers.facebook.com/tools/explorer
    ACCESS_TOKEN = ""

    if not ACCESS_TOKEN:
        print("Error: Please set your Facebook ACCESS_TOKEN in this file.")
        print("Get one at: https://developers.facebook.com/tools/explorer")
        sys.exit(1)

    web = Quotes()
    quote = web.randomquote()
    author = web.get_author()

    message = f'"{quote}"\n — {author}'

    try:
        graph = GraphAPI(ACCESS_TOKEN)
        graph.post("me/feed", message=message)
        print("Quote posted to Facebook successfully!")
        print(message)
    except Exception as e:
        print(f"Error posting to Facebook: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
