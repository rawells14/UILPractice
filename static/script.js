$( document ).ready(function() {
    $("#cs").click(function(){
        clearStates();
        $("#cs").addClass("active");
    });
    $("#math").click(function(){
        clearStates();
        $("#math").addClass("active");
    });
});

function clearStates(){
    $("#nav-buttons>li").removeClass("active");
}