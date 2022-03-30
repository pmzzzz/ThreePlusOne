import requests
import json
import numpy as np
import pandas as pd
import json

url = "http://127.0.0.1:8000/create/course"


def flage(x):
    if x:
        return True
    else:
        return False


def jsonfiyit(x):
    if x == '---1':
        return []
    else:
        return json.loads(x)

def fid(x):
    if x == '---1':
        return None
    else:
        return x
def create_course(course_name, course_description,
                  course_labels, course_fields, course_jobs, duration, content,
                  file_id,
                  is_complete, course_type):
    payload = json.dumps({
        "course_name": course_name,
        "course_description": course_description,
        "course_labels": course_labels,
        "course_fields": course_fields,
        "course_jobs": course_jobs,
        "duration": duration,
        "content": content,
        "file_id": file_id,
        "is_complete": is_complete,
        "course_type": course_type
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


files = pd.read_excel('./测试文件列表.xlsx', sheet_name='课程')

vas = files.dropna(subset=['course_name']).fillna("---1").values

for i in vas:
    print(i)
    course_name = i[0]
    course_description = i[1]
    course_labels = jsonfiyit(i[2])
    course_fields = jsonfiyit(i[3])
    course_jobs = jsonfiyit(i[4])
    duration = i[5]
    content = jsonfiyit(i[6])
    file_id = fid(i[7])
    is_complete = flage(i[8])
    course_type = i[9]
    create_course(course_name, course_description,
                  course_labels, course_fields, course_jobs, duration, content,
                  file_id,
                  is_complete, course_type)
