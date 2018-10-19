var displayedImage = document.querySelector('.displayed-img');
var thumbBar = document.querySelector('.thumb-bar');

btn = document.querySelector('button');
var overlay = document.querySelector('.overlay');

/* Looping through images */


/* Wiring up the Darken/Lighten button */

for (var i =1; i<6;i++){
  var newImage = document.createElement('img');
  newImage.setAttribute('src', "images/pic"+i+".jpg");
  thumbBar.appendChild(newImage);
  newImage.addEventListener("click", thumbClicked);
}

function thumbClicked(event) {
  console.log(event.target.getAttribute('src'));
}
