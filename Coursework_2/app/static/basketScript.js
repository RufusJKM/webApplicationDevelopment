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
    var removeAll = document.getElementsByClassName('removeButton');
    var minus = document.getElementsByClassName("minus");
    var plus = document.getElementsByClassName("plus");
    var quantities = document.getElementsByClassName("quantity")
    var i = 0;
    var len = removeAll.length;
    for (i; i < len; i++){
        //three different buttons all altering basket
        //reusing addToBasket function just adding functioanilty to remove

        $(removeAll[i]).click(function(){
            var buttonID = this.id;
            var parts = buttonID.split(",");
            var productID = parts[1];
            var quantity = quantities[productID-1];
            quantity = 0 - quantity;
            console.log(buttonID);
            console.log(productID);

            $.ajax({
                // Specify the endpoint URL the request should be sent to.
                url: '/addToBasket',
                // The request type.
                type: 'POST',
                // The data, which is now most commonly formatted using JSON because of its
                // simplicity and is native to JavaScript.
                data: JSON.stringify({ pID: productID, quantity: quantity }),
                // Specify the format of the data which will be sent.
                contentType: "application/json; charset=utf-8",
                // The data type itself.
                dataType: "json",
                // Define the function which will be triggered if the request is received and
                // a response successfully returned.
                success: function(response){
                    console.log(response);
                    //reload page
                },
                // The function which will be triggered if any error occurs.
                error: function(error){
                    console.log(error);
                }
              });
            });
        
        $(minus[i]).click(function(){
            var buttonID = this.id;
            var parts = buttonID.split(",");
            var productID = parts[1];
            var quantity = quantities[productID-1];
            console.log(buttonID);
            console.log(productID);

            $.ajax({
                // Specify the endpoint URL the request should be sent to.
                url: '/addToBasket',
                // The request type.
                type: 'POST',
                // The data, which is now most commonly formatted using JSON because of its
                // simplicity and is native to JavaScript.
                data: JSON.stringify({ pID: productID, quantity: -1 }),
                // Specify the format of the data which will be sent.
                contentType: "application/json; charset=utf-8",
                // The data type itself.
                dataType: "json",
                // Define the function which will be triggered if the request is received and
                // a response successfully returned.
                success: function(response){
                    console.log(response);
                    //edit inner html of price and quantity
                },
                // The function which will be triggered if any error occurs.
                error: function(error){
                    console.log(error);
                }
              });
        });

        $(plus[i]).click(function(){
            var buttonID = this.id;
            var parts = buttonID.split(",");
            var productID = parts[1];
            var quantity = quantities[productID-1];
            console.log(buttonID);
            console.log(productID);

            $.ajax({
                // Specify the endpoint URL the request should be sent to.
                url: '/addToBasket',
                // The request type.
                type: 'POST',
                // The data, which is now most commonly formatted using JSON because of its
                // simplicity and is native to JavaScript.
                data: JSON.stringify({ pID: productID, quantity: 1 }),
                // Specify the format of the data which will be sent.
                contentType: "application/json; charset=utf-8",
                // The data type itself.
                dataType: "json",
                // Define the function which will be triggered if the request is received and
                // a response successfully returned.
                success: function(response){
                    console.log(response);
                    //edit inner html of price and quantity
                },
                // The function which will be triggered if any error occurs.
                error: function(error){
                    console.log(error);
                }
              });
        });
    }

});