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

    with open('table.html', 'wb+') as f:
        f.write(req.content)
    with open('table.html', 'rb') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    # soup = BeautifulSoup(req.content, "html.parser")
    results = soup.findAll("div", {"class": "main"})
    l = []
    for res in results:
        art = soup.find('article')
        for a in art:
            table = soup.find('table')
    rows = table.find_all('tr')
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Name", "Decimal"]
        list_of_rows = []
        for row in rows:
            cells = row.find_all('td')
            list_of_rows.append([cells])
        for row in list_of_rows:
            if len(row[0]) != 0:
                r_1 = row[0][1].text.strip()
                r_3 = row[0][3].text.strip()[9:-1]
                writer.writerow(field)
                if r_3 == '':
                    r_4 = row[0][3].text.strip()[:-1]
                    print('name: ', r_1, 'decimal: ', r_4)
                    writer.writerow([r_1, r_4])
                else:
                    print('name: ', r_1, 'decimal: ', r_3)
                    writer.writerow([r_1, r_3])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
