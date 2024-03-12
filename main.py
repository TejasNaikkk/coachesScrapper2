import config
from souper import souper

url = config.url


soup = souper(url)
h3s = soup.find_all('h3', class_='tb-heading')


users = []

for h3 in h3s:
    a = h3.find('a')
    href = a['href']
    users.append(href)

print(len(users))