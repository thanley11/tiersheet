$(function() {

    $(".player11").sortable({ 
//       #QBs, #RBs, #WRs, #TEs, #DEFs, #Ks
        connectWith: ".sortable",
        update: function(event, ui){                                             
            var qb_order = $("#QBs").sortable('toArray',{attribute:'data-pid'});
            var rb_order = $("#RBs").sortable('toArray',{attribute:'data-pid'});
            console.log(qb_order, rb_order);                                                                                                                         
            $.ajax({
                type: "POST",
                url: $SCRIPT_ROOT + "/sort/",
                contentType: "application/json; charset=utf-8",
                // this was causing problems reading the variable items and returning undefined values
                data: {'pid' : qb_order+','+rb_order},
                // []=2[]=1
                success: function(data) {
                    console.log(data);
                },
                dataType: "json",
               });                                            
        }                                                                        
     });

    $("#xQBs").sortable({                                                    
        connectWith: ".connectedSortable",

        update: function(event, ui){                                             
           var serial = $('#QBs').sortable('serialize');                                                                                                                         
            $.ajax({
                type: "POST",
                url: "/", 
                data: {'content': serial, 'csrfmiddlewaretoken': '{{csrf_token}}'} 
                });   
            },                                                                        
          });

    $("#xRBs").sortable({
        connectWith: ".connectedSortable",
    });

    $(".player11").click(function(){
        $(this).toggleClass('highlighted');
    });



    });
