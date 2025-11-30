<template>
  <div :class="className" :style="{ height, width }" ref="chartRef"/>
</template>

<script>
// 引入 ECharts 库
import echarts from 'echarts';
import {generateRandomColor} from "@/utils/ruoyi";

export default {
  name: 'KeywordGravityCharts',

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
      default: '一天的时间流逝'
    },
    chartData: {
      type: Array,
      default: () => [
        // 示例数据
        {name: '听音乐', value: 2},
        {name: '看电影', value: 12},
        {name: '跑步', value: 22},
        {name: '瑜伽', value: 42},
        {name: '发呆', value: 52},
        {name: '阅读', value: 62},
        {name: '敲代码', value: 72},
        {name: '收纳', value: 80},
        {name: '熬夜', value: 65},
        {name: '旅行', value: 24},
        {name: '创作', value: 72},
        {name: '悲伤', value: 72},
        {name: '开心', value: 72}
      ]
    },
    fontSizeRange: {
      type: Array,
      default: () => [12, 24] // 默认字体大小范围 [最小, 最大]
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
    maxLabelLength: {
      type: Number,
      default: 4 // 默认最多显示4个字
    }
  },

  // 数据状态
  data() {
    return {
      chart: null, // ECharts 实例
    };
  },

  // 生命周期钩子：组件挂载后
  mounted() {
    this.$nextTick(() => {
      this.initChart(this.chartData);
      // 监听窗口尺寸变化
      window.addEventListener('resize', this.handleResize);
    });
  },

  // 生命周期钩子：组件销毁前
  beforeDestroy() {
    if (this.chart) {
      this.chart.dispose();
      this.chart = null;
    }
    window.removeEventListener('resize', this.handleResize);
  },

  // 监听器
  watch: {
    // 监听数据变化，重新渲染图表
    chartData: {
      handler(newData) {
        this.initChart(newData);
      },
      deep: true
    },
    // 监听字体大小范围变化，重新渲染图表
    fontSizeRange: {
      handler() {
        this.initChart(this.chartData);
      },
      deep: true
    }
  },

  methods: {
    /**
     * @description 计算数据总和
     */
    calculateTotal(data) {
      return data.reduce((sum, item) => Number(sum) + (Number(item.value) || 0), 0);
    },

    /**
     * @description 获取数据中的最小和最大 value 值
     */
    getMinMaxValue(data) {
      if (!data || data.length === 0) {
        return {min: 0, max: 0};
      }
      const values = data.map(item => item.value);
      return {
        min: Math.min(...values),
        max: Math.max(...values)
      };
    },

    /**
     * @description 根据数据值和范围计算字体大小
     */
    getFontSize(value, minDataValue, maxDataValue, minFontSize, maxFontSize) {
      if (maxDataValue === minDataValue) {
        return minFontSize;
      }
      const valueRatio = (value - minDataValue) / (maxDataValue - minDataValue);
      const calculatedFontSize = minFontSize + valueRatio * (maxFontSize - minFontSize);
      return Math.max(minFontSize, Math.min(maxFontSize, calculatedFontSize));
    },

    /**
     * @description 截断名字以适应最大长度限制（处理中文字符）
     */
    truncateName(name, maxLength) {
      if (!name) return '';
      let width = 0;
      let result = '';
      for (const char of name) {
        // 判断是否全角字符（中文等）
        const isFullWidth = /[\u4E00-\u9FFF\u3400-\u4DBF\uF900-\uFAFF]/.test(char) || char.charCodeAt(0) > 255;
        width += isFullWidth ? 1 : 0.5;
        if (width > maxLength) break;
        result += char;
      }
      return result;
    },

    /**
     * @description 初始化 ECharts 图表
     */
    initChart(data) {
      if (!data || data.length === 0) {
        if (this.chart) {
          this.chart.dispose();
          this.chart = null;
        }
        return;
      }

      // 销毁旧实例并创建新实例
      if (this.chart) {
        this.chart.dispose();
      }
      this.chart = echarts.init(this.$refs.chartRef); // 使用 Vue 2 的 $refs 获取 DOM

      const {min: minChartValue, max: maxChartValue} = this.getMinMaxValue(data);
      const total = this.calculateTotal(data);

      const seriesData = data.map((item) => {
        const calculatedFontSize = this.getFontSize(
          item.value,
          minChartValue,
          maxChartValue,
          this.fontSizeRange[0],
          this.fontSizeRange[1]
        );

        return {
          name: item.name,
          value: item.value,
          label: {
            show: true,
            formatter: () => this.truncateName(item.name, this.maxLabelLength),
            color: generateRandomColor(this.defaultColor),
            fontSize: calculatedFontSize
          },
          itemStyle: {
            // 将节点本身设置为透明
            color: 'rgba(0,0,0,0)',
            borderWidth: 0
          },
          symbolSize: calculatedFontSize * 1.5,
        };
      });

      const option = {
        title: {
          show: true,
          text: this.chartName,
          textStyle: {
            fontSize: 16,
            color: '#ffffff',
          },
          top: '5%',
          left: '5%',
        },
        tooltip: {
          show: true,
          trigger: 'item',
          formatter: function (params) {
            const percentage = total > 0 ? ((params.data.value / total) * 100).toFixed(1) : '0.0';
            // 显示完整的名字，而不仅仅是截断的名字
            return `${params.data.name}: ${params.data.value} (${percentage}%)<br/>总计: ${total}`;
          },
          backgroundColor: 'rgba(0,0,0,0.5)',
          textStyle: {
            color: '#fff'
          }
        },
        toolbox: {
          show: true,
          feature: {
            restore: {}
          }
        },
        series: [
          {
            type: 'graph',
            layout: 'force',
            roam: 'scale',
            force: {
              repulsion: 100,
              gravity: 0.5,
              edgeLength: 5,
              friction: 0.5,
              layoutAnimation: true
            },
            label: {
              show: true,
              position: 'inside'
            },
            lineStyle: {
              opacity: 0 // 隐藏连线
            },
            top: "1%",
            bottom: "1%",
            left: "1%",
            right: "1%",
            data: seriesData,
            links: [], // 没有连线
            animation: true,
            animationDuration: 1500,
            animationEasing: 'cubicOut'
          }
        ]
      };

      this.chart.setOption(option);
    },

    /**
     * @description 处理窗口大小变化，调整图表尺寸
     */
    handleResize() {
      if (this.chart) {
        this.chart.resize();
      }
    }
  }
};
</script>

<style scoped>
.chart {
  /* 确保父容器有明确的尺寸，或者在外部 CSS 中定义 */
  padding: 10px;
  box-sizing: border-box;
  /* 示例：如果你希望在没有父级尺寸时有一个默认高度 */
  /* min-height: 400px; */
}
</style>
