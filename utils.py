import sys
from pathlib import Path

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
session_token = config["AOC_TOKEN"]


def get_input(day, year):
    puzzle_input = Path(f"./{year}/{day}/{day}.txt")
    print(f"Input Data: {puzzle_input}")

    if puzzle_input.is_file():
        return Path(puzzle_input).read_text(encoding="utf-8")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": "session=" + session_token}
    req = requests.get(url, headers=headers, timeout=5)
    if req.status_code == 200:
        puzzle_input.write_text(req.text, encoding="utf-8")
        return req.text
    else:
        sys.exit(
            f"/api/alerts response: {req.status_code}: {req.reason} \n{req.content}"
        )
