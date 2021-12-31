import pandas as pd
from bs4 import BeautifulSoup
from datetime import date


file = open("./tsimple.html", "r", encoding='utf-8')
soup = BeautifulSoup(file)

d1 = list(dict())

cnt = 0
for row in soup.find_all('tr'):
    d = dict()
    for td in row.find_all('td'):
        if td['class'][0] == 'city':
            d['city'] = td.string
        if td['class'][0] == 'gu':
            d['gu'] = td.string
        if td['class'][0] == 'party':
            d['party'] = td.string
        if td['class'][0] == 'name':
            d['name'] = td.text.strip('\n')
        if td['class'][0] == 'hit':
            d['hit'] = td.string
        if td['class'][0] == 'date':
            # dateobj = datetime.strptime(td.string, '%Y-%m-%d')
            dateobj = date.fromisoformat(td.string)
            d['date'] = dateobj
        if td['class'][0] == 'crime':
            d['crime'] = td.string
    d1.append(d)
    del(d)
    cnt += 1
print ('Total ', cnt, ' dict created')


df = pd.DataFrame(d1)

print(df)


