function graphDataScore(usernames, scores){
    var data = {
    labels: usernames,
    datasets: [
        {
            label: "My First dataset",
            backgroundColor: "rgba(255,99,132,0.2)",
            borderColor: "rgba(255,99,132,1)",
            borderWidth: 1,
            hoverBackgroundColor: "rgba(255,99,132,0.4)",
            hoverBorderColor: "rgba(255,99,132,1)",
            data: scores
        }
    ]
};

        var ctx = $("top-ten-graph");
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
                label: "Accuracy",
                fillColor: "#7060B4",
                highlightFill: "#523F9E",
                data: accuracies
            }
        ]
    };

        var ctx = document.getElementById("most-accurate-graph").getContext("2d");
        var accurateGraph = new Chart(ctx).Bar(data);
}