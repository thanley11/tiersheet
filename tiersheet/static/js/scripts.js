$(function() {
         $(".highlight").dblclick(function(){ 
    $(this).toggleClass('highlighted');
    });
});
$(document).on("click","#toggleStar", function()   {  
        var player_id = $(this).attr("data-playerid");
        $.ajax
        ({ 
            type: "POST",
            url: "{% url 'toggleStar' %}", 
            data: {'player_id': player_id, 'csrfmiddlewaretoken': '{{csrf_token}}'},
            success: function(data){
                // if ($(this).hasClass("glyphicon.glyphicon-star")) {
                    $(this).find('i').toggleClass("glyphicon-star glyphicon-star-empty");
                    // $(this).removeClass("glyphicon.glyphicon-star").addClass("glyphicon.glyphicon-star-empty");
                //} else {
                    //  $(this).removeClass("glyphicon.glyphicon-star-empty").addClass("glyphicon.glyphicon-star");
                // }
                //$this.toggleClass('glyphicon-star-empty glyphicon-star'); 
                }
            });
        });
