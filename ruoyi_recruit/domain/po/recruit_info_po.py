# -*- coding: utf-8 -*-
# @Author  : YY
# @FileName: recruit_info_po.py
# @Time    : 2025-11-26 18:15:09

from typing import Optional
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Date, DateTime, Float, Integer, JSON, LargeBinary, Numeric, String, Text, Time
from sqlalchemy.orm import Mapped, mapped_column

from ruoyi_admin.ext import db

class recruit_info_po(db.Model):
    """
    招聘信息表PO对象
    """
    __tablename__ = 'tb_recruit_info'
    __table_args__ = {'comment': '招聘信息表'}
    recruit_id: Mapped[int] = mapped_column(
        'recruit_id',
        BigInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment='编号'
    )
    post: Mapped[Optional[str]] = mapped_column(
        'post',
        String(255),
        nullable=True,
        comment='岗位'
    )
    title_url: Mapped[Optional[str]] = mapped_column(
        'title_url',
        Text,
        nullable=True,
        comment='标题链接'
    )
    salary_range: Mapped[Optional[str]] = mapped_column(
        'salary_range',
        String(255),
        nullable=True,
        comment='薪资范围'
    )
    salary_month_min: Mapped[Optional[str]] = mapped_column(
        'salary_month_min',
        Numeric(10, 0),
        nullable=True,
        comment='月薪最小值'
    )
    salary_month_max: Mapped[Optional[str]] = mapped_column(
        'salary_month_max',
        Numeric(10, 0),
        nullable=True,
        comment='月薪最大值'
    )
    salary_month_avg: Mapped[Optional[str]] = mapped_column(
        'salary_month_avg',
        Numeric(10, 0),
        nullable=True,
        comment='月薪平均值'
    )
    location: Mapped[Optional[str]] = mapped_column(
        'location',
        String(255),
        nullable=True,
        comment='地点'
    )
    experience_required: Mapped[Optional[str]] = mapped_column(
        'experience_required',
        String(255),
        nullable=True,
        comment='经验要求'
    )
    education_required: Mapped[Optional[str]] = mapped_column(
        'education_required',
        String(255),
        nullable=True,
        comment='学历要求'
    )
    skill_required: Mapped[Optional[str]] = mapped_column(
        'skill_required',
        String(255),
        nullable=True,
        comment='技能要求'
    )
    enterprise_name: Mapped[Optional[str]] = mapped_column(
        'enterprise_name',
        String(255),
        nullable=True,
        comment='企业名称'
    )
    listing_status: Mapped[Optional[str]] = mapped_column(
        'listing_status',
        String(255),
        nullable=True,
        comment='上市情况'
    )
    enterprise_size: Mapped[Optional[str]] = mapped_column(
        'enterprise_size',
        String(255),
        nullable=True,
        comment='企业规模'
    )
    main_business: Mapped[Optional[str]] = mapped_column(
        'main_business',
        String(255),
        nullable=True,
        comment='主营业务'
    )
    title_detail: Mapped[Optional[str]] = mapped_column(
        'title_detail',
        String(255),
        nullable=True,
        comment='标题详情'
    )
    salary_range2: Mapped[Optional[str]] = mapped_column(
        'salary_range_2',
        String(255),
        nullable=True,
        comment='薪资范围2'
    )
    job_description: Mapped[Optional[str]] = mapped_column(
        'job_description',
        Text,
        nullable=True,
        comment='岗位描述'
    )
    word_location: Mapped[Optional[str]] = mapped_column(
        'word_location',
        String(255),
        nullable=True,
        comment='工作地点'
    )