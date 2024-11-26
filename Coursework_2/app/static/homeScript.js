document.getElementById('quantity').addEventListener('change', function() {
    // Get the selected value
    const val = this.options[this.selectedIndex].value;
    
    //requires AJAX to get price from db

    //parse as float for multiplication
    var newPrice = parseFloat(price, 10);
    newPrice = newPrice*val

    //Add back £ to the start
    newPrice = "£".concat(newPrice);
    document.getElementById('price').innerHTML = newPrice;
  });

function addToBasket() {
    dropdown = document.getElementById("quantity")
    quantity = dropdown.value;

    //needs ajax for db manipulation
}