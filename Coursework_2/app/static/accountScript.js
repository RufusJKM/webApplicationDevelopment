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
});