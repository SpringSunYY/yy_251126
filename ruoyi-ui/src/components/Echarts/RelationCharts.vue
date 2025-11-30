<template>
  <div :class="className" :style="{ height, width }" ref="chartRef"/>
</template>

<script>
import echarts from 'echarts';

// 经验层自动生成方法
function expWrap(jobValue, skills) {
  const childrenList = [
    {name: "1年以下", value: 0},
    {name: "经验不限", value: 1},
    {name: "1-3年", value: 2},
    {name: "无经验", value: 3},
    {name: "3-5年", value: 4},
    {name: "5-10年", value: 5}
  ];

  return childrenList.map(exp => ({
    name: exp.name,
    value: exp.value,
    children: skills
  }));
}

// 核心数据结构
const defaultData =
  {
    "name": "企业岗位要求",
    "value": 0,
    "children": [
      {
        "name": "10000人以上", "value": 10,
        "children": [
          {
            "name": "Java工程师",
            "value": 101,
            "children": expWrap(101, [{"name": "Java", "value": 10101}, {
              "name": "Spring Boot",
              "value": 10102
            }, {"name": "MySQL", "value": 10103}, {"name": "Redis", "value": 10104}, {
              "name": "消息队列",
              "value": 10105
            }])
          },
          {
            "name": "前端工程师",
            "value": 102,
            "children": expWrap(102, [{"name": "Vue", "value": 10201}, {
              "name": "React",
              "value": 10202
            }, {"name": "TypeScript", "value": 10203}, {"name": "Vite", "value": 10204}])
          },
          {
            "name": "后端架构师",
            "value": 103,
            "children": expWrap(103, [{"name": "微服务架构", "value": 10301}, {
              "name": "分布式系统",
              "value": 10302
            }, {"name": "高并发设计", "value": 10303}, {"name": "容器化部署", "value": 10304}])
          },
          {
            "name": "测试工程师",
            "value": 104,
            "children": expWrap(104, [{"name": "自动化测试", "value": 10401}, {
              "name": "接口测试",
              "value": 10402
            }, {"name": "性能测试", "value": 10403}])
          },
          {
            "name": "产品经理",
            "value": 105,
            "children": expWrap(105, [{"name": "需求分析", "value": 10501}, {
              "name": "原型设计",
              "value": 10502
            }, {"name": "项目推进", "value": 10503}])
          },
          {
            "name": "数据分析师",
            "value": 106,
            "children": expWrap(106, [{"name": "Python", "value": 10601}, {
              "name": "数据清洗",
              "value": 10602
            }, {"name": "可视化报表", "value": 10603}])
          },
          {
            "name": "算法工程师",
            "value": 107,
            "children": expWrap(107, [{"name": "深度学习", "value": 10701}, {
              "name": "机器学习",
              "value": 10702
            }, {"name": "模型优化", "value": 10703}])
          }
        ]
      },
      {
        "name": "100-299人", "value": 20,
        "children": [
          {
            "name": "综合行政专员",
            "value": 201,
            "children": expWrap(201, [{"name": "文档管理", "value": 20101}, {
              "name": "沟通协调",
              "value": 20102
            }, {"name": "采购流程", "value": 20103}])
          },
          {
            "name": "运营专员",
            "value": 202,
            "children": expWrap(202, [{"name": "数据分析", "value": 20201}, {
              "name": "活动策划",
              "value": 20202
            }, {"name": "内容运营", "value": 20203}])
          },
          {
            "name": "仓库管理员",
            "value": 203,
            "children": expWrap(203, [{"name": "出入库管理", "value": 20301}, {
              "name": "物料盘点",
              "value": 20302
            }])
          },
          {
            "name": "客服专员",
            "value": 204,
            "children": expWrap(204, [{"name": "沟通能力", "value": 20401}, {
              "name": "问题处理",
              "value": 20402
            }])
          }
        ]
      },
      {
        "name": "20-99人", "value": 30,
        "children": [
          {
            "name": "电工",
            "value": 301,
            "children": expWrap(301, [{"name": "线路检修", "value": 30101}, {
              "name": "设备维护",
              "value": 30102
            }, {"name": "应急处理", "value": 30103}])
          },
          {
            "name": "维修工",
            "value": 302,
            "children": expWrap(302, [{"name": "设备维修", "value": 30201}, {
              "name": "工具使用",
              "value": 30202
            }, {"name": "机械基础", "value": 30203}])
          },
          {
            "name": "安全员",
            "value": 303,
            "children": expWrap(303, [{"name": "隐患排查", "value": 30301}, {
              "name": "安全巡检",
              "value": 30302
            }, {"name": "应急预案", "value": 30303}])
          },
          {
            "name": "保洁员",
            "value": 304,
            "children": expWrap(304, [{"name": "垃圾分类", "value": 30401}, {
              "name": "区域维护",
              "value": 30402
            }])
          },
          {
            "name": "质检员",
            "value": 305,
            "children": expWrap(305, [{"name": "质量抽检", "value": 30501}, {
              "name": "异常记录",
              "value": 30502
            }])
          },
          {"name": "仓储助理", "value": 306, "children": expWrap(306, [{"name": "仓库整理", "value": 30601}])}
        ]
      },
      {
        "name": "500-999人", "value": 40,
        "children": [
          {
            "name": "绿化养护工",
            "value": 401,
            "children": expWrap(401, [{"name": "植物修剪", "value": 40101}, {
              "name": "施肥",
              "value": 40102
            }, {"name": "病害识别", "value": 40103}])
          },
          {
            "name": "设备管理员",
            "value": 402,
            "children": expWrap(402, [{"name": "设备台账", "value": 40201}, {
              "name": "例行保养",
              "value": 40202
            }])
          }
        ]
      },
      {
        "name": "1000-9999人", "value": 50,
        "children": [
          {
            "name": "园林巡检员",
            "value": 501,
            "children": expWrap(501, [{"name": "植物病害识别", "value": 50101}, {
              "name": "巡查记录",
              "value": 50102
            }, {"name": "简单处理", "value": 50103}])
          },
          {
            "name": "消防巡检员",
            "value": 502,
            "children": expWrap(502, [{"name": "消防设备检查", "value": 50201}, {
              "name": "隐患发现",
              "value": 50202
            }])
          }
        ]
      },
      {
        "name": "300-499人", "value": 60,
        "children": [
          {
            "name": "环卫工人",
            "value": 601,
            "children": expWrap(601, [{"name": "垃圾清运", "value": 60101}, {
              "name": "区域巡查",
              "value": 60102
            }])
          },
          {
            "name": "司机",
            "value": 602,
            "children": expWrap(602, [{"name": "驾驶技能", "value": 60201}, {
              "name": "车辆保养",
              "value": 60202
            }])
          }
        ]
      },
      {
        "name": "20人以下", "value": 70,
        "children": [
          {
            "name": "店员",
            "value": 701,
            "children": expWrap(701, [{"name": "收银", "value": 70101}, {"name": "商品整理", "value": 70102}])
          },
          {
            "name": "外卖员",
            "value": 702,
            "children": expWrap(702, [{"name": "路线规划", "value": 70201}, {
              "name": "快速配送",
              "value": 70202,
              "children": []
            }])
          },
        ]
      }
    ]
  }
;

export default {
  name: 'RelationCharts',

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
    chartData: {
      type: Object,
      default: () => defaultData
    },
    chartName: {
      type: String,
      default: '数据分析'
    },
    colors: {
      type: Array,
      default: () => [
        {c1: "#00c7ef", c2: "#0AF3FF"},
        {c1: "#FF8E14", c2: "#FFA12F"},
        {c1: "#AF5AFF", c2: "#B62AFF"},
        {c1: "#25dd59", c2: "#29f463"},
        {c1: "#6E35FF", c2: "#6E67FF"},
        {c1: "#002AFF", c2: "#0048FF"},
        {c1: "#8CD282", c2: "#95F300"},
        {c1: "#3B0EFF", c2: "#604BFF"},
        {c1: "#00BE74", c2: "#04FDB8"},
        {c1: "#4a3ac6", c2: "#604BFF"}
      ]
    },
  },

  data() {
    return {
      chart: null,
      allNodes: [], // 存储所有节点数据，包含父子关系
      allLinks: [], // 存储所有连线数据
      highlightedNodes: new Set(), // 存储当前高亮节点的ID
      highlightedLinks: new Set() // 存储当前高亮连线的ID
    };
  },

  mounted() {
    this.$nextTick(() => {
      this.initChart();
      window.addEventListener('resize', this.handleResize);
    });
  },

  beforeDestroy() {
    if (this.chart) {
      this.chart.off('mouseover', this.handleMouseOver);
      this.chart.off('mouseout', this.handleMouseOut);
      this.chart.dispose();
      this.chart = null;
    }
    window.removeEventListener('resize', this.handleResize);
  },

  watch: {
    chartData: {
      handler() {
        this.initChart();
      },
      deep: true
    }
  },

  methods: {
    /**
     * 生成唯一ID
     */
    generateIds(arr, parentId = '', parentNode = null, index = 0) {
      arr.forEach((item, idx) => {
        if (item.name === null) return;
        item.parentId = parentNode ? parentNode.id : null;
        item.level = parentNode ? parentNode.level + 1 : 0;

        // 使用更可靠的唯一ID生成方式
        item.id = `${parentId || 'root'}_${item.level}_${item.name}`;
        if (item.children && item.children.length) {
          this.generateIds(item.children, item.id, item, idx);
        }
      });
    },

    /**
     * 递归处理节点数据，生成图谱节点
     * **修改点：在 item 中存储 color 对象、parentId、level**
     */
    handle2(arr, idx, color, category, children, legend) {
      arr.forEach((item, index) => {
        if (item.name === null) return;

        let chineseName = item.name;
        let symbolSize = 10;

        switch (idx) {
          case 0:
            symbolSize = 70;
            break;
          case 1:
            symbolSize = 50;
            break;
          default:
            symbolSize = 10;
            break;
        }

        let label = null;
        if (idx === 0 || idx === 1) {
          label = {position: "inside", rotate: 0};
        }

        // 确定当前节点的颜色对象
        let currentColor = color;
        if (idx === 0) currentColor = this.colors[0];
        if (idx === 1) {
          currentColor = this.colors[index % 10];
          legend.push(chineseName);
        }

        let bgcolor;
        if (idx === 0) {
          bgcolor = {
            type: "radial",
            x: 0.5,
            y: 0.5,
            r: 0.5,
            colorStops: [
              {offset: 0, color: currentColor.c1},
              {offset: 0.8, color: currentColor.c1},
              {offset: 1, color: "rgba(0, 0, 0, 0.3)"}
            ],
            global: false
          };
        } else {
          bgcolor = {
            type: "radial",
            x: 0.5,
            y: 0.5,
            r: 0.5,
            colorStops: [
              {offset: 0, color: currentColor.c1},
              {offset: 0.4, color: currentColor.c1},
              {offset: 1, color: currentColor.c2}
            ],
            global: false
          };
        }

        let itemStyle;
        if (item.children && item.children.length) {
          // 非叶子节点
          itemStyle = {borderColor: currentColor.c2, color: bgcolor};
        } else {
          // 叶子节点
          item.isEnd = true;
          itemStyle = {color: "transparent", borderColor: currentColor.c2};
        }

        itemStyle = Object.assign(itemStyle, {
          shadowColor: "rgba(255, 255, 255, 0.5)",
          shadowBlur: 10
        });

        if (idx === 1) category = chineseName;

        let obj = {
          name: item.id,
          originalName: chineseName,
          symbolSize,
          category,
          label,
          color: bgcolor,
          itemStyle,
          originalValue: item.value,
          lineColor: currentColor.c2,
          // **将 id, parentId, level 等重要信息合并到 ECharts 节点对象中**
          id: item.id,
          parentId: item.parentId,
          level: item.level,
        };

        Object.assign(item, obj);

        if (idx === 0) item.root = true;
        if (!item.children || !item.children.length) item.isEnd = true;

        children.push(item);

        if (item.children && item.children.length) {
          this.handle2(item.children, idx + 1, currentColor, category, children, legend);
        }
      });
    },

    /**
     * 递归处理数据，生成图谱链接
     */
    handle3(arr, links) {
      arr.forEach((item) => {
        if (item.children) {
          const parentLineColor = item.lineColor || this.colors[0].c2;

          item.children.forEach((item2) => {
            const lineColor = parentLineColor;

            links.push({
              source: item.id,
              target: item2.id,
              // 使用 name 属性来作为唯一标识，方便后续 dispatchAction 定位
              name: `${item.id}-${item2.id}`,
              lineStyle: {
                color: lineColor,
                width: 1.5
              },
              emphasis: {
                lineStyle: {
                  color: '#FFD700', // 高亮颜色
                  width: 3,
                  shadowBlur: 10,
                  shadowColor: '#FFD700'
                }
              }
            });
          });

          this.handle3(item.children, links);
        }
      });
    },

    /**
     * **新增方法：获取所有祖先节点ID和相关的连线ID**
     */
    getAncestorsAndLinks(nodeId) {
      const ancestorIds = new Set();
      const ancestorLinkIds = new Set();
      let currentNode = this.allNodes.find(n => n.id === nodeId);

      while (currentNode && currentNode.parentId) {
        ancestorIds.add(currentNode.parentId);
        // 添加连接当前节点与其父节点的连线 ID
        ancestorLinkIds.add(`${currentNode.parentId}-${currentNode.id}`);
        currentNode = this.allNodes.find(n => n.id === currentNode.parentId);
      }
      return {ancestorIds, ancestorLinkIds};
    },

    /**
     * **新增方法：递归获取所有后代节点ID和相关的连线ID**
     */
    getDescendantsAndLinks(nodeId, descendantIds, descendantLinkIds) {
      this.allLinks.forEach(link => {
        if (link.source === nodeId) {
          const targetId = link.target;
          if (!descendantIds.has(targetId)) {
            descendantIds.add(targetId);
            descendantLinkIds.add(link.name);
            this.getDescendantsAndLinks(targetId, descendantIds, descendantLinkIds);
          }
        }
      });
    },

    /**
     * 新增方法：处理鼠标悬停事件
     */
    handleMouseOver(params) {
      if (params.dataType !== 'node') return;

      const hoveredNodeId = params.data.id;
      const nodesToHighlight = new Set([hoveredNodeId]);
      const linksToHighlight = new Set();

      // 1. 获取所有祖先节点及其连线
      const {ancestorIds, ancestorLinkIds} = this.getAncestorsAndLinks(hoveredNodeId);
      ancestorIds.forEach(id => nodesToHighlight.add(id));
      ancestorLinkIds.forEach(id => linksToHighlight.add(id));

      // 2. 获取所有后代节点及其连线
      const descendantIds = new Set();
      const descendantLinkIds = new Set();
      this.getDescendantsAndLinks(hoveredNodeId, descendantIds, descendantLinkIds);
      descendantIds.forEach(id => nodesToHighlight.add(id));
      descendantLinkIds.forEach(id => linksToHighlight.add(id));

      // 3. 添加当前节点与其父节点/子节点的直接连线
      this.allLinks.forEach(link => {
        if (link.source === hoveredNodeId || link.target === hoveredNodeId) {
          linksToHighlight.add(link.name);
          // 确保直接相连的节点也被高亮（尽管 getAncestors/getDescendants 已覆盖）
          nodesToHighlight.add(link.source);
          nodesToHighlight.add(link.target);
        }
      });

      // 4. 清除上次的高亮并设置新的高亮
      this.clearHighlight();

      // 执行高亮操作
      this.chart.dispatchAction({
        type: 'highlight',
        seriesIndex: 0,
        // ECharts 的 highlight action 可以接受 name 数组来高亮节点和连线
        name: [...nodesToHighlight, ...linksToHighlight]
      });

      this.highlightedNodes = nodesToHighlight;
      this.highlightedLinks = linksToHighlight;
    },

    /**
     * 处理鼠标移出事件
     */
    handleMouseOut(params) {
      // 只需要在鼠标移出图表区域或移出节点时执行清除操作
      if (params.dataType === 'node') {
        this.clearHighlight();
      }
    },

    /**
     * 清除所有高亮
     */
    clearHighlight() {
      if (this.highlightedNodes.size > 0 || this.highlightedLinks.size > 0) {
        // 清除上一次的高亮
        this.chart.dispatchAction({
          type: 'downplay',
          seriesIndex: 0,
          name: [...this.highlightedNodes, ...this.highlightedLinks]
        });
        this.highlightedNodes.clear();
        this.highlightedLinks.clear();
      }
    },

    /**
     * 初始化图表
     */
    initChart() {
      if (!this.chartData || Object.keys(this.chartData).length === 0) { // 检查对象是否为空
        if (this.chart) {
          this.chart.dispose();
          this.chart = null;
        }
        return;
      }

      if (!this.chart) {
        this.chart = echarts.init(this.$refs.chartRef);
        // **监听事件**
        this.chart.on('mouseover', this.handleMouseOver);
        this.chart.on('mouseout', this.handleMouseOut);
      } else {
        this.chart.off('mouseover', this.handleMouseOver);
        this.chart.off('mouseout', this.handleMouseOut);
        this.chart.clear();
        // 重新绑定事件
        this.chart.on('mouseover', this.handleMouseOver);
        this.chart.on('mouseout', this.handleMouseOut);
      }

      // 将对象格式的 chartData 包装成数组，并深拷贝
      const chartDataArray = [this.chartData];
      const processedData = JSON.parse(JSON.stringify(chartDataArray));

      // 调用生成 ID 时，同时生成父子关系信息
      this.generateIds(processedData);

      const children = [];
      const links = [];
      const legend = [];

      this.handle2(processedData, 0, null, null, children, legend);
      this.handle3(processedData, links);

      // 存储处理后的节点和连线数据到组件状态
      this.allNodes = children;
      this.allLinks = links;

      // 从数组的第一个（也是唯一的）元素中获取 categories
      const categories = this.chartData.children.map(item => ({name: item.name}));
      const legendColor = this.colors.map(item => item.c2);

      const vm = this;
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
        toolbox: {
          show: true,
          top: '7%',
          left: '1.9%',
          feature: {
            restore: {}
          }
        },
        tooltip: {
          formatter: function (params) {
            if (params.dataType === 'node' && params.data && params.data.originalName) {
              return `${params.data.originalName}<br>值: ${params.data.originalValue}`;
            }
            return '';
          },
          backgroundColor: 'rgba(50,50,50,0.7)',
          borderColor: '#fff',
          borderWidth: 1,
          textStyle: {color: '#fff'}
        },
        color: legendColor,
        legend: {
          show: true,
          data: legend,
          textStyle: {color: "#fff", fontSize: 10},
          icon: "circle",
          type: "scroll",
          orient: "vertical",
          left: "2%",
          top: "10%",
          bottom: 80,
          pageIconColor: "#00f6ff",
          pageIconInactiveColor: "#fff",
          pageIconSize: 12,
          pageTextStyle: {color: "#fff", fontSize: 12}
        },
        selectedMode: "false",
        bottom: 20,
        left: 0,
        right: 0,
        top: 0,
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        animationDurationUpdate: 0,
        series: [{
          name: "知识图谱",
          type: "graph",
          hoverAnimation: true,
          layout: "force",
          force: {
            repulsion: 300,
            edgeLength: 100,
            friction: 0.6,
            gravity: 0.1
          },
          nodeScaleRatio: 0.6,
          draggable: true,
          roam: true,
          symbol: "circle",
          data: children,
          links: links,
          categories: categories,
          // 禁用 ECharts 默认的焦点邻近，使用自定义的 mouseover 事件处理
          focusNodeAdjacency: false,
          // 悬停时高亮样式
          emphasis: {
            itemStyle: {
              borderWidth: 3,
              borderColor: '#FFD700'
            },
          },
          scaleLimit: {min: 0.05, max: 20},
          edgeSymbol: ["circle", "arrow"],
          edgeSymbolSize: [4, 8],
          label: {
            normal: {
              show: true,
              position: "right",
              color: "#fff",
              distance: 5,
              fontSize: 10,
              formatter: function (params) {
                return params.data.originalName || params.name;
              }
            }
          },
          lineStyle: {
            width: 1.5,
            curveness: 0,
            type: "solid"
          }
        }]
      };

      this.chart.setOption(option);
    },

    /**
     * 处理窗口大小变化
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
}
</style>
