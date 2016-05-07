$(document).ready(function() {
    $(function () {
      $('[data-toggle="score-tooltip"]').tooltip();
    });
});

function graphData(correct, incorrect){
    var pieData = {
        labels: [
            "Correct",
            "Incorrect"
        ],
        datasets: [
            {
                data: [correct, incorrect],
                backgroundColor: [
                    "#36A2EB","#FF6384"

                ],
                hoverBackgroundColor: [
                    "#36A2EB",
                    "#FF6384"

                ]
            }]
    };
    var ctx =  $("#correct-incorrect-chart");
    var incorrectGraph = new Chart(ctx,{
        type: 'pie',
        data: pieData
    });
}

function graphOverTime(xpts, ypts){
    var data = {
    labels: xpts,
    datasets: [{
        label: "Questions Answered",
            fill: false,
            lineTension: .2,
            backgroundColor: "rgba(75,192,192,0.4)",
            borderColor: "rgba(75,192,192,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(75,192,192,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(75,192,192,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data: ypts
    }]
    };

    var ctx = $("#overtime-chart");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: data
     });

}
