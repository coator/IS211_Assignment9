import requests
from bs4 import BeautifulSoup
import os
import json


class FParams:
    def __init__(self, fn):
        if os.name == 'nt':
            self.current_working_folder = '\\website_download\\' + fn + '\\'
        else:
            self.current_working_folder = "/website_download/" + fn + "/"
        self.current_working_file = "" + fn + ".htm"
        self.localpath = os.path.abspath(os.getcwd() + self.current_working_folder)

    def TotalPath(self):
        p = self.localpath + self.current_working_file
        return str(p)

    def SearchDir(self):
        olen = os.listdir(self.localpath)
        return olen


def htm_pull(files, url):
    f = files()
    if len(f.SearchDir()) == 0:
        url = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical/'
        r = requests.get(url)
        open(f.localpath + f.current_working_file, 'xb').write(r.content)
    else:
        print('items in dir, skipping download')
    return


def parse_file(files):
    f = files()
    r = open(f.TotalPath(), encoding="utf-8")


def main():
    fn = 'nfl_spreads'
    c = FParams(fn)
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    htm_pull(, url)
    parse_file(FParams)


main()
