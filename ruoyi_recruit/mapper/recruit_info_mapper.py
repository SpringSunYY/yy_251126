# -*- coding: utf-8 -*-
# @Author  : YY
# @FileName: recruit_info_mapper.py
# @Time    : 2025-11-26 18:15:10

from typing import List
from datetime import datetime

from flask import g
from sqlalchemy import select, update, delete, func

from ruoyi_admin.ext import db
from ruoyi_recruit.domain.dto import recruit_statistics_request
from ruoyi_recruit.domain.entity import recruit_info
from ruoyi_recruit.domain.po import recruit_info_po
from ruoyi_recruit.domain.ro import statistics_ro
from ruoyi_recruit.domain.ro.statistics_ro import statistics_salary_ro


class recruit_info_mapper:
    """招聘信息表Mapper"""

    @staticmethod
    def select_recruit_info_list(recruit: recruit_info) -> List[recruit_info]:
        """
        查询招聘信息表列表

        Args:
            recruit (recruit_info): 招聘信息表对象

        Returns:
            List[recruit_info]: 招聘信息表列表
        """
        try:
            # 构建查询条件
            stmt = select(recruit_info_po)

            if recruit.recruit_id is not None:
                stmt = stmt.where(recruit_info_po.recruit_id == recruit.recruit_id)

            if recruit.post:
                stmt = stmt.where(recruit_info_po.post.like("%" + str(recruit.post) + "%"))

            if recruit.title_url is not None:
                stmt = stmt.where(recruit_info_po.title_url == recruit.title_url)

            if recruit.location:
                stmt = stmt.where(recruit_info_po.location.like("%" + str(recruit.location) + "%"))

            if recruit.experience_required is not None:
                stmt = stmt.where(recruit_info_po.experience_required == recruit.experience_required)

            if recruit.education_required:
                stmt = stmt.where(recruit_info_po.education_required.like("%" + str(recruit.education_required) + "%"))

            if recruit.skill_required:
                stmt = stmt.where(recruit_info_po.skill_required.like("%" + str(recruit.skill_required) + "%"))

            if recruit.enterprise_name:
                stmt = stmt.where(recruit_info_po.enterprise_name.like("%" + str(recruit.enterprise_name) + "%"))

            if recruit.listing_status is not None:
                stmt = stmt.where(recruit_info_po.listing_status == recruit.listing_status)

            if recruit.enterprise_size is not None:
                stmt = stmt.where(recruit_info_po.enterprise_size == recruit.enterprise_size)

            if recruit.main_business:
                stmt = stmt.where(recruit_info_po.main_business.like("%" + str(recruit.main_business) + "%"))

            if recruit.title_detail:
                stmt = stmt.where(recruit_info_po.title_detail.like("%" + str(recruit.title_detail) + "%"))

            if "criterian_meta" in g and g.criterian_meta.page:
                g.criterian_meta.page.stmt = stmt

            result = db.session.execute(stmt).scalars().all()
            return [recruit_info.model_validate(item) for item in result] if result else []
        except Exception as e:
            print(f"查询招聘信息表列表出错: {e}")
            return []

    @staticmethod
    def select_recruit_info_by_id(recruit_id: int) -> recruit_info:
        """
        根据ID查询招聘信息表

        Args:
            recruit_id (int): 编号

        Returns:
            recruit_info: 招聘信息表对象
        """
        try:
            print(recruit_id)
            result = db.session.get(recruit_info_po, recruit_id)
            return recruit_info.model_validate(result) if result else None
        except Exception as e:
            print(f"根据ID查询招聘信息表出错: {e}")
            return None

    @staticmethod
    def insert_recruit_info(recruit: recruit_info) -> int:
        """
        新增招聘信息表

        Args:
            recruit (recruit_info): 招聘信息表对象

        Returns:
            int: 插入的记录数
        """
        try:
            now = datetime.now()
            new_po = recruit_info_po()
            new_po.recruit_id = recruit.recruit_id
            new_po.post = recruit.post
            new_po.title_url = recruit.title_url
            new_po.salary_range = recruit.salary_range
            new_po.salary_month_min = recruit.salary_month_min
            new_po.salary_month_max = recruit.salary_month_max
            new_po.salary_month_avg = recruit.salary_month_avg
            new_po.location = recruit.location
            new_po.experience_required = recruit.experience_required
            new_po.education_required = recruit.education_required
            new_po.skill_required = recruit.skill_required
            new_po.enterprise_name = recruit.enterprise_name
            new_po.listing_status = recruit.listing_status
            new_po.enterprise_size = recruit.enterprise_size
            new_po.main_business = recruit.main_business
            new_po.title_detail = recruit.title_detail
            new_po.salary_range2 = recruit.salary_range2
            new_po.job_description = recruit.job_description
            new_po.word_location = recruit.word_location
            db.session.add(new_po)
            db.session.commit()
            recruit.recruit_id = new_po.recruit_id
            return 1
        except Exception as e:
            db.session.rollback()
            print(f"新增招聘信息表出错: {e}")
            return 0

    @staticmethod
    def update_recruit_info(recruit: recruit_info) -> int:
        """
        修改招聘信息表

        Args:
            recruit (recruit_info): 招聘信息表对象

        Returns:
            int: 更新的记录数
        """
        try:

            existing = db.session.get(recruit_info_po, recruit.recruit_id)
            if not existing:
                return 0
            now = datetime.now()
            # 主键不参与更新
            existing.post = recruit.post
            existing.title_url = recruit.title_url
            existing.salary_range = recruit.salary_range
            existing.salary_month_min = recruit.salary_month_min
            existing.salary_month_max = recruit.salary_month_max
            existing.salary_month_avg = recruit.salary_month_avg
            existing.location = recruit.location
            existing.experience_required = recruit.experience_required
            existing.education_required = recruit.education_required
            existing.skill_required = recruit.skill_required
            existing.enterprise_name = recruit.enterprise_name
            existing.listing_status = recruit.listing_status
            existing.enterprise_size = recruit.enterprise_size
            existing.main_business = recruit.main_business
            existing.title_detail = recruit.title_detail
            existing.salary_range2 = recruit.salary_range2
            existing.job_description = recruit.job_description
            existing.word_location = recruit.word_location
            db.session.commit()
            return 1

        except Exception as e:
            db.session.rollback()
            print(f"修改招聘信息表出错: {e}")
            return 0

    @staticmethod
    def delete_recruit_info_by_ids(ids: List[int]) -> int:
        """
        批量删除招聘信息表

        Args:
            ids (List[int]): ID列表

        Returns:
            int: 删除的记录数
        """
        try:
            stmt = delete(recruit_info_po).where(recruit_info_po.recruit_id.in_(ids))
            result = db.session.execute(stmt)
            db.session.commit()
            return result.rowcount
        except Exception as e:
            db.session.rollback()
            print(f"批量删除招聘信息表出错: {e}")
            return 0

    @staticmethod
    def get_recruit_skill_statistics(request: recruit_statistics_request) -> List[statistics_ro]:
        """
        获取招聘信息技能统计
        -- 统计招聘信息技能总数
        select count(*) as value, skill_required as name from tb_recruit_info
        group by skill_required
        """
        # 构建查询条件
        # 构建查询语句，统计技能要求并按技能分组
        stmt = select(
            func.count().label('value'),
            recruit_info_po.skill_required.label('name')
        ).group_by(recruit_info_po.skill_required)
        # 过滤空值
        stmt = stmt.where(recruit_info_po.skill_required.isnot(None))
        stmt = recruit_info_mapper.builder_statistics_query(request, stmt)

        # 执行查询
        result = db.session.execute(stmt).fetchall()
        return [statistics_ro(value=row.value, name=row.name) for row in result]

    @staticmethod
    def get_recruit_skill_salary_statistics(request: recruit_statistics_request) -> List[statistics_salary_ro]:
        """
        获取招聘信息技能工资统计
        """
        stmt = select(
            func.count().label('value'),
            recruit_info_po.skill_required.label('name'),
            func.min(recruit_info_po.salary_month_min).label('min_salary'),
            func.max(recruit_info_po.salary_month_max).label('max_salary'),
            func.avg(recruit_info_po.salary_month_avg).label('avg_salary'),
        ).group_by(recruit_info_po.skill_required)
        stmt = stmt.where(recruit_info_po.skill_required.isnot(None))
        # 只统计有薪资数据的记录
        stmt = stmt.where(recruit_info_po.salary_month_min.isnot(None))
        stmt = recruit_info_mapper.builder_statistics_query(request, stmt)
        result = db.session.execute(stmt).fetchall()
        # 处理 None 值，如果为 None 则使用 0.0（理论上不会出现，因为已经过滤了）
        return [statistics_salary_ro(
            value=row.value, 
            name=row.name, 
            min_salary=float(row.min_salary) if row.min_salary is not None else 0.0, 
            max_salary=float(row.max_salary) if row.max_salary is not None else 0.0, 
            avg_salary=float(row.avg_salary) if row.avg_salary is not None else 0.0
        ) for row in result]

    @staticmethod
    def builder_statistics_query(request, stmt):
        if request.recruit_id is not None:
            stmt = stmt.where(recruit_info_po.recruit_id == request.recruit_id)
        if request.post:
            stmt = stmt.where(recruit_info_po.post.like("%" + str(request.post) + "%"))
        if request.location:
            stmt = stmt.where(recruit_info_po.location.like("%" + str(request.location) + "%"))
        if request.experience_required:
            stmt = stmt.where(recruit_info_po.experience_required == request.experience_required)
        if request.education_required:
            stmt = stmt.where(recruit_info_po.education_required == request.education_required)
        if request.skill_required:
            stmt = stmt.where(recruit_info_po.skill_required.like("%" + str(request.skill_required) + "%"))
        if request.enterprise_name:
            stmt = stmt.where(recruit_info_po.enterprise_name.like("%" + str(request.enterprise_name) + "%"))
        if request.listing_status:
            stmt = stmt.where(recruit_info_po.listing_status == request.listing_status)
        if request.enterprise_size:
            stmt = stmt.where(recruit_info_po.enterprise_size == request.enterprise_size)
        if request.main_business:
            stmt = stmt.where(recruit_info_po.main_business.like("%" + str(request.main_business) + "%"))
        return stmt

    @staticmethod
    def get_recruit_post_statistics(request: recruit_statistics_request):
        """
        获取招聘信息职位统计
        -- 统计招聘信息职位总数
        select count(*) as value, post as name from tb_recruit_info
        group by post
        """
        stmt = select(
            func.count().label('value'),
            recruit_info_po.post.label('name')
        ).group_by(recruit_info_po.post)
        stmt = stmt.where(recruit_info_po.post.isnot(None))
        stmt = recruit_info_mapper.builder_statistics_query(request, stmt)
        return [statistics_ro(value=row.value, name=row.name) for row in db.session.execute(stmt).fetchall()]
