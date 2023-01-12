import csv
import json
import sys
import requests
import time
import datetime as dt
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='voter',
    auth_plugin='mysql_native_password'
    )
vals = []
sql = "INSERT INTO voters (`name`, `age`, `house_no`, `relation_name`, `part_no`, `serial_no`,`voter_id`) VALUES (%s, %s,%s, %s,%s, %s,%s)"
mycursor = mydb.cursor()
start = time.time()
heads = {'Content-Type': 'application/json', 'Accept': 'application/json'}
with open('s1.csv', mode ='r') as file:   
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
        val = (lines['Name'],  lines['Age'],lines['House'],lines['Relative'], lines['Part'], lines['Serial'], lines['EPIC'])
        vals.append(val)
        # x = requests.post("http://localhost:8000/uploadVoterFileApi", data=json.dumps(data), headers=heads)
        # print(x.status_code)
        print(val);

mycursor.executemany(sql, vals)
            # print(vals)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

        # sys.exit()
end = time.time()
print("Took {} seconds .".format(end - start))