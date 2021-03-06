function graphDataScore(usernames, scores){
    var data = {
    labels: usernames,
    datasets: [
        {
            label: "Score",
            backgroundColor: "rgba(255,99,132,0.2)",
            borderColor: "rgba(255,99,132,1)",
            borderWidth: 1,
            hoverBackgroundColor: "rgba(255,99,132,0.4)",
            hoverBorderColor: "rgba(255,99,132,1)",
            data: scores
        }
    ]
};

        var ctx = $("#top-ten-graph");
        var topTen = new Chart(ctx, {
            type: 'bar',
            data: data
});
}
function graphDataAccurate(usernames, accuracies){
     var data = {
    labels: usernames,
    datasets: [
        {
            label: "% Accuracy",
            backgroundColor: "rgba(125, 255, 56,0.2)",
            borderColor: "rgba(125, 255, 56,1)",
            borderWidth: 1,
            hoverBackgroundColor: "rgba(125, 255, 56,0.4)",
            hoverBorderColor: "rgba(125, 255, 56,1)",
            data: accuracies
        }
    ]
};

        var ctx = $("#most-accurate-graph");
        var accurateGraph = new Chart(ctx, {
            type: 'bar',
            data: data
});
}