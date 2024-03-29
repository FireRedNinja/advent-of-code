import shutil
from datetime import datetime
from pathlib import Path
from utils import get_input

YEAR = datetime.today().year
DAY = datetime.today().day

year_input = input(f"Enter Year [{YEAR}]: ")
day_input = input(f"Enter Day [{DAY}]: ")

if year_input != "":
    YEAR = year_input
if day_input != "":
    DAY = day_input

path = Path(f"./{YEAR}/{DAY}")
print(f"Creating files in {path}")
if not path.exists():
    path.mkdir(parents=True)
    shutil.copy("./0/0.py", path.joinpath(f"{DAY}.py"))
    get_input(DAY, YEAR)

print("Done!")
