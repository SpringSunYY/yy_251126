from pydantic import BaseModel

class statistics_ro(BaseModel):
    """
    统计总数对象
    """
    value: int
    name: str

class statistics_business_ro(BaseModel):
    """
    统计列表对象
    """
    value: int
    business: str
    skill: str

class statistics_salary_ro(BaseModel):
    """
    统计列表对象
    """
    value: int
    name: str
    min_salary: float
    max_salary: float
    avg_salary: float
