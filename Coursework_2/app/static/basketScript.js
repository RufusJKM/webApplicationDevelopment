$(document).ready(function() {

    // Set the token so that we are not rejected by server
      var csrf_token = $('meta[name=csrf-token]').attr('content');
    // Configure ajaxSetup so that the CSRF token is added to the header of every request
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });
    console.log("before for");
    var removeAll = document.getElementsByClassName('removeButton');
    var minus = document.getElementsByClassName("minus");
    var plus = document.getElementsByClassName("plus");
    var i = 0;
    var len = removeAll.length;
    for (i; i < len; i++){
        console.log("inside for");
        $(removeAll[i]).click(function(){
            var buttonID = this.id;
            var parts = buttonID.split(",");
            var productID = parts[1];
            console.log(buttonID);
            console.log(productID);
        });

        $(minus[i]).click(function(){
            var buttonID = this.id;
            var parts = buttonID.split(",");
            var productID = parts[1];
            console.log(buttonID);
            console.log(productID);
        });

        $(plus[i]).click(function(){
            var buttonID = this.id;
            var parts = buttonID.split(",");
            var productID = parts[1];
            console.log(buttonID);
            console.log(productID);
        });
    }

});