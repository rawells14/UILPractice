$(document).ready(function() {
    hideAll();
    $("#open-question").click(function(){
        hideAll();
        $("#question-wrapper").show();
    });
    $("#open-feedback").click(function(){
        hideAll();
        $("#feedback-wrapper").show();
    });
});

function hideAll(){
    $("#question-wrapper").hide();
    $("#feedback-wrapper").hide();
}