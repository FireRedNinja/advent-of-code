import sys
from pathlib import Path

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
session_token = config["AOC_TOKEN"]


def get_input(day, year):
    puzzle_input_dir = Path(f"./{year}/{day}/{day}.txt")
    test_input_dir = Path(f"./{year}/{day}/test_input.txt")
    print(f"Input Data: {puzzle_input_dir}")

    puzzle_input = None
    test_input = None
    if puzzle_input_dir.is_file():
        puzzle_input = Path(puzzle_input_dir).read_text(encoding="utf-8")
    
    if test_input_dir.is_file():
        test_input = Path(test_input_dir).read_text(encoding="utf-8")
    else:
        test_input_dir.write_text(encoding="utf-8")

    if not puzzle_input:
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        headers = {"Cookie": "session=" + session_token}
        req = requests.get(url, headers=headers, timeout=5)
        if req.status_code == 200:
            puzzle_input_dir.write_text(req.text, encoding="utf-8")
            puzzle_input = req.text
        else:
            sys.exit(
                f"/api/alerts response: {req.status_code}: {req.reason} \n{req.content}"
            )

    return (puzzle_input, test_input)