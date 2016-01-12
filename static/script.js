$( document ).ready(function() {
    var page = window.location.pathname;
    if(page == "/cs"){
        $("#cs").addClass("active");
    }
    else if(page== "/math"){
        $("#math").addClass("active");
    }else if(page == "/dashboard"){
        $("#dashboard").addClass("active");
    }
    $('#begin-cs').on('click', function () {
    console.log("dank")
    var $btn = $(this).button('loading')
    setTimeout(function(){
    window.location.replace("/cs/question");
     }, 600);

  })
});

function clearStates(){
    $("#nav-buttons>li").removeClass("active");
}