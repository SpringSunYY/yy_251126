import request from '@/utils/request'





// 查询招聘信息表列表
export function listRecruitInfo(query) {
  return request({
    url: '/recruit/recruit/list',
    method: 'get',
    params: query
  })
}

// 查询招聘信息表详细
export function getRecruitInfo(recruitId) {
  return request({
    url: '/recruit/recruit/' +recruitId,
    method: 'get'
  })
}

// 新增招聘信息表
export function addRecruitInfo(data) {
  return request({
    url: '/recruit/recruit',
    method: 'post',
    data: data
  })
}

// 修改招聘信息表
export function updateRecruitInfo(data) {
  return request({
    // 后端 Flask 控制器使用的是不带主键的 PUT '' 路径，这里保持一致
    url: '/recruit/recruit',
    method: 'put',
    data: data
  })
}

// 删除招聘信息表
export function delRecruitInfo(recruitId) {
  return request({
    url: '/recruit/recruit/' +recruitId,
    method: 'delete'
  })
}