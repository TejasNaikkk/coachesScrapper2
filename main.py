import config
from souper import souper
from getDetails import getInfo
import pymongo

url = config.url
testURL = config.testURL
conn = config.mongoLocal

# Main soup
soup = souper(url)
h3s = soup.find_all('h3', class_='tb-heading')

# Create connection with mongo
client = pymongo.MongoClient(conn)
db = client["Scrapped"]
collection = db["Coaches2"]

def insertDataToMongo(payload, collection):
    collection.insert_one(payload)

users = []
for h3 in h3s:
    a = h3.find('a')
    href = a['href']
    users.append(href)

for user in users:
    payload = getInfo(user)
    insertDataToMongo(payload,collection)

client.close()