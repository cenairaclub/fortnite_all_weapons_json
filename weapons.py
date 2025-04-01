import requests
from bs4 import BeautifulSoup
import json

with open("Silahlar - Fortnite.GG.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

weapons = []
tables = soup.find_all('table')
index = 1  # Index numarası için sayaç

for table in tables:
    rows = table.find_all('tr')[1:]  # İlk satırı atlayarak başla
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 8:  # En az 8 sütun olduğundan emin ol
            weapon = {
                'index': index,  # Index numarasını ekle
                'rarity': cols[1].text.strip(),
                'DPS': cols[2].text.strip(),
                'damage': cols[3].text.strip(),
              #  'body': cols[4].text.strip(),
                'fire_rate': cols[5].text.strip(),
                'magazine': cols[6].text.strip(),
              #  'reload': cols[7].text.strip()
            }
            weapons.append(weapon)
            index += 1  # Her silah için index'i bir artır

with open("weapons.json", "w", encoding="utf-8") as f:
    json.dump(weapons, f, ensure_ascii=False, indent=2)

print(f"{len(weapons)} silah JSON dosyasına kaydedildi.") 