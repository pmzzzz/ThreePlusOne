from datetime import datetime
from elasticsearch import Elasticsearch


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
    return res

if __name__ == '__main__':
    search_course('hh')