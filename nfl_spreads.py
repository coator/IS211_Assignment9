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
                    "Favorite": item[1],
                    "Spread": item[2],
                    "Underdog": item[3]}
        json_out = json.dumps(json_str)
        handicaps.append(json_out)
    return handicaps


def player_choice(handicaps):
    for i in handicaps:
        h = json.loads(i)
        print(h['Date'].strip('ET'))
    while True:
        date_choice = input('Please choose a date and time from above: ')
        date_choice = ' '+date_choice + ' ET '
        truthy_return = False
        for x in handicaps:

            h = json.loads(x)
            if h['Date'].strip(' ') == str(date_choice.strip(' ')):
                if h['Favorite'][0:3] == ' At':
                    print('{}: Underdog{}{} with a spread of{}'.format(h['Date'], h['Underdog'],h['Favorite'],
                                                                                        h['Spread']))
                    truthy_return = True
                else:
                    print('{}: Favorite{}{} with a spread of{}'.format(h['Date'], h['Favorite'], h['Underdog'],
                                                                                        h['Spread']))
                    truthy_return = True
        if truthy_return:
            return
        else:
            print('None Returned, Please try again')




def main():
    fn = 'nfl_spreads'
    c = FParams(fn)
    url = "http://www.footballlocks.com/nfl_point_spreads.shtml"
    htm_pull(c, url)
    game_list = parse_file(c)
    player_choice(game_list)


main()
