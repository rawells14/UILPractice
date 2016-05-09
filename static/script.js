$( document ).ready(function() {
    var page = window.location.pathname;
    if(page.includes("cs")){
        $("#cs").addClass("active");
    }
    else if(page.includes("math")){
        $("#math").addClass("active");
    }else if(page == "/dashboard"){
        $("#dashboard").addClass("active");
    }
    $('#begin-cs').on('click', function () {
        var $btn = $(this).button('loading')
        setTimeout(function(){
        window.location.replace("/cs/new");
     }, 600);
     });
  $('#begin-math').on('click', function () {
        var $btn = $(this).button('loading')
        setTimeout(function(){
        window.location.replace("/math/new");
         }, 600);
  });
  $('.carousel').carousel({
             interval: 4500,
             wrap: true,
             pause: false
         });
});

function clearStates(){
    $("#nav-buttons>li").removeClass("active");
}