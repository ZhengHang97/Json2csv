import json
import csv
import os

lists = os.listdir("/home/g19tka08/Json2csv/iclr_2017")
lists.sort(key= lambda x:int(x[:-5]))
print(lists)
result = []

for i in lists:
    filename = "/home/g19tka08/Json2csv/iclr_2017/" + str(i)
    json_data = [json.loads(line) for line in open(filename)][0]['reviews']
    for data in json_data:
        if 'CLARITY' in data:
            if data['comments'] != '':
                result.append({
                    'CLARITY': data['CLARITY'],
                    # 'ORIGINALITY': data['ORIGINALITY'] if 'ORIGINALITY' in data else str(0),
                    # 'CORRECTNESS': data['CORRECTNESS'] if 'CORRECTNESS' in data else str(0),
                    # 'COMPARISON': data['COMPARISON'] if 'COMPARISON' in data else str(0),
                    # 'SUBSTANCE': data['SUBSTANCE'] if 'SUBSTANCE' in data else str(0),
                    # 'IMPACT': data['IMPACT'] if 'IMPACT' in data else str(0),
                    'comments': data['comments']
                })

with open('iclr_clarity_result.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=result[0].keys())
    writer.writeheader()
    for elem in result:
        writer.writerow(elem)
print(len(result))