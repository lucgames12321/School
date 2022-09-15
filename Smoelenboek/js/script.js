//Code voor het hamburger menu
function Hamburger() {
    var x = document.getElementById("TheHeader");
    if (x.className === "header-right") {
      x.className += " responsive";
    } else {
      x.className = "header-right";
    }
  }




// Code voor de Simple Automatic slider 
var myIndex = 0;
  carousel();
              
  function carousel() {
    var i;
    var x = document.getElementsByClassName("foto");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}    
    x[myIndex-1].style.display = "block";  
    setTimeout(carousel, 5000); // Kaas is lekker ja 5000ms is dus 5 secondjes kan ook langer 
}



// Code voor de Simple Automatic slider2
var myIndex1 = 0;
  carousel1();
              
  function carousel1() {
    var i;
    var x = document.getElementsByClassName("foto1");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
    myIndex1++;
    if (myIndex1 > x.length) {myIndex1 = 1}    
    x[myIndex1-1].style.display = "block";  
    setTimeout(carousel1, 5000); // Kaas is lekker ja 5000ms is dus 5 secondjes kan ook langer 
}