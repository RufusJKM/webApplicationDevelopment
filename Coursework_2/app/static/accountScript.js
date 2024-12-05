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

      $('#logOut').click(function(){
        console.log("Clicked log out");
        $.ajax({
            // Specify the endpoint URL the request should be sent to.
            url: '/logOut',
            // The request type.
            type: 'POST',
            // The data, which is now most commonly formatted using JSON because of its
            // simplicity and is native to JavaScript.
            data: JSON.stringify({ information: "logOut" }),
            // Specify the format of the data which will be sent.
            contentType: "application/json; charset=utf-8",
            // The data type itself.
            dataType: "json",
            // Define the function which will be triggered if the request is received and
            // a response successfully returned.
            success: function(response){
                console.log(response);
                window.location = '/';
            },
            // The function which will be triggered if any error occurs.
            error: function(error){
                console.log(error);
            }
          });
    });
});