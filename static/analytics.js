$(document).ready(function() {
    $(function () {
      $('[data-toggle="score-tooltip"]').tooltip();
    });

});

function graphData(correct, incorrect){
var pieData = [{
    value: correct,
    label: Math.round((correct)/(correct+incorrect)*100) +"% Correct",
    color: "#68D141",
    highlight: "#339F0B"
},{
    value: incorrect,
    label: Math.round((incorrect)/(correct+incorrect)*100)+"% Incorrect",
    color: "#F54C4C",
    highlight: "#BA0C0C"
}];
    var ctx = document.getElementById("correct-incorrect-chart").getContext("2d");
    var correctIncorrectChart = new Chart(ctx).Pie(pieData);
}

function graphOverTime(xpts, ypts){
    var data = {
    labels: xpts,
    datasets: [
        {
            label: "Questions Answered",
            fill: true,
            lineTension: .1,
            backgroundColor: 'rbga(89, 85, 148,1)',
            borderColor: "rgba(75,192,192,1)",
            borderCapStyle: 'butt',
            borderDash: [],
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(75,192,192,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 1,
            pointHoverBackgroundColor: "rgba(75,192,192,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 1,
            data: ypts,
            }
    ]
    };

    var ctx = document.getElementById("overtime-chart").getContext("2d");
    var correctIncorrectChart = new Chart(ctx).Line(data);
}
