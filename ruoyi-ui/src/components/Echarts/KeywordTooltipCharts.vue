<template>
  <div :class="className" :style="{ height, width }" ref="chartRef"/>
</template>

<script>
// 引入 Highcharts 核心库
import Highcharts from 'highcharts';

// 必须引入词云图模块
// highcharts 模块是 UMD 格式，在 webpack 中需要使用 require
const wordcloudModule = require('highcharts/modules/wordcloud');
const exportingModule = require('highcharts/modules/exporting');
const fullscreenModule = require('highcharts/modules/full-screen');

// 尝试多种可能的导出格式
const getModuleFunction = (module) => {
  if (typeof module === 'function') {
    return module;
  }
  if (module && typeof module.default === 'function') {
    return module.default;
  }
  if (module && module.__esModule && module.default) {
    return module.default;
  }
  if (module && typeof module === 'object') {
    for (const key in module) {
      if (typeof module[key] === 'function') {
        return module[key];
      }
    }
  }
  return module;
};

const WordCloud = getModuleFunction(wordcloudModule);
const Exporting = getModuleFunction(exportingModule);
const FullScreen = getModuleFunction(fullscreenModule);

// 应该确保在使用前正确初始化模块
if (typeof WordCloud === 'function') {
  WordCloud(Highcharts);
} else {
  console.error('无法初始化 WordCloud 模块，模块类型:', typeof WordCloud, WordCloud);
}

if (typeof Exporting === 'function') {
  Exporting(Highcharts);
}

if (typeof FullScreen === 'function') {
  FullScreen(Highcharts);
}

import {generateRandomColor} from "@/utils/ruoyi";

// 原始数据
const RAW_DATA = [
  {name: "生活资源", value: 999},
  {name: "供热管理", value: 888, tooltip: "供热管理是这样的\n需要供热"},
  {name: "供气质量", value: 777, tooltip: "供气质量最近良好"},
  {name: "生活用水管理", value: 688},
  {name: "一次供水问题", value: 588},
  {name: "交通运输", value: 516},
  {name: "城市交通", value: 515},
  {name: "环境保护", value: 483},
  {name: "房地产管理", value: 462},
  {name: "城乡建设", value: 449},
  {name: "社会保障与福利", value: 429},
  {name: "公共安全", value: 406},
  {name: "公交运输管理", value: 386},
  {name: "市容环卫", value: 355},
  {name: "自然资源管理", value: 355},
  {name: "粉尘污染", value: 335},
  {name: "噪声污染", value: 324}
];

// 初始化标题
const INITIAL_TITLE_TEXT = '城市热点问题词云图';


export default {
  name: 'KeywordTooltipCharts',

  // 属性定义
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '100%'
    },
    chartName: {
      type: String,
      default: INITIAL_TITLE_TEXT
    },
    chartData: {
      type: Array,
      default: () => RAW_DATA
    },
    fontSizeRange: {
      type: Array,
      default: () => [12, 80] // 默认字体大小范围
    },
    defaultColor: {
      type: Array,
      default: () => [
        '#5B8FF9', '#5AD8A6', '#5D7092', '#F6BD16', '#E86A92',
        '#7262FD', '#269A29', '#8E36BE', '#41A7E2', '#7747A3',
        '#FF7F50', '#FFDAB9', '#ADFF2F', '#00CED1', '#9370DB',
        '#3CB371', '#FF69B4', '#FFB6C1', '#DA70D6', '#98FB98',
        '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
        '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9'
      ]
    },
  },

  // 数据状态
  data() {
    return {
      chart: null, // Highcharts 实例
      processedData: [], // 经过 Highcharts 格式处理后的数据
    };
  },

  // 生命周期钩子：组件挂载后
  mounted() {
    this.$nextTick(() => {
      this.processAndInitChart(this.chartData);
      // 监听窗口尺寸变化
      window.addEventListener('resize', this.handleResize);
    });
  },

  // 生命周期钩子：组件销毁前
  beforeDestroy() {
    if (this.chart) {
      // Highcharts 使用 destroy() 释放资源
      this.chart.destroy();
      this.chart = null;
    }
    window.removeEventListener('resize', this.handleResize);
  },

  // 监听器
  watch: {
    // 监听数据变化，重新渲染图表
    chartData: {
      handler(newData) {
        this.processAndInitChart(newData);
      },
      deep: true
    },
  },

  methods: {
    /**
     * @description 将原始数据转换为 Highcharts 词云格式，并保留自定义 tooltip
     * 同时为每个词汇分配随机颜色
     */
    processData(rawData) {
      return rawData.map(item => ({
        name: item.name,
        weight: item.value, // Highcharts 词云图使用 'weight' 字段
        customTooltip: item.tooltip, // 保留自定义 tooltip 字段
        color: generateRandomColor(this.defaultColor) // **【随机颜色】**
      }));
    },

    /**
     * @description 重新初始化图表 (对应 ECharts 的 restore)
     */
    resetChart() {
      // 销毁旧图表并重新初始化，确保所有状态回到最初
      this.processAndInitChart(this.chartData);
    },

    /**
     * @description 处理数据并初始化/重绘图表
     */
    processAndInitChart(data) {
      this.processedData = this.processData(data);
      this.initChart();
    },
    /**
     * @description 初始化 Highcharts 图表
     */
    initChart() {
      if (!this.$refs.chartRef || !this.processedData.length) {
        if (this.chart) {
          this.chart.destroy();
          this.chart = null;
        }
        return;
      }

      // 销毁旧实例并创建新实例
      if (this.chart) {
        this.chart.destroy();
        this.chart = null;
      }

      const chartContainer = this.$refs.chartRef;

      const options = {
        title: {text: this.chartName},
        credits: {enabled: false},
        tooltip: {
          enabled: true,
          backgroundColor: 'rgba(0,0,0,0.2)',
          style: {
            color: '#fff',
            fontSize: '12px'
          },
          formatter: function () {
            const point = this.point;
            let html = `<b>${point.name}:${point.weight}</b><br/>`;
            if (point.customTooltip) {
              html += point.customTooltip.replace(/\n/g, '<br/>');
            }
            return html;
          },
        },

        exporting: {
          enabled: true,
          buttons: {
            contextButton: {
              menuItems: [
                'viewFullscreen',
                'printChart',
                'separator',
                // 自定义重置按钮
                {
                  text: 'Re-initialize',
                  onclick: () => {
                    this.resetChart();
                  }
                },
                'separator',
                'downloadPNG',
                'downloadJPEG',
                'downloadPDF',
                'downloadSVG',
                'viewData'
              ]
            }
          }
        },

        series: [{
          type: 'wordcloud',
          minFontSize: this.fontSizeRange[0],
          maxFontSize: this.fontSizeRange[1],
          data: this.processedData,
          name: '热点权重',
        }]
      };

      // 创建 Highcharts 实例
      this.chart = Highcharts.chart(chartContainer, options);
    },

    /**
     * @description 处理窗口大小变化，调整图表尺寸
     */
    handleResize() {
      if (this.chart) {
        this.chart.reflow(); // Highcharts 调整图表尺寸的方法
      }
    }
  }
};
</script>

<style scoped>

</style>
