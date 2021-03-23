const clock = document.querySelector(".clock");
const clockText = clock.querySelector("h1");
const dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


function getTime() {
    const CurrentTime = new Date();
    const hours = CurrentTime.getHours();
    const minutes = CurrentTime.getMinutes();
    clockText.innerText = `${hours < 10 ? `0${hours}` : hours} : ${minutes < 10 ? `0${minutes}` : minutes} `;

}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();