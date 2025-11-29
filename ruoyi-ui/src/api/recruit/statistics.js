import request from '@/utils/request'

//招聘信息技能统计
export function recruitSkillAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/skill',
    method: 'get',
    params: query
  })
}

//招聘信息技能工资统计
export function recruitSkillSalaryAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/skill/salary',
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


//招聘信业务技能/statistics/business/skill
export function recruitBusinessSkillAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/business/skill',
    method: 'get',
    params: query
  })
}

//招聘信息业务工资
export function recruitBusinessSalaryAnalysis(query) {
  return request({
    url: '/recruit/recruit/statistics/business/salary',
    method: 'get',
    params: query
  })
}

