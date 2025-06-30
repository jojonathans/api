import requests 
from bs4 import BeautifulSoup 
import csv


BASE_URL = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2015'
response = requests.get(BASE_URL)
items = response.json()

result= []
for item in items : 
    title   = item.get("title")
    year    = item.get("year")
    awards  = item.get("awards")

    result.append({
        "Title" : title,
        "Year" : year , 
        "Awards" : awards
    })

for item in result: 
    print(f"Title :  {item['Title']} - Year :  {item['Year']} - Awards :  {item['Awards']} ")

