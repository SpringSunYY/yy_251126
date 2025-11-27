import request from '@/utils/request'

//招聘信息技能统计
export function recruitSkillAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/skill',
    method: 'get',
    params: query
  })
}
