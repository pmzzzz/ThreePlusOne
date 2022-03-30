import requests
import json
import numpy as np
import pandas as pd
import json

url = "http://127.0.0.1:8000/create/file"


def create_file(file_name, file_description, file_type, file_labels, duration, file_path):
    payload = json.dumps({
        "file_name": file_name,
        "file_description": file_description,
        "file_type": file_type,
        "file_labels": file_labels,
        "duration": duration,
        "file_path": file_path
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


files = pd.read_excel('./测试文件列表.xlsx',sheet_name='文件')

vas = files.dropna(subset=['file_name']).fillna("---1").values


def jsonfiyit(x):
    if x == '---1':
        return []
    else:
        return json.loads(x)


for i in vas:
    file_name = i[0]
    file_description = i[1]
    file_type = i[2]
    file_labels = jsonfiyit(i[3])
    duration = i[4]
    file_path = i[5]
    create_file(file_name, file_description, file_type, file_labels, duration, file_path)
