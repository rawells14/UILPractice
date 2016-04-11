$(document).ready(function() {
//    $("#badge-holder img").hover(function() {
//        $(this).tooltip();
//        console.log(this);
//    });
    $('#badge-holder').tooltip({
        selector: "img[data-toggle=tooltip]"
    })

});