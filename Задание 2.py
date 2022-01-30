import requests
offset_ = 2001
limit_ = 1000
url = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?offset={offset_}&limit={limit_}&sortField=devId.devShortCleanNm&sortType=asc&objStatus=0'
res = requests.get(url)
objects_data = res.json()
list_id = objects_data.get('data').get('list')
x = []
for i in list_id:
    x.append(i.get('objId'))
print(type(x[1]))

url1 = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{x[1]}'
res1 = requests.get(url1)
objects_data1 = res1.json()
