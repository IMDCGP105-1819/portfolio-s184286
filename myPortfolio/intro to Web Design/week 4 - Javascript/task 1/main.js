
document.querySelector('html').style.backgroundColor='red';



// 1. COMPLETE VARIABLE AND FUNCTION DEFINITIONS

var customName = document.getElementById('customname');
var randomize = document.querySelector('.randomize');
var story = document.querySelector('.story');

function randomValueFromArray(array){
  return array[Math.floor(Math.random()*array.length)];
}

// 2. RAW TEXT STRINGS

var storyText = "It was 94 farenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but he was not surprised — :insertx: weighs 300 pounds, and it was a hot day."

var insertX = ["Willy the Goblin", "Big Daddy", "Father Christmas"];

var insertY = ["the soup kitchen","Disneyland","the White House"];

var insertZ = ["spontaneously combusted","melted into a puddle on the sidewalk","turned into a slug and crawled away"];


// 3. EVENT LISTENER AND PARTIAL FUNCTION DEFINITION

randomize.addEventListener('click', result);

function result() {

var newStory = storyText

var xitem = randomValueFromArray(insertX)
var yitem = randomValueFromArray(insertY)
var zitem = randomValueFromArray(insertZ)

newStory = newStory.replace(":insertx:", xitem)
newStory = newStory.replace(":inserty:", yitem)
newStory = newStory.replace(":insertz:", zitem)

  if(customName.value != '') {
    var name = customName.value;
    newStory = newStory.replace("bob",name)
  }

  if(document.getElementById("uk").checked) {
    var weight = Math.round(300/14) +" stone";
    var temperature =  Math.round(((94 - 32) * 5) / 9) + " celsius";
    
  }

  story.textContent = newStory;
  story.style.visibility = 'visible';
}
