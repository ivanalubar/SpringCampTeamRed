$(document).ready(function(){
    $('#data').jstree({
        "core" : {
        "check_callback" : true
        },
        "plugins": [
            "wholerow",
            "contextmenu",
            "dnd",
            "state",
            "massload",
            "search",
            "types",
            ""
        ]
    });

    $('#data').on("changed.jstree", function(e, data){
        if(data.selected.length){
            $(data.selected).each(function(idx){
                var node = data.instance.get_node(data.selected[idx]);
                console.log('The selected node is: ' + node.text);

            });
        }
    });
});