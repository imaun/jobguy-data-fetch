import requests
import json

def saveToFile(data, mode):
    with open("companies.json", mode, encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print("Starting...")
index = 1
apiUrl = 'http://api.jobguy.ir/public/company/list/?size=50&index=' + str(index) + '&order_by=HOTTEST'
print("Fetching page " + str(index))
res = requests.get(apiUrl)
saveToFile(res.json(), "w")

while(res.status_code == 200):
    index +=1
    apiUrl = 'http://api.jobguy.ir/public/company/list/?size=50&index=' + str(index) + '&order_by=HOTTEST'
    print("Fetching page " + str(index))
    res = requests.get(apiUrl)
    if(res.status_code == 200):
        saveToFile(res.json(), "a")

print('finished successfully.')