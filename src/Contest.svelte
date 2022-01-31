<script>
  export let contestData;

	import highcharts from './highcharts';

  let candidates = []
  let raised = []
  let onhand = []

  contestData.forEach(i => candidates.push(i.candidate + " (" + i.party + ")") && raised.push(parseFloat(i.raised)) && onhand.push(parseFloat(i.onhand)));

  let styleGeneral = {
    fontFamily: '"Open Sans", Helvetica, Arial, "Lucida Grande", sans-serif',
    fontSize: '14px',
    fontWeight: 'normal',
    color: "#676767"
  }

  let config = {
    chart: {
      type: "bar",
    },
    credits: {enabled: false},
    colors: ['#0D57A0', '#0793AB'],
    title: {
      text: null
    },
    yAxis: {
        title: {
            text: 'Dollars'
        }
    },
    xAxis: {
      categories: candidates,
      labels: {
        style: styleGeneral
      }
    },
    legend: {
      margin: 30,
      verticalAlign: 'top',
      align: 'center',
      borderWidth: 0,
      itemDistance: 20,
      itemStyle: styleGeneral
    },
    tooltip: {
      style: styleGeneral,
      useHTML: true,
      formatter: function() {
        return '<strong>' + this.series.name + ", " + this.x + '</strong>: $' + this.y.toLocaleString('en-US');
      }
    },
    series: [{
        name: 'Total raised',
        data: raised
    }, {
        name: 'Cash on hand',
        data: onhand
    }]
	};
	

</script>

<p><small>Showing data as of {contestData[0].period}</small></p>

<div class="chart" use:highcharts={config}></div>
