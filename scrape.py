import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

URL = 'https://www.w3schools.com/charsets/ref_emoji_smileys.asp'
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
results = soup.findAll("div", {"class": ""})