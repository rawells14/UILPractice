function graphData(usernames, scores){


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