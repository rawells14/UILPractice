var cor = 10;
var explan = "";
var isCor;
var chosen;
var answered = false;
var qid;
var subject;

function init(correct, explanation, qid, subject){
    cor = correct;
    explan = explanation
    this.qid = qid;
    this.subject = subject;

}

$(document).ready(function() {
    clearFeedback();
    $("#answer-choices a").click(function() {
        if(answered == false){
            answered = true;
            chosen = this.id;
            if(chosen == cor){
                isCor = true;
                correct();
            }else{
                incorrect();
                isCor = false;
            }
            }
    });
    $(".explanation").html(explan);

    $(function() {
        $('#send-data').click(function() {
        var url_to_submit =
            $.ajax({
                url: '/'+subject+'/submit',
                data: {isCor : ""+isCor, qid : qid},
                type: 'POST',
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
            window.location.replace("/"+subject+"/new");
        });
    });
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
    clearFeedback();
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
    clearFeedback();
    $("#correct").slideDown("slow");
}
function clearFeedback(){
    $("#correct").hide();
    $("#incorrect").hide();
}