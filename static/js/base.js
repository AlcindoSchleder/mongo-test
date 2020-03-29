var BaseEvents = function () {
    var ConfirmDialog = function (message) {
        if (confirm(message))
            return true;
        else
            return false;
    };
    return {
        //main function to initiate the module
        Confirm: function (msg) {
            return ConfirmDialog(msg);
        }
    };
}();
