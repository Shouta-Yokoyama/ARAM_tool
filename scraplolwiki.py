# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:14:55 2023

@author: shouta yokoyama
"""

import requests, re, json
from bs4 import BeautifulSoup

url = "https://www.loljp-wiki.jp/wiki/?%A5%C7%A1%BC%A5%BF%A5%D9%A1%BC%A5%B9%2F%A5%C1%A5%E3%A5%F3%A5%D4%A5%AA%A5%F3"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

elems = soup.find_all("div", class_="intro")

output_data = []

for elem in elems:
    
    try:
        tmp = elem.find(title=re.compile("Champion/*"))
        name_list = tmp.get_text(",").split(",")
        img_url = elem.find("img").get("src")
        range_ = elem.get_text(",").split(",") 
        data={}
        data={"champion_name_ja" : name_list[0],
              "champion_name_en" : name_list[1].replace("(","").replace(")",""),
              "img_url" : "https://www.loljp-wiki.jp/wiki/"+img_url,
              "range":range_[4].replace("\n","").replace("(","").replace(")","")}
        print(data)
        output_data.append(data)
    except Exception as e:
        print(e)
        continue

with open("champion_list.json", "w") as f:
    json.dump(output_data, f)

print(elems[0].get_text(",").split(","))
pass