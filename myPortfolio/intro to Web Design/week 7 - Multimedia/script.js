

function playPauseMedia() {
    fixPlay();

    if (media.paused) {
        play.setAttribute('data-icon', 'u');
        media.play();
    } else {
        play.setAttribute('data-icon', 'P');
        media.pause();
    }
}


/*

document.getElementById("Button1").addEventListener("click", function () {.......} );

play.addEventListener('click', playPauseMedia);
stop.addEventListener('click', stopMedia);
media.addEventListener('ended',stopMedia);
rwd.addEventListener('click', mediaBackward);
fwd.addEventListener('click', mediaForward);
media.addEventListener('timeupdate',setTime);




*/

function doChat() {   // kripken speakClient
    event.preventDefault();
    text = document.querySelector('input');
    speak(text.value);
}