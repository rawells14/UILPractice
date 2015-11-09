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

    console.log(pieData[0].value)
    var ctx = document.getElementById("correct-incorrect-chart").getContext("2d");
    var correctIncorrectChart = new Chart(ctx).Pie(pieData);
}


function getColor(percentage){
    var colors = ["#AA3939", "#AA6939", "#AA9239", "#68C21D", "#148282"];
    var percents = [50, 60, 70, 80, 90]
    var color = "";
    for(i = percents.length; i >= 0; i++){
        if(percentage >= percents[i]){
            return colors[i];
        }
    }
    return colors[0];
}

function changeColor(percentage){
    $("#accuracy-percent").css('color', getColor(percentage));
}