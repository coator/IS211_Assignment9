import urllib.request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import os
import json
ua = UserAgent()

class FParams:
    def __init__(self):
        if os.name == 'nt':
            self.current_working_folder = '\\website_download\\apple_stock\\'
        else:
            self.current_working_folder = "/website_download/apple_stock/"
        self.current_working_file = "apple_stock.htm"

    def LocalPath(self):
        return os.path.abspath(os.getcwd() + self.current_working_folder)

    def TotalPath(self):
        p = self.LocalPath() + self.current_working_file
        return str(p)

    def SearchDir(self):
        olen = os.listdir(self.LocalPath())
        return olen


def htm_pull(files):
    f = files()
    ff = f.LocalPath()
    print(ff)
    if len(f.SearchDir()) == 0:
        url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical/'
        req = urllib.request.Request(url, headers={'User-Agent': ua.random})
        f = urllib.request.urlopen(req)
        print(f.read().decode('utf-8'))

    else:
        print('items in dir, skipping download')
    return


def parse_file(files):
    pass


def main():
    htm_pull(FParams)
    parse_file(FParams)


main()
