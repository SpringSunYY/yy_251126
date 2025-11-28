from typing import List

from pydantic import BaseModel


class statistics_vo(BaseModel):
    """
    统计总数对象
    """
    value: int
    name: str


class relation_statistics_vo(BaseModel):
    """
    关系统计对象
      {
    "name": "企业岗位要求",
    "value": 0,
    "list": [
      {
        "name": "10000人以上", "value": 10,
        "list": [
    """
    name: str
    value: int
    children: List['relation_statistics_vo']

    class Config:
        # 允许前向引用
        arbitrary_types_allowed = True
