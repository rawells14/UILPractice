var cor = 10;
var explan = "";
var isCor;
var chosen;
function init(correct, explanation){
    cor = correct;
    explan = explanation

}

$(document).ready(function() {
    $("#answer-choices a").click(function() {
        chosen = this.id;
        if(chosen == cor){
            isCor = true;
            correct();
        }else{
            incorrect();
            isCor = false;
        }
    });
    $(".explanation").html(explan);
    $("#correct").hide();
    $("#incorrect").hide();
});

function incorrect(){
    $("#answer-choices a").each(function(index){
        if(this.id == cor){
            $(this).addClass("list-group-item-success");
            $(this).removeClass("list-group-item-info");

        }else if(this.id == chosen){
            $(this).removeClass("list-group-item-info");
            $(this).addClass("list-group-item-danger");

        }
        else{
            $(this).addClass("list-group-item disabled");
        }
    });
    $("#incorrect").slideDown("slow");
}
function correct(){
    $("#answer-choices a").each(function(index){
        if(this.id == cor){
            $(this).addClass("list-group-item-success");
            $(this).removeClass("list-group-item-info");

        }else{
            $(this).addClass("list-group-item disabled");
        }
    });
    $("#correct").slideDown("slow");
}