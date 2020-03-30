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

    var documentEvents = function () {
        $(".btn-back").click(function (e) {
            window.location.href = '/'
        });
        $("#add-category").click(function() {
            href = $(this).attr('data-link')
            showPopup(href, 'New');
            return false;
        });
        $("#edit-category").click(function() {
            pk = $("#id_fk_movies_category option:selected").val();
            var url = "/category/" + pk;
            showPopup(url, 'Edit');
        });
    }
    var closePopup = function (win, newID, newRepr, id) {
        $(id).append('<option value=' + newID + ' selected >' + newRepr + '</option>')
        win.close();
    };
    var showPopup = function (href, oper) {
        var win = window.open(href, document.title + '- ' + oper, 'height=600,width=1000,resizable=no,scrollbars=no');
        win.focus();
    };

    return {
        //main function to initiate the module
        init: function () {
            documentEvents();
        },
        closeWindow: function (win, newID, newRepr, id) {
            closePopup(win, newID, newRepr, id);
        }
    };
}();

$(document).ready(function() {
    MoviesEvents.init(); // starting home page events
});
