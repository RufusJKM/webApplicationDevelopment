var dropdowns = document.getElementsByClassName('quantity');
var len = dropdowns.length;
var i = 0;
for (i; i < len; i++) {
  dropdowns[i].addEventListener('change', function(event) {

    // Get the selected value
    const val = this.options[this.selectedIndex].value;
    var item = this.name;

    //requires AJAX to get price from db
    $.ajax({
      // Specify the endpoint URL the request should be sent to.
      url: '/changePrice',
      // The request type.
      type: 'POST',
      // The data, which is now most commonly formatted using JSON because of its
      // simplicity and is native to JavaScript.
      data: JSON.stringify({ response: item }),
      // Specify the format of the data which will be sent.
      contentType: "application/json; charset=utf-8",
      // The data type itself.
      dataType: "json",
      // Define the function which will be triggered if the request is received and
      // a response successfully returned.
      success: function(response){
          console.log(response);

          var newPrice = val*response; 
          console.log(newPrice)
      },
      // The function which will be triggered if any error occurs.
      error: function(error){
          console.log(error);
      }
    });

    
    //parse as float for multiplication
    console.log(newPrice)

    //Add back £ to the start
    newPrice = "£".concat(newPrice);
    //document.getElementById('price').innerHTML = newPrice;
  });
}

function addToBasket() {
    dropdown = document.getElementById("quantity")
    quantity = dropdown.value;

    //needs ajax for db manipulation
}