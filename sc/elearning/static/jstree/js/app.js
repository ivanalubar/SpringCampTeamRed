$(document).ready(function(){

    $(document).on('click', '.save_course', function(){
        var v = $('#data').jstree(true).get_json('#', {flat:false})
        var content_json = JSON.stringify(v);

        options = {
        url: "/api/courses/"+COURSE_ID,
        data: {'content':content_json },
        type: "POST",
        dataType: "json"
        };

        options.headers = {'X-CSRFToken': Cookies.get('csrftoken')};
        $.ajax(options).done( function(data){
        console.log(data);
        });
    });

    $('#data').on("changed.jstree", function(e, data){
        if(data.selected.length){
            $(data.selected).each(function(idx){
                var node = data.instance.get_node(data.selected[idx]);
                console.log('The selected node is: ' + node.text);
            });
        }
    });


    $.get("/api/courses/"+COURSE_ID, function(data){
        console.log(data);
        console.log(JSON.parse(data.content));

        $('#data').jstree({
        "core" : {
            "check_callback" : true,
            "data" : JSON.parse(data.content),
            },
            "plugins": [
                "wholerow",
                "contextmenu",
                "dnd",
                "state",
                "massload",
                "search",
                "types",
                "json_data"
            ]
        });
    });
});