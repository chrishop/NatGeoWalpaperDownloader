#!/usr/bin/env python3

import requests
import argparse
import os

from sys import argv
from os import system

def main():

    # argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="the name of the image excluding file extension")
    parser.add_argument("url", help="the url of a natgeo photo of the day")
    args = parser.parse_args(argv[1:])

    # scrape the page
    request = requests.get(args.url, allow_redirects=True)
    html_tmp = open("tmp.html", "w+")
    html_tmp.write(request.text)
    html_tmp.close()

    # find high resolution url in webpage
    read = open("tmp.html", 'r')
    url_line = ""

    for line in read.readlines():
        if 'og:image' in line:
            url_line = line
            break

    read.close()
    os.remove('tmp.html')
    img_url = url_line.split('\"')[3]

    # download
    image_request = requests.get(img_url)
    open(args.name + ".jpg", 'wb').write(image_request.content)


if __name__ == '__main__':
    main()
