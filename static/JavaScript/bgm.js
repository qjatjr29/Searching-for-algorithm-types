const BGM_container = document.querySelector(".BGM");
const BGM_button = BGM_container.querySelector(".BGM__button");
const BGM_icon = BGM_button.querySelector("i");
const BGM_NUMBER = 6;
var audio = new Audio();

function playBgm() {
    let audioNumber = Math.floor(Math.random() * BGM_NUMBER);
    audio.src = `../static/bgm/${audioNumber + 1}.mp3`;
    audio.play();
    BGM_button.classList.add("playing");
    BGM_icon.classList.replace("fa-play", "fa-volume-mute");
    audio.addEventListener("ended", function () {
        audioNumber = Math.floor(Math.random() * BGM_NUMBER);
        this.src = `../static/bgm/${audioNumber + 1}.mp3`;
        this.currentTime = 0;
        this.play();
    }, false);
}
function pauseBgm() {

    audio.pause();
    // BGM_button.innerHTML = "BGM";
    BGM_icon.classList.replace("fa-volume-mute", "fa-play");
    // BGM_button.innerHTML = `<i class="fas fa-music fa-2x"></i>`;

    BGM_button.classList.remove("playing");
}

function checkPlaying(event) {
    event.preventDefault();
    // console.log(BGM_button.classList.contains("playing"));
    if (BGM_button.classList.contains("playing")) {

        pauseBgm();
    }
    else {
        playBgm();
    }
}



function init() {
    BGM_button.addEventListener("click", checkPlaying);
}

init();