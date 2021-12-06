
// Welkom bij de divs javascript ja hier gaat die dus kijken naar een element met class naam "collapsible" en als die die gevonden heeft dan gaat die dan naar
// zon button zoeken en als die n button heeft gevonden gaat die wachten op click event en dan poef open hij de div met een magische animatie!!

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}