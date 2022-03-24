from sqlalchemy.orm import Session

from . import models, schemas
import json

from .models import MyFile, MyCourse, MyLabel


# ==============文件====================

def create_file(db: Session, my_file: schemas.MyFileCreate):
    name = my_file.name
    description = my_file.description
    file_type = my_file.file_type
    labels = json.dumps(my_file.labels)
    duration = my_file.duration
    path = my_file.path

    file = MyFile(name=name,
                  description=description,
                  file_type=file_type,
                  labels=labels,
                  duration=duration,
                  path=path)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file


def get_file(db: Session, fid: int):
    return db.query(models.MyFile).filter(models.MyFile.fid == fid).first()


def get_file_by_name(db: Session, name: str):
    return db.query(models.MyFile).filter(models.MyFile.name == name).first()


def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyFile).offset(skip).limit(limit).all()


def delete_file(db: Session, fid: int):
    file = get_file(db, fid)
    if file:
        db.delete(file)
        db.commit()
        return file
    return False


# ==============课程====================
def create_course(db: Session, my_course: schemas.MyCourse):
    name = my_course.name
    description = my_course.description
    labels = json.dumps(my_course.labels)
    fields = json.dumps(my_course.fields)
    duration = my_course.duration
    content = json.dumps(my_course.content)
    file_id = my_course.file_id
    is_complete = my_course.is_complete
    course_type = my_course.course_type

    course = MyCourse(
        name=name,
        description=description,
        labels=labels,
        fields=fields,
        duration=duration,
        content=content,
        file_id=file_id,
        is_complete=is_complete,
        course_type=course_type)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def get_course(db: Session, cid: int):
    return db.query(models.MyCourse).filter(models.MyCourse.cid == cid).first()


def get_course_by_name(db: Session, name: str):
    return db.query(models.MyCourse).filter(models.MyCourse.name == name).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyCourse).offset(skip).limit(limit).all()


def delete_course(db: Session, cid: int):
    course = get_course(db, cid)
    if course:
        db.delete(course)
        db.commit()
        return course
    return False


# ==============标签====================
def create_label(db: Session, my_label: schemas.MyLabel):
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


def get_label(db: Session, lid: int):
    return db.query(models.MyLabel).filter(models.MyLabel.lid == lid).first()


def get_label_by_value(db: Session, value: str):
    return db.query(models.MyLabel).filter(models.MyLabel.value == value).first()


def get_labels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyLabel).offset(skip).limit(limit).all()


def delete_label(db: Session, lid: int):
    label = get_label(db, lid)
    if label:
        db.delete(label)
        db.commit()
        return label
    return False
