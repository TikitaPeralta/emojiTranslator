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
        # field = ["Name", "Decimal"]
        list_of_rows = []
        for row in rows:
            cells = row.find_all('td')
            list_of_rows.append([cells])
        for row in list_of_rows:
            if len(row[0]) != 0:
                name = row[0][1].text.strip()
                decimal = row[0][3].text.strip()[9:-1]
                corrected_decimal = row[0][3].text.strip()[:-1]
                if 'type-' not in name and ',' not in name:
                    if '≊' in name:
                        shorter_name = name.split('≊')
                        if decimal == '':
                            writer.writerow([shorter_name[0], corrected_decimal])
                        else:
                            writer.writerow([shorter_name[0], decimal])
                    else:
                        if decimal == '':
                            writer.writerow([name, corrected_decimal])
                        else:
                            writer.writerow([name, decimal])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
