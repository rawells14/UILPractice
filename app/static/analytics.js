function graphData(xLabels, yPts){
var data = {
    labels: xLabels,
    datasets: [
        {
            label: "Accuracy Over Time",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: yPts
        }
    ]

};
console.log(data.labels)
    var ctx = document.getElementById("score-chart").getContext("2d");
    var accuracyChart = new Chart(ctx).Line(data,{
        bezierCurve: true
    });
}
