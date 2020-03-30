/**
 * Handle main page Events.
 *
 * Manipulação dos eventos da página principal
 *
 * @version    1.0.0
 * @package    VocatioTelecom
 * @subpackage js
 * @author     Alcindo Schleder <alcindoschleder@gmail.com>
 *
 */

var IndexEvents = function () {

    var documentEvents = function () {
        $('.edit-movie').click(function (e) {
            e.preventDefault();
            url = $(this).attr('data-link');
            window.location.href = url
        })
        $('.idelete-movie').click(function (e) {
            e.preventDefault();
            url = $(this).attr('data-link');
            if (BaseEvents.Confirm('Did You wish delete this record?')) {
                sendAjaxOverride(url, 'DELETE', 'Record deleted successfully!')
            }
        });
        $('.ilike').click(function (e) {
            e.preventDefault();
            url = $(this).attr('data-link');
            sendAjaxOverride(url, 'PUT')
        });
        $('.idislike').click(function (e) {
            e.preventDefault();
            url = $(this).attr('data-link');
            sendAjaxOverride(url, 'PATH')
        });
    };
    var sendAjaxOverride = function (url, method, msg = '', urlRedirect = '/') {
        href = window.location.href
        $.ajaxSetup({
             beforeSend: function(xhr, settings) {
                 function getCookie(name) {
                     var cookieValue = null;
                     if (document.cookie && document.cookie != '') {
                         var cookies = document.cookie.split(';');
                         for (var i = 0; i < cookies.length; i++) {
                             var cookie = jQuery.trim(cookies[i]);
                             // Does this cookie string begin with the name we want?
                             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                 break;
                             }
                         }
                     }
                     return cookieValue;
                 }
                 if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                     // Only send the token to relative URLs i.e. locally.
                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                 }
             }
        });
        $.ajax({
            url: url,
            type: 'POST',
            success: function () {
                if (msg) alert(msg);
                window.location.href = href
            },
            headers: { 'x-MethodOverride': method }
        });
    };
    var hidePage = function (page, url) {
    };
    var showPage = function (page, url) {
    };

    return {
        //main function to initiate the module
        init: function () {
            documentEvents();
        }
    };
}();

$(document).ready(function() {
    IndexEvents.init(); // starting home page events
});
