    function showEditPopup(url) {
        var win = window.open(url, "Edit",
            'height=500,width=800,resizable=yes,scrollbars=yes');
        return false;
    }
    function showAddPopup(triggeringLink) {
        console.log('adicionar nova categoria')
        var name = triggeringLink.id.replace(/^add_/, '');
        console.log('variavel name: ', name)
        href = triggeringLink.href;
        console.log('variavel href: ', href)
        var win = window.open(href, name, 'height=500,width=800,resizable=no,scrollbars=no');
        win.focus();
        return false;
    }
    function closePopup(win, newID, newRepr, id) {
        $(id).append('<option value=' + newID + ' selected >' + newRepr + '</option>')
        win.close();
    }
    $("#edit_author").click(function(){
        author_name = $("#id_author option:selected").text();
        var data = {"author_name":author_name};
        $.ajax({
            type : 'GET',
            url :  '/author/ajax/get_author_id',
            data : data,
            success : function(data){
                var url = "/author/" + data['author_id'] + "/edit/";
                showEditPopup(url);
            },
            error: function(data) {
              alert("Something Went Wrong");
            }
        });
    })
