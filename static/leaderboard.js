function graphDataScore(usernames, scores){
    var data = {
    labels: usernames,
    datasets: [
        {
            label: "Score",
            fillColor: "#7060B4",
            highlightFill: "#523F9E",
            data: scores
        }
    ]
};

        var ctx = document.getElementById("top-ten-graph").getContext("2d");
        var topTenChart = new Chart(ctx).Bar(data);
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