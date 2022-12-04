import sys
from datetime import datetime

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
session_token = config["AOC_TOKEN"]


data = None
url = "https://adventofcode.com/2022/leaderboard/private/view/212116.json"
headers = {"Cookie": "session=" + session_token}
r = requests.get(url, headers=headers)

if r.status_code == 200:
    data = r.json()
else:
    sys.exit(f"/api/alerts response:{r.status_code}: {r.reason} \n{r.content}")

me = data["members"]["710489"]

print("My's Stats:")
for key in me["completion_day_level"]:
    print(f"\tDay {key}:")
    for star in me["completion_day_level"][key]:
        star_time = datetime.fromtimestamp(
            me["completion_day_level"][key][star]["get_star_ts"]
        )
        print(f"\t\tStar {star} Time: {star_time}")
