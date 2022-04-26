from datetime import datetime
from elasticsearch import Elasticsearch
import json
import warnings
warnings.filterwarnings("ignore")
es = Elasticsearch(hosts=['http://127.0.0.1:9200'])


def insert_course(course_id, document, index="coursefull"):
    res = es.index(index=index, id=course_id, document=document)
    return res


def search_course(kw: str):
    res = es.search(index="coursefull", typed_keys=['course'], body={
        "query": {
            "multi_match": {
                "query": kw,
                "fields": []
            }
        }
    })
    return dict(res)

if __name__ == '__main__':
    r = search_course('python')
    print(r)
    print(r['hits']['hits'][0]['_score'])