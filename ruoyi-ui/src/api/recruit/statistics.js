import request from '@/utils/request'

//招聘信息技能统计
export function recruitSkillAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/skill',
    method: 'get',
    params: query
  })
}


//招聘信息分布统计
export function recruitDistributionAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/distribution',
    method: 'get',
    params: query
  })
}
