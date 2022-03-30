from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class Allow(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"


class AllObject(str, Enum):
    file = "file"
    course = "course"
    label = "label"
    user = "user"
    field = "field"
    job = "job"
    course_field = "course_field"
    course_job = "course_job"


class FileType(str, Enum):
    """
    文件类型
    """
    link = 'link'
    doc = 'doc'
    video = 'video'
    audio = 'audio'
    image = 'image'
    other = 'other'


class CourseType(str, Enum):
    """
    课程类型
    """
    cognition = 'cognition'  # 认知
    General_ability = 'General_ability'  # 通用能力
    specialty = 'specialty'  # 专业


class MyFileCreate(BaseModel):
    file_name: str
    file_description: Optional[str] = None
    file_type: FileType = FileType.other
    file_labels: List[int] = []  # 标签的id
    duration: int
    file_path: Optional[str] = None


class MyFile(MyFileCreate):
    """
    文件
    """
    id: Optional[int] = None


class MyCourseCreate(BaseModel):
    """
    课程
    """
    course_name: str  # 不可重复
    course_description: Optional[str] = None
    course_labels: List[int] = []  # 标签id
    course_fields: List[int] = []
    course_jobs: List[int] = []
    duration: Optional[int] = None
    content: List[int] = []  # 课程id
    file_id: Optional[int] = None  # 文件id
    is_complete: bool = False
    course_type: CourseType


class MyCourse(MyCourseCreate):
    """
    课程
    """
    id: Optional[int] = None


class MyLabelCreate(BaseModel):
    """
    标签
    """
    label_type: str
    value: str


class MyLabel(MyLabelCreate):
    """
    标签
    """
    id: Optional[int] = None


class MyJobCreate(BaseModel):
    """
    工作
    """
    job_name: str
    job_description: Optional[str] = None


class MyJob(MyJobCreate):
    """
    工作
    """
    id: Optional[int] = None


class MyFieldCreate(BaseModel):
    field_name: str
    field_description: Optional[str] = None


class MyField(MyFieldCreate):
    id: int


class MyCourseFieldCreate(BaseModel):
    course_id: int
    field_id: int


class MyCourseField(MyCourseFieldCreate):
    id: int


class MyCourseJobCreate(BaseModel):
    course_id: int
    job_id: int


class MyCourseJob(MyCourseJobCreate):
    id: int


class FileBase(BaseModel):
    md5: str
    filename: str
    owner_id: int
    type: Optional[str]


class FileCreate(FileBase):  # 用于向数据库提交新记录
    pass


class FileInfo(FileBase):  # 用于与数据库查阅结果对接
    id: int

    class Config:
        orm_mode = True
