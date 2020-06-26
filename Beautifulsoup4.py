# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:56:17 2020

@author: Bhuvi
"""

from bs4 import BeautifulSoup
import requests
import pandas  as pd


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table')[1]
rows = table.find_all('tr')
row_list = list()

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)

df_bs = pd.DataFrame(row_list,columns=['City','Country','Notes'])
df_bs.set_index('Country',inplace=True)
df_bs.to_csv('G:/beautifulsoup.csv')

