$( document ).ready(function() {

var data = [1,2,3]
var ctx = document.getElementById("score-chart").getContext("2d");
var myNewChart = new Chart(ctx).Line(data);



});