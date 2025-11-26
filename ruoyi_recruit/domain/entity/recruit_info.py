# -*- coding: utf-8 -*-
# @Author  : YY
# @FileName: recruit_info.py
# @Time    : 2025-11-26 18:15:09

from typing import Optional, Annotated
from pydantic import Field, BeforeValidator
from ruoyi_common.base.model import BaseEntity
from ruoyi_common.base.transformer import str_to_int
from ruoyi_common.base.schema_excel import ExcelField
from ruoyi_common.base.schema_vo import VoField


class recruit_info(BaseEntity):
    """
    招聘信息表对象
    """
    # 编号
    recruit_id: Annotated[
        Optional[int],
        BeforeValidator(str_to_int),
        Field(default=None, description="编号"),
        VoField(query=True),
        ExcelField(name="编号")
    ]
    # 岗位
    post: Annotated[
        Optional[str],
        Field(default=None, description="岗位"),
        VoField(query=True),
        ExcelField(name="岗位")
    ]
    # 标题链接
    title_url: Annotated[
        Optional[str],
        Field(default=None, description="标题链接"),
        VoField(query=True),
        ExcelField(name="标题链接")
    ]
    # 薪资范围
    salary_range: Annotated[
        Optional[str],
        Field(default=None, description="薪资范围"),
        ExcelField(name="薪资范围")
    ]
    # 月薪最小值
    salary_month_min: Annotated[
        Optional[float],
        Field(default=None, description="月薪最小值"),
        ExcelField(name="月薪最小值")
    ]
    # 月薪最大值
    salary_month_max: Annotated[
        Optional[float],
        Field(default=None, description="月薪最大值"),
        ExcelField(name="月薪最大值")
    ]
    # 月薪平均值
    salary_month_avg: Annotated[
        Optional[float],
        Field(default=None, description="月薪平均值"),
        ExcelField(name="月薪平均值")
    ]
    # 地点
    location: Annotated[
        Optional[str],
        Field(default=None, description="地点"),
        VoField(query=True),
        ExcelField(name="地点")
    ]
    # 经验要求
    experience_required: Annotated[
        Optional[str],
        Field(default=None, description="经验要求"),
        VoField(query=True),
        ExcelField(name="经验要求")
    ]
    # 学历要求
    education_required: Annotated[
        Optional[str],
        Field(default=None, description="学历要求"),
        VoField(query=True),
        ExcelField(name="学历要求")
    ]
    # 技能要求
    skill_required: Annotated[
        Optional[str],
        Field(default=None, description="技能要求"),
        VoField(query=True),
        ExcelField(name="技能要求")
    ]
    # 企业名称
    enterprise_name: Annotated[
        Optional[str],
        Field(default=None, description="企业名称"),
        VoField(query=True),
        ExcelField(name="企业名称")
    ]
    # 上市情况
    listing_status: Annotated[
        Optional[str],
        Field(default=None, description="上市情况"),
        VoField(query=True),
        ExcelField(name="上市情况")
    ]
    # 企业规模
    enterprise_size: Annotated[
        Optional[str],
        Field(default=None, description="企业规模"),
        VoField(query=True),
        ExcelField(name="企业规模")
    ]
    # 主营业务
    main_business: Annotated[
        Optional[str],
        Field(default=None, description="主营业务"),
        VoField(query=True),
        ExcelField(name="主营业务")
    ]
    # 标题详情
    title_detail: Annotated[
        Optional[str],
        Field(default=None, description="标题详情"),
        VoField(query=True),
        ExcelField(name="标题详情")
    ]
    # 薪资范围2
    salary_range2: Annotated[
        Optional[str],
        Field(default=None, description="薪资范围2"),
        ExcelField(name="薪资范围2")
    ]
    # 岗位描述
    job_description: Annotated[
        Optional[str],
        Field(default=None, description="岗位描述"),
        ExcelField(name="岗位描述")
    ]
    # 工作地点
    word_location: Annotated[
        Optional[str],
        Field(default=None, description="工作地点"),
        ExcelField(name="工作地点")
    ]

    # 页码
    page_num: Optional[int] = Field(default=1, description="页码")
    # 每页数量
    page_size: Optional[int] = Field(default=10, description="每页数量")