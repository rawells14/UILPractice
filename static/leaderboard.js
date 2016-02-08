function graphData(names, scores){
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