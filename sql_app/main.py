from typing import List

from fastapi import Depends, FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
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


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create/file', description="创建文件")
def create_file(my_file: schemas.MyFileCreate,
                db: Session = Depends(get_db)
                ):
    file = crud.create_file(db, my_file)
    return {'fid':file.fid}


@app.post('/create/course', description="创建课程")
def create_course(my_course: schemas.MyCourseCreate,
                  db: Session = Depends(get_db)
                  ):
    course = crud.create_course(db, my_course)
    return {'cid':course.cid,}


@app.post('/create/label', description="创建标签")
def create_label(my_label: schemas.MyLabelCreate,
                 db: Session = Depends(get_db)
                 ):
    label = crud.create_label(db, my_label)
    return {'lid':label.lid}


@app.get('/get/{obj_type}', description="获取单个对象")
def get_object(obj_type: AllObject, xid: int, db: Session = Depends(get_db)):
    if obj_type == AllObject.file:
        return crud.get_file(db, xid)
    if obj_type == AllObject.course:
        return crud.get_course(db, xid)
    if obj_type == AllObject.label:
        return crud.get_label(db, xid)
    return {"message": "没有这种东西"}


@app.get('/get/many/{obj_type}', description="获取多个对象")
def get_many_object(
        obj_type: AllObject,
        kip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    if obj_type == AllObject.file:
        return crud.get_files(db, kip, limit)
    if obj_type == AllObject.course:
        return crud.get_courses(db, kip, limit)
    if obj_type == AllObject.label:
        return crud.get_labels(db, kip, limit)
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
