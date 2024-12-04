$(document).ready(function() {
    //set prices to 2dp
    var prices = document.getElementsByClassName("price");
    for (var i = 0; i < prices.length; i++){
        var currentPrice = prices[i].innerHTML;
        currentPrice = parseFloat(currentPrice.substring(1, currentPrice.length));
        currentPrice = currentPrice.toFixed(2);
        currentPrice = "£".concat(currentPrice);
        prices[i].innerHTML = currentPrice;
    }
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
            var index = parts[2];
            console.log(buttonID);
            console.log(productID);

            $.ajax({
                // Specify the endpoint URL the request should be sent to.
                url: '/addToBasket',
                // The request type.
                type: 'POST',
                // The data, which is now most commonly formatted using JSON because of its
                // simplicity and is native to JavaScript.
                data: JSON.stringify({ pID: productID, quantity: 0 }),
                // Specify the format of the data which will be sent.
                contentType: "application/json; charset=utf-8",
                // The data type itself.
                dataType: "json",
                // Define the function which will be triggered if the request is received and
                // a response successfully returned.
                success: function(response){
                    console.log(response);
                    location.reload();
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
            var index = parts[2];
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
                    if (response["response"] == "deleted"){
                        location.reload()
                    } else {
                        //edit inner html of price and quantity
                    }
                    
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