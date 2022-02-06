import requests
import pandas
import time
def downloading(offset, limit):
    url = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?offset={offset}&limit={limit}&sortField=devId.devShortCleanNm&sortType=asc&objStatus=0'
    res = requests.get(url)
    objects_data = res.json()
    list_id = objects_data.get('data').get('list')
    return list_id

offset_ = 1
limit_ = 5048
df = pandas.DataFrame()


k = 0
for j in range(2):
    list_id = downloading(offset_,limit_)
    for i in list_id:
        if k == 5000:
            objectID = i.get('objId')
            url1 = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{objectID}'
            res1 = requests.get(url1)
            objects_data1 = res1.json()
            objects_data1 = objects_data1.get('data')
            df = df.append(pandas.json_normalize(objects_data1), ignore_index=True)
            time.sleep(20)
            k = 0
        else:
            objectID = i.get('objId')
            url1 = f'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/{objectID}'
            res1 = requests.get(url1)
            objects_data1 = res1.json()
            objects_data1 = objects_data1.get('data')
            df = df.append(pandas.json_normalize(objects_data1), ignore_index=True)
            k += 1
    offset_ += 5048
df.to_excel('Задание 2.xlsx',index=False)
df.to_pickle('Задание 2.pickle')
df.to_csv('Задание 2.csv')