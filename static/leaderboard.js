function graphData(usernames, scores){


    var data = {
    labels: usernames,
    datasets: [
        {
            label: "Score",
            fillColor: "rgba(220,220,220,0.5)",
            strokeColor: "rgba(220,220,220,0.8)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: scores
        }
    ]
};
        
        var ctx = document.getElementById("top-ten-graph").getContext("2d");
        var topTenChart = new Chart(ctx).Bar(data);
        console.log(usernames)

}