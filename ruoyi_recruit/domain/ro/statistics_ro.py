from pydantic import BaseModel

class statistics_ro(BaseModel):
    """
    统计总数对象
    """
    value: int
    name: str
