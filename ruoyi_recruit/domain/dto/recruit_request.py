from typing import Optional, Annotated

from pydantic import Field, BeforeValidator

from ruoyi_common.base.model import BaseEntity
from ruoyi_common.base.schema_excel import ExcelField
from ruoyi_common.base.schema_vo import VoField
from ruoyi_common.base.transformer import str_to_int


class recruit_statistics_request(BaseEntity):
    """
招聘信息统计查询对象
"""
    # 编号
    recruit_id: Annotated[
        Optional[int],
        BeforeValidator(str_to_int),
        Field(default=None, description="编号"),
        VoField(query=True),
    ]
    # 岗位
    post: Annotated[
        Optional[str],
        Field(default=None, description="岗位"),
        VoField(query=True),
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
