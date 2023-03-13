import json
import os
import requests
import urllib.request
f = open('convertcsv.json')
data = json.load(f)
URL = "https://raw.communitydragon.org/pbe/plugins/rcp-be-lol-game-data/global/default/v1/champion-tiles/"
for obj in data:
    folder_name = f'./{obj["name"]}'
    current_champion_id = obj["id"]
    try:
        os.mkdir(folder_name)
    except OSError as err:
        print(err)
    currentskinid = str(obj['id'])+'00'
    for x in range(5):
        print("Aktualny link do skina: ", currentskinid+str(x+1))
        url_full = URL+str(current_champion_id)+"/"+currentskinid+str(x+1)+".jpg"
        print(url_full)
        # urllib.request.urlretrieve(url_full, os.path.join(folder_name, currentskinid+".jpg"))
        response = requests.get(url_full)
        with open(f'{folder_name}/{currentskinid+str(x)}.jpg', 'wb') as f:
            f.write(response.content)

    print('Aktualne id:',obj['id'])
    # print('Aktualny link:', currentskinid)