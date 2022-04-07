from sqlalchemy import Boolean, Column, Integer, String, TEXT, Enum, ForeignKey

from .database import Base


class MyFile(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_name = Column(String(128), unique=True, nullable=False)
    file_description = Column(TEXT)
    file_type = Column(String(128))
    file_labels = Column(String(128))
    duration = Column(Integer)
    file_path = Column(String(128))


class MyCourse(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True,
                index=True, autoincrement=True)
    course_name = Column(String(128), index=True, unique=True, nullable=False)
    course_description = Column(TEXT)
    course_labels = Column(String(128))
    course_fields = Column(String(128))
    course_jobs = Column(String(128))
    duration = Column(Integer)
    content = Column(String(128))
    file_id = Column(Integer)
    is_complete = Column(Boolean)
    course_type = Column(String(128))


class MyLabel(Base):
    __tablename__ = "labels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label_type = Column(String(128), index=True)
    label_value = Column(String(128), index=True)


class MyJob(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    job_name = Column(String(128), index=True)
    job_description = Column(TEXT)


class MyField(Base):
    __tablename__ = "fields"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    field_name = Column(String(128), unique=True)
    field_description = Column(TEXT)


class MyCourseField(Base):
    __tablename__ = "course_fields"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    field_id = Column(Integer, index=True)
    course_id = Column(Integer, index=True)


class MyCourseJob(Base):
    __tablename__ = "course_jobs"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    job_id = Column(Integer, index=True)
    course_id = Column(Integer, index=True)


class MyCourseLabel(Base):
    __tablename__ = "course_labels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label_id = Column(Integer, index=True)
    course_id = Column(Integer, index=True)


class MyFileLabel(Base):
    __tablename__ = "file_labels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    label_id = Column(Integer, index=True)
    file_id = Column(Integer, index=True)


# class FileDB(Base):
#     __tablename__ = "physic_files"
#
#     id = Column(Integer, primary_key=True, index=True)
#     filename = Column(String, nullable=False)
#     md5 = Column(String, nullable=False)
# owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     type = Column(String)
