$( document ).ready(function() {
    var page = window.location.pathname;
    console.log(page)
    if(page == "/cs"){
        $("#cs").addClass("active");
    }
    else if(page== "/math"){
        $("#math").addClass("active");
    }else if(page == "/dashboard"){
        $("#dashboard").addClass("active");
    }
});

function clearStates(){
    $("#nav-buttons>li").removeClass("active");
}