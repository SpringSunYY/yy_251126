<template>
  <div class="app-container">
    <!-- 搜索栏 -->
    <el-form :model="queryParams" ref="queryForm" size="small" :inline="true" label-width="80px" class="search-form">
      <el-form-item label="岗位" prop="post">
        <el-input
          v-model="queryParams.post"
          placeholder="请输入岗位"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="地点" prop="location">
        <el-input
          v-model="queryParams.location"
          placeholder="请输入地点"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="经验要求" prop="experienceRequired">
        <el-select v-model="queryParams.experienceRequired" placeholder="请选择经验要求" clearable>
          <el-option
            v-for="dict in dict.type.recruit_experience_required"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="学历要求" prop="educationRequired">
        <el-select v-model="queryParams.educationRequired" placeholder="请选择学历要求" clearable>
          <el-option
            v-for="dict in dict.type.recruit_education_required"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="技能要求" prop="skillRequired">
        <el-input
          v-model="queryParams.skillRequired"
          placeholder="请输入技能要求"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="企业名称" prop="enterpriseName">
        <el-input
          v-model="queryParams.enterpriseName"
          placeholder="请输入企业名称"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item label="上市情况" prop="listingStatus">
        <el-select v-model="queryParams.listingStatus" placeholder="请选择上市情况" clearable>
          <el-option
            v-for="dict in dict.type.recruit_listing_status"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="企业规模" prop="enterpriseSize">
        <el-select v-model="queryParams.enterpriseSize" placeholder="请选择企业规模" clearable>
          <el-option
            v-for="dict in dict.type.recruit_enterprise_size"
            :key="dict.value"
            :label="dict.label"
            :value="dict.value"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="主营业务" prop="mainBusiness">
        <el-input
          v-model="queryParams.mainBusiness"
          placeholder="请输入主营业务"
          clearable
          @keyup.enter.native="handleQuery"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
        <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>
    <el-row :gutter="10">
      <el-col :span="7">
        <div class="chart-wrapper" style="height: 50vh">
          <KeywordGravityCharts :chart-data="killAnalysisData"
                                :chart-name="killAnalysisName"/>
        </div>
        <div class="chart-wrapper" style="height: 30vh">
          <ScatterAvgCharts :chart-data="killAnalysisSalaryData"
                            :chart-name="killAnalysisSalaryName"
          />
        </div>
      </el-col>
      <el-col :span="8">
        <MapCharts style="height: 60vh"/>
      </el-col>
      <el-col :span="7">
        <div class="chart-wrapper" style="height: 30vh">
          <KeywordTooltipCharts
            :chart-data="recruitBusinessSkillAnalysisData"
            :chart-name="recruitBusinessSkillAnalysisName"
          />
        </div>
        <div class="chart-wrapper" style="height: 30vh">
          <ScatterRandomCharts
            :chart-data="recruitBusinessSkillSalaryData"
            :chart-name="recruitBusinessSkillSalaryName"
          />
        </div>
      </el-col>
    </el-row>


  </div>
</template>

<script>
import PanelGroup from './dashboard/PanelGroup'
import LineChart from './dashboard/LineChart'
import RaddarChart from './dashboard/RaddarChart'
import PieChart from './dashboard/PieChart'
import BarChart from './dashboard/BarChart'
import {
  recruitBusinessSalaryAnalysis,
  recruitBusinessSkillAnalysis,
  recruitSkillAnalysis,
  recruitSkillSalaryAnalysis
} from "@/api/recruit/statistics";
import KeywordGravityCharts from "@/components/Echarts/KeywordGravityCharts.vue";
import RelationCharts from "@/components/Echarts/RelationCharts.vue";
import ScatterAvgCharts from "@/components/Echarts/ScatterAvgCharts.vue";
import KeywordTooltipCharts from "@/components/Echarts/KeywordTooltipCharts.vue";
import ScatterRandomCharts from "@/components/Echarts/ScatterRandomCharts.vue";
import MapCharts from "@/components/Echarts/MapCharts.vue";


export default {
  name: 'Index',
  components: {
    MapCharts,
    ScatterRandomCharts,
    KeywordTooltipCharts,
    ScatterAvgCharts,
    RelationCharts,
    KeywordGravityCharts: KeywordGravityCharts,
    PanelGroup,
    LineChart,
    RaddarChart,
    PieChart,
    BarChart
  },
  dicts: ['recruit_experience_required', 'recruit_education_required', 'recruit_listing_status', 'recruit_enterprise_size'],
  data() {
    return {
      killAnalysisData: [],
      killAnalysisName: "求职技能分析",
      killAnalysisSalaryData: [],
      killAnalysisSalaryName: "技能职位与平均工资散点图",
      recruitBusinessSkillAnalysisData: [],
      recruitBusinessSkillAnalysisName: "招聘信息行业所需技能分析",
      recruitBusinessSkillSalaryName: "招聘信息行业薪资分析",
      recruitBusinessSkillSalaryData: [],
      // 查询参数
      queryParams: {
        post: null,
        location: null,
        experienceRequired: null,
        educationRequired: null,
        skillRequired: null,
        enterpriseName: null,
        listingStatus: null,
        enterpriseSize: null,
        mainBusiness: null,
      },
    }
  },
  created() {
    this.getStatisticsData()
  },
  methods: {
    /** 搜索按钮操作 */
    handleQuery() {
      this.getStatisticsData()
    },
    /** 重置按钮操作 */
    resetQuery() {
      this.resetForm("queryForm");
      this.handleQuery()
    },
    getStatisticsData() {
      this.getKillAnalysisData()
      this.getKillAnalysisSalaryData()
      this.getRecruitBusinessSkillSalaryData()
      this.getRecruitBusinessSkillAnalysisData()
    },
    getKillAnalysisData() {
      recruitSkillAnalysis(this.queryParams).then(res => {
        this.killAnalysisData = res.data
      })
    },
    getKillAnalysisSalaryData() {
      recruitSkillSalaryAnalysis(this.queryParams).then(res => {
        if (!res.data || !res.data.length) {
          return
        }
        this.killAnalysisSalaryData = res.data.map(item => {
          return {
            name: item.name,
            xAxis: item.value,
            yAxis: item.avgSalary,
            tooltip: `平均工资：${item.avgSalary}\n最高工资：${item.maxSalary}\n最低工资：${item.minSalary}`
          }
        })
      })
    },
    getRecruitBusinessSkillSalaryData() {
      recruitBusinessSalaryAnalysis(this.queryParams).then(res => {
        if (!res.data || !res.data.length) {
          return
        }
        this.recruitBusinessSkillSalaryData = res.data.map(item => {
          return {
            name: item.name,
            value: item.maxSalary,
            tooltip: `平均工资：${item.avgSalary}\n最高工资：${item.maxSalary}\n最低工资：${item.minSalary}`
          }
        })
      })
    },

    getRecruitBusinessSkillAnalysisData() {
      recruitBusinessSkillAnalysis(this.queryParams).then(res => {
        this.recruitBusinessSkillAnalysisData = res.data.map(item => {
          if (item.tooltips) {
            let tooltip = `行业所需技能:\n`
            item.tooltips.forEach(skill => {
              tooltip += `${skill.name}：${skill.value}\n`
            })
            return {
              name: item.name,
              value: item.value,
              tooltip: tooltip
            }
          } else {
            return {
              name: item.name,
              value: item.value
            }
          }
        })
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.app-container {
  margin-top: -10px; // 抵消默认间距
  height: 92vh;
  width: 100%;
  position: relative;
  background-image: url("../assets/images/index-bg.png");
  background-repeat: repeat;
  background-size: cover;
  overflow: hidden;
}

.search-form {
  background: 'transparent';
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>
