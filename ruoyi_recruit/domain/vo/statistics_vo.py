from pydantic import BaseModel


class statistics_vo(BaseModel):
    """
    统计总数对象
    """
    value: int
    name: str
