<script>

  export let contestData;
	import highcharts from './highcharts';

  function makeIdSlug(office) {
    return office.replace(" ", "-").toLowerCase();
  }

  let periods = [...new Set(contestData.map(value=>value.period))]
  let currentPeriod = periods[0];
  let candidates = []
  let raised = []
  let onhand = []

  let currentContestData = contestData.filter(item => item.period == currentPeriod);
  currentContestData.forEach(i => candidates.push(i.candidate + " (" + i.party + ")") && raised.push(parseFloat(i.raised)) && onhand.push(parseFloat(i.onhand)));

  let styleGeneral = {
    fontFamily: '"Open Sans", Helvetica, Arial, "Lucida Grande", sans-serif',
    fontSize: '18px',
    fontWeight: 'normal',
    color: "#676767"
  }

  let baseHeight = 300;
  if (candidates.length > 2) {baseHeight = 450};
  if (candidates.length > 5) {baseHeight = 550};
  if (candidates.length > 7) {baseHeight = 650};

  let config = {
    chart: {
      type: "bar",
    },
    credits: {enabled: false},
    colors: ['#0D57A0', '#0793AB'],
    plotOptions: {
      series: {
        states: {
          inactive: {
            enabled: false
          }
        }
      }
    },
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

  function handleSelect() {
    currentContestData = contestData.filter(item => item.period == currentPeriod);
    candidates = []
    raised = []
    onhand = []
    currentContestData.forEach(i => candidates.push(i.candidate + " (" + i.party + ")") && raised.push(parseFloat(i.raised)) && onhand.push(parseFloat(i.onhand)));
    config.xAxis.categories = candidates;
    config.series[0].data = raised;
    config.series[1].data = onhand;
    if (candidates.length > 2) {baseHeight = 450};
    if (candidates.length > 5) {baseHeight = 550};
    if (candidates.length > 7) {baseHeight = 650};
  }

  function dateParse(d) {
    let dt = new Date(d)
    return dt.toLocaleString("en-US", {month: "long", day: "numeric", year: "numeric"})
  }
	

</script>

<style>

  .contest {
    border-bottom: 1px solid #d6d6da;
		margin-bottom: 1.5em;
		padding-bottom: .75em;
  }

  .contest h4 {
    margin-bottom: 0.25em;
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

  small {
    font-size: .7em;
  }

  .selected {
    font-weight: 700;
  }

  @media screen and (max-width: 960px) {
    table {
      font-size: 0.7em;
    }
  } 
</style>

<div class="contest" id="{makeIdSlug(contestData[0].office)}">
  <h4>{contestData[0].office}</h4>
  <div><small>Showing data for fundraising period {#if periods.length == 1}<strong>{currentPeriod}</strong>{:else} 
    
    <select bind:value={currentPeriod} on:change="{handleSelect}">{#each periods as period}
    
      <option value="{period}">{period}</option>
   
    {/each}</select>{/if},
  
  which goes from  {dateParse(currentContestData[0].periodstart)} to {dateParse(currentContestData[0].periodend)}.</small></div>
  

  <div class="chart" use:highcharts={config} style="height: {baseHeight}px;"></div>

  <table>
    <thead>
      <tr><th>Candidate</th><th>Party</th><th class="right">Total raised</th><th class="right">Cash on hand</th><th class="right">Link to filing</th></tr>
    </thead>
    <tbody>
      {#each currentContestData as candidate}
        <tr><td>{candidate.candidate}</td><td>{candidate.party}</td><td class="right">{parseFloat(candidate.raised).toLocaleString('en-US')}</td><td class="right">{parseFloat(candidate.onhand).toLocaleString('en-US')}</td><td class="right">{#if candidate.link}<a href="{candidate.link}">Filing <i class="fas fa-file"></i></a>{/if}</td></tr>
      {/each}
    </tbody>

  </table>
</div>
