const res = document.getElementById('res').innerText.replace(/'/g, '"');
const data = document.getElementById('data').innerText.replace(/'/g, '"');
const links = document.getElementById('links').innerText.replace(/'/g, '"');
const res_j = JSON.parse(res);
const data_j = JSON.parse(data);
const links_j = JSON.parse(links);
const title = document.getElementsByClassName('title');
const brief = document.getElementsByClassName('brief');
const tags = document.getElementsByClassName('tags');
const map = document.getElementsByClassName('map');
const tag = document.getElementsByClassName('tag');

title[0].innerText = res_j.course_name;
brief[0].innerText = res_j.course_description;
tag[0].innerText = '学习时长:'+res_j.duration+'min';


// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));
var option;
// 指定图表的配置项和数据
option = {
    // title: {
    //   text: 'Basic Graph'
    // },
    tooltip: {},
    animationDurationUpdate: 1500,
    animationEasingUpdate: 'quinticInOut',
    series: [
        {
            type: 'graph',
            layout: 'force',
            symbolSize: 20,
            roam: false,
            force: {  //斥力因子
                repulsion: 100,
                edgeLength: [100, 200],
            },
            draggable: true,
            label: {
                show: true
            },
            edgeSymbol: ['', 'arrow'],
            // edgeSymbolSize: [4, 10],
            edgeLabel: {
                fontSize: 20
            },
            data: data_j,
            // links: [],
            links: links_j,

            lineStyle: {
                opacity: 0.9,
                curveness: 0
            }
        }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);