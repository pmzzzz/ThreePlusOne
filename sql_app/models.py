from sqlalchemy import Boolean, Column,Integer, String

from .database import Base


class MyFile(Base):
    __tablename__ = "files"
    fid = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(128), index=True)
    description = Column(String(128))
    file_type = Column(String(128))
    labels = Column(String(128))
    duration = Column(Integer)
    path = Column(String(128))


class MyCourse(Base):
    __tablename__ = "courses"
    cid = Column(Integer, primary_key=True,
                 index=True,autoincrement=True)
    name = Column(String(128),index=True)
    description = Column(String(128))
    labels = Column(String(128))
    fields = Column(String(128))
    duration = Column(Integer)
    content = Column(String(128))
    file_id = Column(Integer)
    is_complete = Column(Boolean)
    course_type = Column(String(128))


class MyLabel(Base):
    __tablename__ = "labels"
    lid = Column(Integer, primary_key=True, index=True,autoincrement=True)
    label_type = Column(String(128), index=True)
    value = Column(String(128), index=True)
