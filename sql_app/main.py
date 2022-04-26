import json
from copy import copy
from typing import List
from . import search
from fastapi import Depends, FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from .schemas import AllObject

from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.description = "3+1课程体系API"
app.title = "3+1课程体系"

templates = Jinja2Templates(directory="templates")
app.mount('/assets', StaticFiles(directory='assets'), name='assets')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


# @app.get("/search")
# async def search_course(kw: str, request: Request):
#     # 进行搜索，将满足条件的id返回
#     res = search.search_course(kw)
#     return JSONResponse(res)

@app.get("/search")
async def search_course(kw: str, request: Request):
    # 进行搜索，将满足条件的id返回
    res = search.search_course(kw)
    return templates.TemplateResponse('搜索结果.html', {'request': request, 'res': json.dumps(res)})


@app.get('/show/course', description="查看课程")
def show_course(id: int, request: Request, db: Session = Depends(get_db)):
    course = crud.get_course(db, id)
    x = dict(course.__dict__)
    x.pop('_sa_instance_state')

    data = get_all_course(db=db, cid=id, data=[])
    data[0]['itemStyle']['color'] = '#f6a21c'
    data[0]['symbolSize'] = 30
    data[0]['label']['show'] = True
    datamap = {}
    for i, j in enumerate(data):
        datamap[j['id']] = i
    links = []
    for ii, i in enumerate(data):
        cid = i['id']
        course1 = crud.get_course(db, cid)
        content = course1.content
        content = json.loads(content)
        for j in content:
            links.append({'source': ii, 'target': datamap[j]})
    print(data)
    print(links)
    return templates.TemplateResponse('课程简介.html', {'request': request, 'res': json.dumps(x), 'data': json.dumps(data),
                                                    'links': json.dumps(links)})


@app.post('/create/file', description="创建文件")
def create_file(my_file: schemas.MyFileCreate,
                db: Session = Depends(get_db)
                ):
    file = crud.create_file(db, my_file)
    return {'id': file.id}


@app.post('/create/course', description="创建课程")
def create_course(my_course: schemas.MyCourseCreate,
                  db: Session = Depends(get_db)
                  ):
    course = crud.create_course(db, my_course)
    try:
        document = {}
        course_id = course.id
        description = course.course_description
        name = course.course_name
        jobs = json.loads(course.course_jobs)
        fields = json.loads(course.course_fields)
        labels = json.loads(course.course_labels)
        content = json.loads(course.content)
        is_complete = course.is_complete
        document['course_id'] = course_id
        document['description'] = description
        document['name'] = name
        if jobs:
            jobs = ' '.join([crud.get_job(db, i).job_name for i in jobs])
            document['jobs'] = jobs
        if fields:
            fields = ' '.join([crud.get_field(db, i).field_name for i in fields])
            document['fields'] = fields
        if labels:
            labels = ' '.join([crud.get_label(db, i).value for i in labels])
            document['labels'] = labels
        if content:
            child_name = ' '.join([crud.get_course(db, i).course_name for i in content])
            document['child_name'] = child_name
        document['is_complete'] = int(is_complete)
        search.insert_course(course_id=course_id, document=document)
    except Exception as e:
        print(e)
    return {'id': course.id}


@app.post('/create/label', description="创建标签")
def create_label(my_label: schemas.MyLabelCreate,
                 db: Session = Depends(get_db)
                 ):
    label = crud.create_label(db, my_label)
    return {'id': label.id}


@app.post("/create/field", description="创建领域")
def create_field(my_field: schemas.MyFieldCreate,
                 db: Session = Depends(get_db)):
    field = crud.create_field(db, my_field)
    return {'id': field.id}


@app.post('/create/job', description="创建职业")
def create_job(my_job: schemas.MyJobCreate,
               db: Session = Depends(get_db)):
    job = crud.create_job(db, my_job)
    return {'id': job.id}


@app.post("/create/course_field", description="创建课程领域")
def create_course_field(my_course_field: schemas.MyCourseFieldCreate,
                        db: Session = Depends(get_db)):
    course_field = crud.create_course_field(db, my_course_field)
    return {'id': course_field.id}


@app.post("/create/course_job", description="创建课程职业")
def create_course_job(my_course_job: schemas.MyCourseJobCreate,
                      db: Session = Depends(get_db)):
    course_job = crud.create_course_job(db, my_course_job)
    return {'id': course_job.id}


@app.post("/create/course_label", description="创建课程标签")
def create_course_label(my_course_label: schemas.MyCourseLabelCreate,
                        db: Session = Depends(get_db)):
    course_label = crud.create_course_label(db, my_course_label)
    return {'id': course_label.id}


@app.post("/create/file_label", description="创建文件标签")
def create_file_label(my_file_label: schemas.MyFileLabelCreate,
                      db: Session = Depends(get_db)):
    file_label = crud.create_file_label(db, my_file_label)
    return {'id': file_label.id}


@app.get('/get/{obj_type}', description="获取单个对象")
def get_object(obj_type: AllObject, xid: int, db: Session = Depends(get_db)):
    """

    :param obj_type: 获取对象的类型
    :param xid: 该实体的id
    :param db: 数据库
    :return: 一个实体
    """
    if obj_type == AllObject.file:
        return crud.get_file(db, xid)
    if obj_type == AllObject.course:
        return crud.get_course(db, xid)
    if obj_type == AllObject.label:
        return crud.get_label(db, xid)
    if obj_type == AllObject.field:
        return crud.get_field(db, xid)
    if obj_type == AllObject.job:
        return crud.get_job(db, xid)
    if obj_type == AllObject.course_field:
        return crud.get_course_field(db, xid)
    if obj_type == AllObject.course_job:
        return crud.get_course_job(db, xid)
    if obj_type == AllObject.course_label:
        return crud.get_course_label(db, xid)
    if obj_type == AllObject.file_label:
        return crud.get_file_label(db, xid)
    return {"message": "没有这种东西"}


@app.get('/get/many/{obj_type}', description="获取多个对象")
def get_many_object(
        obj_type: AllObject,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    if obj_type == AllObject.file:
        return crud.get_files(db, skip, limit)
    if obj_type == AllObject.course:
        return crud.get_courses(db, skip, limit)
    if obj_type == AllObject.label:
        return crud.get_labels(db, skip, limit)
    if obj_type == AllObject.field:
        return crud.get_fields(db, skip, limit)
    if obj_type == AllObject.job:
        return crud.get_jobs(db, skip, limit)
    if obj_type == AllObject.course_field:
        return crud.get_course_fields(db, skip, limit)
    if obj_type == AllObject.course_job:
        return crud.get_course_jobs(db, skip, limit)
    if obj_type == AllObject.course_label:
        return crud.get_course_labels(db, skip, limit)
    if obj_type == AllObject.file_label:
        return crud.get_file_labels(db, skip, limit)
    return {"message": "没有这种东西"}


## 权限？
@app.delete('/delete/{obj_type}', description="删除单个对象")
def delete_object(obj_type: AllObject, xid: int, db: Session = Depends(get_db)):
    if obj_type == AllObject.file:
        return crud.delete_file(db, xid)
    if obj_type == AllObject.course:
        return crud.delete_course(db, xid)
    if obj_type == AllObject.label:
        return crud.delete_label(db, xid)
    if obj_type == AllObject.field:
        return crud.delete_field(db, xid)
    if obj_type == AllObject.job:
        return crud.delete_job(db, xid)
    if obj_type == AllObject.course_field:
        return crud.delete_course_field(db, xid)
    if obj_type == AllObject.course_job:
        return crud.delete_course_job(db, xid)
    if obj_type == AllObject.course_label:
        return crud.delete_course_label(db, xid)
    if obj_type == AllObject.file_label:
        return crud.delete_file_label(db, xid)
    return {"message": "没有这种东西"}


# TODO: 上传文件
@app.post('/uploadfile', description="上传文件")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.post("/uploadfiles/")
async def create_upload_files(
        files: List[UploadFile] = File(...)
):
    return {"filenames": [file.filename for file in files]}


# ######### 第二层应用 ######## 用户

@app.get("/full_course", description="获取一层课程，以及它的子课程，前端可根据子课程的id来向下人查找，减轻后端递归的开销")
def get_full_course(cid: int, db: Session = Depends(get_db)):
    course = crud.get_course(db, cid)
    content = course.content
    content = json.loads(content)
    content = [crud.get_course(db, i) for i in content]
    return {"me": course, "content": content}


# f6a21c
def get_all_course(cid: int, db: Session = Depends(get_db), data=None):
    if data is None:
        data = []
    course = crud.get_course(db, cid)
    content = course.content
    content = json.loads(content)
    data1 = {'id': course.id,
             'name': course.course_name,
             'symbolSize': 20,
             'value': course.duration,
             'itemStyle': {
                 'color': '#13c2c2',
                 'opacity': 0.8,
             },
             'label': {
                 'show': False,
             }
             }
    data.append(data1)
    if content:
        for i in content:
            get_all_course(i, db, data)
    else:
        return data
    return data


if __name__ == '__main__':
    xx = get_all_course(cid=40, data=[])
    print(xx)
