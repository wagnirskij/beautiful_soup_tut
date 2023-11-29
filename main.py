import pandas as pd
from bs4 import BeautifulSoup

# import lxml <--- certain sites use this (then also put it into the soup as parser)

with open(file="F:/100DAYS/day45_beautiful_soup/website.html", mode="r", encoding="utf-8") as html_file:
    lines = html_file.read()


soup = BeautifulSoup(lines, "html.parser")

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get("href"))