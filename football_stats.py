from bs4 import BeautifulSoup
import requests
import os
import json


class FParams:
    def __init__(self):
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
    player_stats = soup.find_all('tr', {"class": "TableBase-bodyTr"})
    num, list_of_players = 0, []
    for players in player_stats:
        player_stat_cols = players.find_all('td')
        player_stat_ttl_td = [ele.text.strip().replace("\\n", "") for ele in player_stat_cols]
        player_stat_info = [ele for ele in player_stat_cols]
        player_stat_info = player_stat_info[0]
        player_name_elem = player_stat_info.find('a', {'class': ""})
        player_pos_elem = player_stat_info.find('span', {'class': "CellPlayerName-position"})
        player_team_elem = player_stat_info.find('span', {'class': "CellPlayerName-team"})
        players_touchdown_elem = player_stat_ttl_td[12]
        if num < 21:
            jspn_str = {"Name": player_name_elem.text.strip(),
                        "Position": player_pos_elem.text.strip(),
                        "Team": player_team_elem.text.strip(),
                        "Touchdown Amount": players_touchdown_elem}
            json_out = json.dumps(jspn_str)
            list_of_players.append(json_out)
            num += 1
    for x in list_of_players: print(x)



def main():
    htm_pull(FParams)
    parse_file(FParams)


main()
