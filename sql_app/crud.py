from sqlalchemy.orm import Session

from . import models, schemas
import json

from .models import MyFile, MyCourse, MyLabel, MyJob, MyCourseField, MyCourseJob, MyField


# ==============文件====================

def create_file(db: Session, my_file: schemas.MyFileCreate):
    file_name = my_file.file_name
    file_description = my_file.file_description
    file_type = my_file.file_type
    file_labels = json.dumps(my_file.file_labels)
    duration = my_file.duration
    file_path = my_file.file_path

    file = MyFile(file_name=file_name,
                  file_description=file_description,
                  file_type=file_type,
                  file_labels=file_labels,
                  duration=duration,
                  file_path=file_path)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file


def get_file(db: Session, id_: int):
    return db.query(models.MyFile).filter(models.MyFile.id == id_).first()


def get_file_by_name(db: Session, file_name: str):
    return db.query(models.MyFile).filter(models.MyFile.file_name == file_name).first()


def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyFile).offset(skip).limit(limit).all()


def delete_file(db: Session, id_: int):
    file = get_file(db, id_)
    if file:
        db.delete(file)
        db.commit()
        return file
    return False


# ==============课程====================
def create_course(db: Session, my_course: schemas.MyCourseCreate):
    course_name = my_course.course_name
    course_description = my_course.course_description
    course_labels = json.dumps(my_course.course_labels)
    course_fields = json.dumps(my_course.course_fields)
    course_jobs = json.dumps(my_course.course_jobs)
    duration = my_course.duration
    content = json.dumps(my_course.content)
    file_id = my_course.file_id
    is_complete = my_course.is_complete
    course_type = my_course.course_type

    course = MyCourse(
        course_name=course_name,
        course_description=course_description,
        course_labels=course_labels,
        course_fields=course_fields,
        course_jobs=course_jobs,
        duration=duration,
        content=content,
        file_id=file_id,
        is_complete=is_complete,
        course_type=course_type)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def get_course(db: Session, id_: int):
    return db.query(models.MyCourse).filter(models.MyCourse.id == id_).first()


def get_course_by_name(db: Session, course_name: str):
    return db.query(models.MyCourse).filter(models.MyCourse.course_name == course_name).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyCourse).offset(skip).limit(limit).all()


def delete_course(db: Session, id_: int):
    course = get_course(db, id_)
    if course:
        db.delete(course)
        db.commit()
        return course
    return False


# ==============标签====================
def create_label(db: Session, my_label: schemas.MyLabelCreate):
    label_type = my_label.label_type
    value = my_label.value

    label = MyLabel(
        label_type=label_type,
        value=value
    )
    db.add(label)
    db.commit()
    db.refresh(label)
    return label


def get_label(db: Session, id_: int):
    return db.query(models.MyLabel).filter(models.MyLabel.id == id_).first()


def get_label_by_value(db: Session, value: str):
    return db.query(models.MyLabel).filter(models.MyLabel.value == value).first()


def get_labels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyLabel).offset(skip).limit(limit).all()


def delete_label(db: Session, id_: int):
    label = get_label(db, id_)
    if label:
        db.delete(label)
        db.commit()
        return label
    return False


# ==============职位====================

def create_job(db: Session, my_label: schemas.MyJobCreate):
    job_name = my_label.job_name
    job_description = my_label.job_description
    job = MyJob(
        job_name=job_name,
        job_description=job_description
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_job(db: Session, id_: int):
    return db.query(models.MyJob).filter(models.MyJob.id == id_).first()


def get_job_by_name(db: Session, job_name: str):
    return db.query(models.MyJob).filter(models.MyJob.job_name == job_name).first()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyJob).offset(skip).limit(limit).all()


def delete_job(db: Session, id_: int):
    job = get_job(db, id_)
    if job:
        db.delete(job)
        db.commit()
        return job
    return False


# ==============领域====================
def create_field(db: Session, my_field: schemas.MyFieldCreate):
    field_name = my_field.field_name
    field_description = my_field.field_description
    field = MyField(
        field_name=field_name,
        field_description=field_description
    )
    db.add(field)
    db.commit()
    db.refresh(field)
    return field


def get_field(db: Session, id_: int):
    return db.query(models.MyField).filter(models.MyField.id == id_).first()


def get_field_by_name(db: Session, field_name: str):
    return db.query(models.MyField).filter(models.MyField.field_name == field_name).first()


def get_fields(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyField).offset(skip).limit(limit).all()


def delete_field(db: Session, id_: int):
    field = get_field(db, id_)
    if field:
        db.delete(field)
        db.commit()
        return field
    return False


# =============课程领域====================
def create_course_field(db: Session, my_course_field: schemas.MyCourseFieldCreate):
    course_id = my_course_field.course_id
    field_id = my_course_field.field_id
    course_field = MyCourseField(
        course_id=course_id,
        field_id=field_id
    )
    db.add(course_field)
    db.commit()
    db.refresh(course_field)
    return course_field


def get_course_field(db: Session, id_: int):
    return db.query(models.MyCourseField).filter(models.MyCourseField.id == id_).first()


def get_course_field_by_ids(db: Session, course_id: int, field_id: int):
    return db.query(models.MyCourseField).filter(models.MyCourseField.course_id == course_id,
                                                 models.MyCourseField.field_id == field_id).first()


def get_course_field_course(db: Session, course_id: int):
    return db.query(models.MyCourseField).filter(models.MyCourseField.course_id == course_id).all()


def get_course_fields(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyCourseField).offset(skip).limit(limit).all()


def delete_course_field(db: Session, id_: int):
    course_field = get_course_field(db, id_)
    if course_field:
        db.delete(course_field)
        db.commit()
        return course_field
    return False


# ==============课程职位====================

def create_course_job(db: Session, my_course_job: schemas.MyCourseJobCreate):
    course_id = my_course_job.course_id
    job_id = my_course_job.job_id
    course_job = MyCourseJob(
        course_id=course_id,
        job_id=job_id
    )
    db.add(course_job)
    db.commit()
    db.refresh(course_job)
    return course_job


def get_course_job(db: Session, id_: int):
    return db.query(models.MyCourseJob).filter(models.MyCourseJob.id == id_).first()


def get_course_job_by_ids(db: Session, course_id: int, job_id: int):
    return db.query(models.MyCourseJob).filter(models.MyCourseJob.course_id == course_id,
                                               models.MyCourseJob.job_id == job_id).first()


def get_course_job_course(db: Session, course_id: int):
    return db.query(models.MyCourseJob).filter(models.MyCourseJob.course_id == course_id).all()


def get_course_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyCourseJob).offset(skip).limit(limit).all()


def delete_course_job(db: Session, id_: int):
    course_job = get_course_job(db, id_)
    if course_job:
        db.delete(course_job)
        db.commit()
        return course_job
    return False



# crud.py
# 添加新记录
# def create_file(db: Session, file: schemas.FileCreate):
#     db_file = models.FileDB(**file.dict())
#     db.add(db_file)
#     db.commit()
#     db.refresh(db_file)
#     return db_file
#
#
# # 查询记录，可选参数为用户id和文件类型
# def get_files(db: Session, user_id: int = -1, filetype: str = ''):
#     q = db.query(models.FileDB)
#     if user_id > 0:
#         q = q.filter(models.FileDB.owner_id == user_id)
#     if filetype != '':
#         q = q.filter(models.FileDB.type == filetype)
#     return q.all()
#
#
# # 查找单条记录
# def get_file(db: Session, file_id: int):
#     return db.query(models.FileDB).get(file_id)
#
#
# # 删除一条记录
# def drop_file(db: Session, file_id: int):
#     db_file = db.query(models.FileDB).get(file_id)
#     db.delete(db_file)
#     db.commit()
#     return db_file
#
#
# from sqlalchemy import func
#
#
# # 查看相同文件对应的记录数量
# def count_num_of_same_file(db: Session, file_md5: str):
#     return db.query(func.count(models.FileDB.id)).filter(models.FileDB.md5 == file_md5).scalar()
