const clock = document.querySelector(".clock");
const clockText = clock.querySelector("h1");
const dateText = clock.querySelector("h3");
const dayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


function getTime() {
    const CurrentTime = new Date();
    const hours = CurrentTime.getHours();
    const minutes = CurrentTime.getMinutes();
    // const seconds = CurrentTime.getSeconds();
    const month = CurrentTime.getMonth();
    const years = CurrentTime.getFullYear();
    const date = CurrentTime.getDate();
    let day = CurrentTime.getDay();
    day = dayList[day];
    console.log(dateText);
    clockText.innerText = `${hours < 10 ? `0${hours}` : hours} : ${minutes < 10 ? `0${minutes}` : minutes} `;
    dateText.innerText = `${years}. ${month}. ${date} <br> ${day}`;
}

function init() {
    getTime();
    setInterval(getTime, 1000);
}

init();