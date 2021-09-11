import json
import csv
import os

lists = os.listdir("/home/g19tka08/Json2csv/acl_2017")
lists.sort(key=lambda x: int(x[:-5]))
print(lists)
result = []

for i in lists:
    filename = "/home/g19tka08/Json2csv/acl_2017/" + str(i)
    json_data = [json.loads(line) for line in open(filename)][0]['reviews']
    for data in json_data:
        result.append({
            'SUBSTANCE': data['SUBSTANCE'] if 'SUBSTANCE' in data else str(0),
            'CLARITY': data['CLARITY'] if 'CLARITY' in data else str(0),
            'APPROPRIATENESS': data['APPROPRIATENESS'] if 'APPROPRIATENESS' in data else str(0),
            'IMPACT': data['IMPACT'] if 'IMPACT' in data else str(0),
            'COMPARISON': data['MEANINGFUL_COMPARISON'] if 'MEANINGFUL_COMPARISON' in data else str(0),
            'ORIGINALITY': data['ORIGINALITY'] if 'ORIGINALITY' in data else str(0),
            'SOUNDNESS': data['SOUNDNESS_CORRECTNESS'] if 'SOUNDNESS_CORRECTNESS' in data else str(0),
            'comments': data['comments'] if 'comments' in data else str(0),
            'RECOMMENDATION': data['RECOMMENDATION'] if 'RECOMMENDATION' in data else str(0),
        })
with open('acl_result.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=result[0].keys())
    writer.writeheader()
    for elem in result:
        writer.writerow(elem)
print(len(result))