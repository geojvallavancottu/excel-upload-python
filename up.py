import csv
import json
import sys
import requests

heads = {'Content-Type': 'application/json', 'Accept': 'application/json'}
with open('sample1.csv', mode ='r') as file:   
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        print(lines['Part'])
        data = {
            'name': lines['Name'],
            'gender': lines['Sex'],
            'age': lines['Age'],
            'house_no': lines['House'],
            'section_address': lines['Section'],
            'relation_name': lines['Relative'],
            'relation_type': lines['Reln'],
            'part_no': lines['Part'],
            'serial_no': lines['Serial'],
            'voter_status': lines['Status'],
            'voter_id' : lines['EPIC'],
            'ward': lines['Ward'],
        }
        x = requests.post("https://umapathysrinivasgowda.com/uploadVoterFileApi", data=json.dumps(data), headers=heads)
        print(x.status_code)
        print(data);
        # sys.exit()