import requests
from bs4 import BeautifulSoup
import os
import re
import json


class FParams:
    def __init__(self, fn):
        if os.name == 'nt':
            self.current_working_folder = '\\website_download\\' + fn + '\\'
        else:
            self.current_working_folder = "/website_download/" + fn + "/"
        self.current_working_file = fn + ".htm"
        self.localpath = os.getcwd() + self.current_working_folder
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
    a, aa = [], []
    r = open(files.htmfileloc, encoding="utf-8")
    soup = BeautifulSoup(r, "html.parser")
    # I didn't know how else to do this. Also Re is super helpful
    re_str = "<TR>\n\s\s\s\s<TD>.*<\/TD>\n\s\s\s\s<TD>.*<\/TD>\n\s\s\s\s<TD>.*<\/TD>\n\s\s\s\s<TD>.*<\/TD>\n\s\s<\/TR>"

    for item in soup(text=re.compile(re_str)):
        a.append(item)

    for item in a:
        g = re.findall(re_str, item)
        for i in g:
            i = i.replace('</TR>', '').replace('<TR>', '').replace('</TD>', ',').replace('<TD>', '') \
                .replace('\n    ', ' ').replace('\n  ', ' ').replace('&nbsp;<span title=\"Pick. No favorite', "Pick. " \
                                                                                                              "No "
                                                                                                              "favorite").replace(
                "no underdog. A point spread of zero.\">PK</span>", "no underdog. A point spread of zero.")
            aa.append(i)
    handicaps = []
    for item in aa:
        item = item.split(',')
        json_str = {"Date": item[0],
                    "TeamA": item[1],
                    "Handicapping score": item[2],
                    "TeamB": item[3]}
        json_out = json.dumps(json_str)
        handicaps.append(json_out)
    for x in handicaps: print(x)


def player_choice():
    choice_tuple = ('date', 'teama', 'handicapping', "teamb")
    while True:
        i = input('Please choose {}'.format(choice_tuple))
        if i == choice_tuple[0]:
            print(choice_tuple[0])
        elif i == choice_tuple[1]:
            print(choice_tuple[1])
        elif i == choice_tuple[2]:
            print(choice_tuple[2])
        elif i == choice_tuple[3]:
            print(choice_tuple[3])
        elif i == 'exit':
            exit()
        elif i not in choice_tuple:
            pass


def main():
    fn = 'nfl_spreads'
    c = FParams(fn)
    print(c.localpath)
    url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
    htm_pull(c, url)
    parse_file(c)
    player_choice()


main()
