function Hamburger() {
    var x = document.getElementById("TheHeader");
    if (x.className === "header-right") {
      x.className += " responsive";
    } else {
      x.className = "header-right";
    }
  }