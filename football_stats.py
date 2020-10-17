from bs4 import BeautifulSoup
import requests
import os
import json


class FParams:
    def __init__(self):
        import os
        if os.name == 'nt':
            self.current_working_folder = "\\website_download\\football_stats\\"
        else:
            self.current_working_folder = "/website_download/football_stats/"
        self.current_working_file = "football_stats.htm"

    def LocalPath(self):
        return os.getcwd() + self.current_working_folder

    def TotalPath(self):
        p = self.LocalPath() + self.current_working_file
        return str(p)

    def SearchDir(self):
        olen = os.listdir(self.LocalPath())
        return olen


"""def file_params():


    cwfolder = "/website_download/football_stats/"
    cwfile = "football_stats.htm"

    path = os.getcwd() + cwfolder
    total_path = path + cwfile

    search_dir = os.listdir(path)"""


def htm_pull(files):
    f = files()
    if len(f.SearchDir()) == 0:
        print(' dir empty')
        r = requests.get("https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers")
        open(f.Localpath(), 'xb').write(r.content)
    else:
        print('items in dir, skipping download')
    return


def parse_file(files):
    f = files()
    r = open(f.TotalPath(), encoding="utf-8")

    soup = BeautifulSoup(r, 'html.parser')
    d = soup.find_all('tr', {"class": "TableBase-bodyTr"})
    num = 0
    for dd in d:
        cols = dd.find_all('td')
        ddd = [ele.text.strip().replace("\\n", "") for ele in cols]
        dddd = [ele for ele in cols]
        dddd= dddd[0]
        player_name_elem = dddd.find('a', {'class': ""})
        player_pos_elem = dddd.find('span', {'class': "CellPlayerName-position"})
        player_team_elem = dddd.find('span', {'class': "CellPlayerName-team"})
        players_touchdown_elem = ddd[12]
        if player_name_elem is not None and num < 21:

            print("Name:            ",player_name_elem.text.strip())
            print("Position:        ",player_pos_elem.text.strip())
            print("Team:             ",player_team_elem.text.strip())
            print("Touchdown Amount:",players_touchdown_elem)
            print("_____________________________________________________________________")
            num+=1


def main():
    htm_pull(FParams)
    parse_file(FParams)


main()
