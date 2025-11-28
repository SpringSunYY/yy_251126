<template>
  <div class="dashboard-editor-container">

    <panel-group @handleSetLineChartData="handleSetLineChartData"/>

    <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:32px;">
      <line-chart :chart-data="lineChartData"/>
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <raddar-chart/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <pie-chart/>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="8">
        <div class="chart-wrapper">
          <bar-chart/>
        </div>
      </el-col>
    </el-row>
    <div class="chart-wrapper" style="height: 50vh">
      <KeywordGravityCharts :chart-data="killAnalysisData"
                            :chart-name="killAnalysisName"/>
    </div>
    <div class="chart-wrapper" style="height: 100vh">
      <RelationCharts :chart-data="recruitDistributionData"
                      :chart-name="recruitDistributionName"/>
    </div>
    <div class="chart-wrapper" style="height: 100vh">
      <ScatterAvgCharts :chart-data="killAnalysisSalaryData"
                        :chart-name="killAnalysisSalaryName"
      />
    </div>

  </div>
</template>

<script>
import PanelGroup from './dashboard/PanelGroup'
import LineChart from './dashboard/LineChart'
import RaddarChart from './dashboard/RaddarChart'
import PieChart from './dashboard/PieChart'
import BarChart from './dashboard/BarChart'
import {recruitDistributionAnalysis, recruitSkillAnalysis, recruitSkillSalaryAnalysis} from "@/api/recruit/statistics";
import KeywordGravityCharts from "@/components/Echarts/KeywordGravityCharts.vue";
import RelationCharts from "@/components/Echarts/RelationCharts.vue";
import ScatterAvgCharts from "@/components/Echarts/ScatterAvgCharts.vue";

const lineChartData = {
  newVisitis: {
    expectedData: [100, 120, 161, 134, 105, 160, 165],
    actualData: [120, 82, 91, 154, 162, 140, 145]
  },
  messages: {
    expectedData: [200, 192, 120, 144, 160, 130, 140],
    actualData: [180, 160, 151, 106, 145, 150, 130]
  },
  purchases: {
    expectedData: [80, 100, 121, 104, 105, 90, 100],
    actualData: [120, 90, 100, 138, 142, 130, 130]
  },
  shoppings: {
    expectedData: [130, 140, 141, 142, 145, 150, 160],
    actualData: [120, 82, 91, 154, 162, 140, 130]
  }
}

export default {
  name: 'Index',
  components: {
    ScatterAvgCharts,
    RelationCharts,
    KeywordGravityCharts: KeywordGravityCharts,
    PanelGroup,
    LineChart,
    RaddarChart,
    PieChart,
    BarChart
  },
  data() {
    return {
      lineChartData: lineChartData.newVisitis,
      killAnalysisData: [],
      killAnalysisName: "求职技能分析",
      killAnalysisSalaryData: [],
      killAnalysisSalaryName: "技能职位与平均工资散点图",
      recruitDistributionData: {},
      recruitDistributionName: "招聘信息分布",

    }
  },
  created() {
    this.getKillAnalysisData()
    this.getRecruitDistributionData()
    this.getKillAnalysisSalaryData()
  },
  methods: {
    getKillAnalysisData() {
      recruitSkillAnalysis().then(res => {
        this.killAnalysisData = res.data
      })
    },
    getRecruitDistributionData() {
      recruitDistributionAnalysis().then(res => {
        this.recruitDistributionData = res.data
      })
    },
    getKillAnalysisSalaryData() {
      recruitSkillSalaryAnalysis().then(res => {
        if (!res.data || !res.data.length) {
          return
        }
        const data = res.data.map(item => {
          return {
            name: item.name,
            xAxis: item.value,
            yAxis: item.avgSalary,
            tooltip: `平均工资：${item.avgSalary}\n最高工资：${item.maxSalary}\n最低工资：${item.minSalary}`
          }
        })
        this.killAnalysisSalaryData = data
      })
    },
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

@media (max-width: 1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>
