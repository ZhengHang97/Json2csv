import json
import csv
import os

lists = os.listdir("/home/g19tka08/Json2csv/iclr_2017")
lists.sort(key= lambda x:int(x[:-5]))
print(lists)
result = []
j = 0
for i in lists:
    filename = "/home/g19tka08/Json2csv/iclr_2017/" + str(i)
    json_data = [json.loads(line) for line in open(filename)][0]
    for data in json_data['reviews']:
        if 'comments' in data:
            if data['comments'] != '':
                if data['IS_META_REVIEW']:
                    result.append({
                        # 'index': str(j),
                        'comments': data['comments'],
                        'DECISION': str(1) if json_data['accepted'] else str(0)}
                    )
with open('iclr_decision_result.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=result[0].keys())
    writer.writeheader()
    for elem in result:
        writer.writerow(elem)
print(len(result))