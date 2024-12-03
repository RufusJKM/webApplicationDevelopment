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

  var dropdowns = document.getElementsByClassName('quantity');
  var buttons = document.getElementsByClassName("addButton");
  var len = dropdowns.length;
  var currentValues = [];
  var i = 0;
  for (i; i < len; i++) {
    //array stores product values
    currentValues.push(1);
  }
  i = 0;
  var newPrice = 0;
  for (i; i < len; i++) {
    //array stores product values
    //function to update price using dropdown
    $(dropdowns[i]).change(function() {

      // Get the selected value
      var item = this.id;
      var name = this.name;
      var val = this.options[this.selectedIndex].value;
      currentValues[item - 1] = val;


      //requires AJAX to get price from db
      $.ajax({
        // Specify the endpoint URL the request should be sent to.
        url: '/changePrice',
        // The request type.
        type: 'POST',
        // The data, which is now most commonly formatted using JSON because of its
        // simplicity and is native to JavaScript.
        data: JSON.stringify({ prodID: item }),
        // Specify the format of the data which will be sent.
        contentType: "application/json; charset=utf-8",
        // The data type itself.
        dataType: "json",
        // Define the function which will be triggered if the request is received and
        // a response successfully returned.
        success: function(response){
            var originalPrice = response["response"];

            //update price
            newPrice = val*originalPrice;
            newPrice = newPrice.toFixed(2); 
            console.log(newPrice)
            console.log(name)

            //change price on page
            newPrice = "£".concat(newPrice);
            document.getElementById(name.concat('price')).innerHTML = newPrice;
        },
        // The function which will be triggered if any error occurs.
        error: function(error){
            console.log(error);
        }
      });
    });
    
    //add to basket function
    $(buttons[i]).click(function(){
      //get button id and split to find the product id
      var buttonID = this.id;
      var parts = buttonID.split(",");
      var productID = parts[1];

      //get the number to be added to basket
      var val = currentValues[productID - 1];

      //send information to backend
      $.ajax({
        // Specify the endpoint URL the request should be sent to.
        url: '/addToBasket',
        // The request type.
        type: 'POST',
        // The data, which is now most commonly formatted using JSON because of its
        // simplicity and is native to JavaScript.
        data: JSON.stringify({ pID: productID, quantity: val }),
        // Specify the format of the data which will be sent.
        contentType: "application/json; charset=utf-8",
        // The data type itself.
        dataType: "json",
        // Define the function which will be triggered if the request is received and
        // a response successfully returned.
        success: function(response){
            console.log(response);
        },
        // The function which will be triggered if any error occurs.
        error: function(error){
            console.log(error);
        }
      });
    });
  }
});

