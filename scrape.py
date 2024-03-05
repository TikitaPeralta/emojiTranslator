import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
import csv

URL = 'https://www.quackit.com/character_sets/emoji/emoji_v3.0/unicode_emoji_v3.0_characters_all.cfm'
try:
    req = requests.get(URL)
    if req.status_code == 200:
        # print(req.text)
        print("Success!")
    else:
        print(f"Failed with status code: {req.status_code}")
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.findAll("div", {"class": "main"})
    # print(results)
    l = []
    for res in results:
        art = soup.find('article')
        for a in art:
            table = soup.find('table')
    rows = table.find_all('tr')
    list_of_rows = []
    # print(rows)
    for row in rows:
        cells = row.find_all('td')
        list_of_rows.append([cells])
        # print(list_of_rows)
    for row in list_of_rows:
        print(row[0])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


# for row in list_of_rows:
#     print(row)

# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     field = ["Name", "Decimal"]
    
#     writer.writerow(field)
#     for c in rows:
#         writer.writerow([f'{name}'.lower, f'{decimal}'])