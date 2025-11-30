<template>
  <StarsBorderBg height="92vh" class="relation-container">
    <RelationCharts :chart-data="recruitDistributionData"
                    :chart-name="recruitDistributionName"/>
  </StarsBorderBg>
</template>
<script>

import RelationCharts from "@/components/Echarts/RelationCharts.vue";
import {recruitDistributionAnalysis} from "@/api/recruit/statistics";
import StarsBorderBg from "@/components/BorderBg/StarsBorderBg.vue";

export default {
  name:"RecruitRelation",
  components: {StarsBorderBg, RelationCharts},
  data() {
    return {
      recruitDistributionData: {},
      recruitDistributionName: "企业岗位所需经验与技能分析",
    }
  },
  created() {
    this.getRecruitDistributionData();
  },
  methods: {
    getRecruitDistributionData() {
      recruitDistributionAnalysis().then(res => {
        this.recruitDistributionData = res.data
      })
    },
  }
}

</script>
<style scoped lang="scss">
.relation-container {
  margin-top: -10px; // 抵消默认间距
  height: 92vh;
  width: 100%;
}
</style>
