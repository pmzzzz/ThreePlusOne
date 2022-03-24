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
    name: str
    description: Optional[str] = None
    file_type: FileType = FileType.other
    labels: List[int] = []  # 标签的id
    duration: int
    path: Optional[str] = None


class MyFile(MyFileCreate):
    """
    文件
    """
    fid: Optional[int] = None


class MyCourseCreate(BaseModel):
    """
    课程
    """
    name: str  # 不可重复
    description: Optional[str] = None
    labels: List[int] = []  # 标签id
    fields: List[str] = []
    duration: Optional[int] = None
    content: List[int] = []  # 课程id
    file_id: Optional[int] = None  # 文件id
    is_complete: bool = False
    course_type: CourseType


class MyCourse(MyCourseCreate):
    """
    课程
    """
    cid: Optional[int] = None


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
    lid: Optional[int] = None
