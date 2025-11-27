# -*- coding: utf-8 -*-
# @Author  : YY
# @FileName: recruit_info_service.py
# @Time    : 2025-11-26 18:15:10

from typing import List

from ruoyi_common.exception import ServiceException
from ruoyi_common.utils.base import LogUtil
from ruoyi_framework.descriptor import custom_cacheable
from ruoyi_recruit.domain.dto import recruit_statistics_request
from ruoyi_recruit.domain.entity import recruit_info
from ruoyi_recruit.domain.vo.statistics_vo import statistics_vo
from ruoyi_recruit.mapper.recruit_info_mapper import recruit_info_mapper
import re


class recruit_info_service:
    """招聘信息表服务类"""

    def select_recruit_info_list(self, recruit: recruit_info) -> List[recruit_info]:
        """
        查询招聘信息表列表

        Args:
            recruit (recruit_info): 招聘信息表对象

        Returns:
            List[recruit_info]: 招聘信息表列表
        """
        return recruit_info_mapper.select_recruit_info_list(recruit)

    def select_recruit_info_by_id(self, recruit_id: int) -> recruit_info:
        """
        根据ID查询招聘信息表

        Args:
            recruit_id (int): 编号

        Returns:
            recruit_info: 招聘信息表对象
        """
        return recruit_info_mapper.select_recruit_info_by_id(recruit_id)

    def insert_recruit_info(self, recruit: recruit_info) -> int:
        """
        新增招聘信息表

        Args:
            recruit (recruit_info): 招聘信息表对象

        Returns:
            int: 插入的记录数
        """
        # 计算月薪
        self.calculate_recruit_salary(recruit)
        return recruit_info_mapper.insert_recruit_info(recruit)

    def update_recruit_info(self, recruit: recruit_info) -> int:
        """
        修改招聘信息表

        Args:
            recruit (recruit_info): 招聘信息表对象

        Returns:
            int: 更新的记录数
        """
        # 计算月薪
        self.calculate_recruit_salary(recruit)
        return recruit_info_mapper.update_recruit_info(recruit)

    def delete_recruit_info_by_ids(self, ids: List[int]) -> int:
        """
        批量删除招聘信息表

        Args:
            ids (List[int]): ID列表

        Returns:
            int: 删除的记录数
        """
        return recruit_info_mapper.delete_recruit_info_by_ids(ids)

    def import_recruit_info(self, recruit_list: List[recruit_info], is_update: bool = False) -> str:
        """
        导入招聘信息表数据

        Args:
            recruit_list (List[recruit_info]): 招聘信息表列表
            is_update (bool): 是否更新已存在的数据

        Returns:
            str: 导入结果消息
        """
        if not recruit_list:
            raise ServiceException("导入招聘信息表数据不能为空")

        success_count = 0
        fail_count = 0
        success_msg = ""
        fail_msg = ""

        for recruit in recruit_list:
            try:
                display_value = recruit
                # 计算月薪
                self.calculate_recruit_salary(recruit)
                display_value = getattr(recruit, "recruit_id", display_value)
                existing = None
                if recruit.recruit_id is not None:
                    existing = recruit_info_mapper.select_recruit_info_by_id(recruit.recruit_id)
                if existing:
                    if is_update:
                        result = recruit_info_mapper.update_recruit_info(recruit)
                    else:
                        fail_count += 1
                        fail_msg += f"<br/> 第{fail_count}条数据，已存在：{display_value}"
                        continue
                else:
                    result = recruit_info_mapper.insert_recruit_info(recruit)

                if result > 0:
                    success_count += 1
                    success_msg += f"<br/> 第{success_count}条数据，操作成功：{display_value}"
                else:
                    fail_count += 1
                    fail_msg += f"<br/> 第{fail_count}条数据，操作失败：{display_value}"
            except Exception as e:
                fail_count += 1
                fail_msg += f"<br/> 第{fail_count}条数据，导入失败，原因：{e.__class__.__name__}"
                LogUtil.logger.error(f"导入招聘信息表失败，原因：{e}")

        if fail_count > 0:
            if success_msg:
                fail_msg = f"导入成功{success_count}条，失败{fail_count}条。{success_msg}<br/>" + fail_msg
            else:
                fail_msg = f"导入成功{success_count}条，失败{fail_count}条。{fail_msg}"
            raise ServiceException(fail_msg)
        success_msg = f"恭喜您，数据已全部导入成功！共 {success_count} 条，数据如下：" + success_msg
        return success_msg

    def calculate_recruit_salary(self, recruit):
        """
        计算月薪
        """
        # 从数据里面拿到工资范围
        salary_range = recruit.salary_range
        if not salary_range:
            pass
        # 调用解析薪资的方法并使用返回值
        parsed_salary = self.parse_salary(salary_range)
        if parsed_salary:
            # 将解析后的薪资数据赋值给recruit对象
            recruit.salary_month_min = parsed_salary["min_salary"]
            recruit.salary_month_max = parsed_salary["max_salary"]
            recruit.salary_month_avg = parsed_salary["avg_salary"]
        pass

    @staticmethod
    def parse_salary(s: str):
        s = s.strip()
        if "面议" in s:
            return None

        # 默认薪资单位
        min_val = max_val = 0.0
        monthly_min = monthly_max = 0.0
        salary_multiplier = 12  # 默认按12薪
        day_pay = False

        # 是否有“xx薪”
        match_salary_times = re.search(r'·(\d+)薪', s)
        if match_salary_times:
            salary_multiplier = int(match_salary_times.group(1))

        # 区间匹配（如：1.5-3万、8000-12000元、100-200元/天）
        match_range = re.search(r'([\d.]+)-([\d.]+)', s)
        if match_range:
            min_val = float(match_range.group(1))
            max_val = float(match_range.group(2))
        else:
            # 只有一个数字
            match_single = re.search(r'([\d.]+)', s)
            if match_single:
                min_val = max_val = float(match_single.group(1))
            else:
                return None

        # 单位：万、元、元/天
        if "万" in s:
            min_val *= 10000
            max_val *= 10000
        elif "元/天" in s:
            day_pay = True
            min_val *= 30
            max_val *= 30
        else:
            # 默认元/月
            pass

        # 按薪数平摊到每个月
        monthly_min = min_val * salary_multiplier / 12
        monthly_max = max_val * salary_multiplier / 12
        monthly_avg = (monthly_min + monthly_max) / 2

        # 保留两位小数
        return {
            "min_salary": round(monthly_min, 2),
            "max_salary": round(monthly_max, 2),
            "avg_salary": round(monthly_avg, 2)
        }

    # region 数据分析
    @custom_cacheable(
        key_prefix="recruit_info_service",
        key_field="get_recruit_skill_analysis",
        use_query_params_as_key=True,
        expire_time=5*60
    )
    def get_recruit_skill_analysis(self, request: recruit_statistics_request)-> List[statistics_vo]:
        """
        获取招聘信息表技能分析
        """
        # 根据查询条件查询到所有的招聘信息
        statistics_ros = recruit_info_mapper.get_recruit_skill_statistics(request)
        # 将查询结果进行聚合，名称以逗号分割得到每个技能名称，并叠加统计数量
        skill_counts = {}
        for statistics_ro in statistics_ros:
            if not statistics_ro.name:
                continue
            skills = [skill.strip() for skill in statistics_ro.name.split(",") if skill.strip()]
            for skill in skills:
                skill_counts[skill] = skill_counts.get(skill, 0) + statistics_ro.value
        # 遍历结果集，返回一个统计对象列表，根据技能value排序，取前一百
        skill_counts = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:100]
        return [statistics_vo(name=name, value=count) for name, count in skill_counts]

# endregion
