/**
 * Handle movies page Events.
 *
 *
 * @version    1.0.0
 * @package    i-city
 * @subpackage js
 * @author     Alcindo Schleder <alcindoschleder@gmail.com>
 *
 */

var MoviesEvents = function () {
    var win = null

    var documentEvents = function () {
        $("#add-category").click(function() {
            href = $(this).attr('data-link')
            showPopup(href, 'New');
            return false;
        });
        $("#edit-category").click(function() {
            console.log('click on #edit-category')
            dsc_category = $("#fk_movies_category option:selected").text();
            var data = {"dsc_category": dsc_category};
            $.ajax({
                type : 'GET',
                url :  '/category/ajax/get_category_id',
                data : data,
                success : function(data) {
                    var url = "/category/" + data['movies_category_id'];
                    showPopup(url, 'Edit');
                },
                error: function(data) {
                  alert("Something Went Wrong");
                }
            });
        });
    }
    var closePopup = function (win, newID, newRepr, id) {
        console.lgo('testing win var ', win);
        if (!win) return false;
        console.lgo('Appending value ', newID, newRepr, ' on ', id);
        $(id).append('<option value=' + newID + ' selected >' + newRepr + '</option>')
        console.lgo('Closing popup! ');
        win.close();
        win = null
        console.lgo('popup closed!');
    };
    var showPopup = function (href, oper) {
        win = window.open(href, document.title + '- ' + oper, 'height=600,width=1000,resizable=no,scrollbars=no');
        win.focus();
    };

    return {
        //main function to initiate the module
        init: function () {
            documentEvents();
        },
        closeWindow: function (win, newID, newRepr, id) {
            console.log('callingo close window')
            closePopup(win, newID, newRepr, id);
        }
    };
}();

$(document).ready(function() {
    MoviesEvents.init(); // starting home page events
});
