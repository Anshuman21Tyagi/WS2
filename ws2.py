from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(START_URL)

soup = BeautifulSoup(page.text,'html.parser')
star_table = soup.find_all('table')
temp = []
table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)

star_names = []
distance1 = []
mass = []
radius = []

for i in range(1,len(temp)):
    star_names.append(temp[i][0])
    distance1.append(temp[i][5])
    radius.append(temp[i][8])
    mass.append(temp[i][7])

df = pd.DataFrame(list(zip(
    star_names, 
    distance1, 
    mass, 
    radius)), 
    columns =['star_names','distance1','mass', 'radius']
    )

df.to_csv('stars2.csv')