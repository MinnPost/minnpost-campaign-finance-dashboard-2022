<script>

  export let contestData;
	import highcharts from './highcharts';

  let candidates = []
  let raised = []
  let onhand = []

  contestData.forEach(i => candidates.push(i.candidate + " (" + i.party + ")") && raised.push(parseFloat(i.raised)) && onhand.push(parseFloat(i.onhand)));

  let styleGeneral = {
    fontFamily: '"Open Sans", Helvetica, Arial, "Lucida Grande", sans-serif',
    fontSize: '18px',
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

<style>

  .contest {
    border-bottom: 1px solid #d6d6da;
		margin-bottom: 1.5em;
		padding-bottom: .75em;
  }

  .right {
    text-align: right;
  }

  table {
    width: 100%;
    font-family: Arial, Helvetica, sans-serif;
    font-size: .8em;
    line-height: 1.5em;
    text-align: left;
  }

  tr:nth-child(even) td {
    background-color: #F8F8F8;
  }

  th {
    vertical-align: bottom;
    border-bottom: 2px solid #cccccc;
    padding: 0.5em 0.5em 0 0.5em;
  }

  td {
    padding: 0.5em;
    vertical-align: middle;
  }
</style>

<div class="contest">
  <h4>{contestData[0].office}</h4>
  <p><small>Showing data as of {contestData[0].period}.</small></p>

  <div class="chart" use:highcharts={config}></div>

  <table>
    <thead>
      <tr><th>Candidate</th><th>Party</th><th class="right">Total raised</th><th class="right">Cash on hand</th><th class="right">Link to filing</th></tr>
    </thead>
    <tbody>
      {#each contestData as candidate}
        <tr><td>{candidate.candidate}</td><td>{candidate.party}</td><td class="right">{parseFloat(candidate.raised).toLocaleString('en-US')}</td><td class="right">{parseFloat(candidate.onhand).toLocaleString('en-US')}</td><td>{#if candidate.link}<a href="{candidate.link}">Filing <i class="fas fa-document"></i></a>{/if}</td></tr>
      {/each}
    </tbody>

  </table>
</div>
