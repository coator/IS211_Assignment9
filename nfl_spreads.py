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
        self.current_working_file = fn + ".htm"
        self.localpath = os.getcwd()+self.current_working_folder
        self.htmfileloc = self.localpath + self.current_working_file

    def SearchDir(self):
        olen = os.listdir(self.localpath)
        return olen


def htm_pull(files, url):
    if len(files.SearchDir()) == 0:
        r = requests.get(url)
        open(files.localpath + files.current_working_file, 'xb').write(r.content)
    else:
        print('items in dir, skipping download')
    return


def parse_file(files):
    r = open(files.htmfileloc, encoding="utf-8")
    for rr in r:
        print(rr)


def main():
    fn = 'nfl_spreads'
    c = FParams(fn)
    print(c.localpath)
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    htm_pull(c, url)
    parse_file(c)


main()
