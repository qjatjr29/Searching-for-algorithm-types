const mainimg = document.querySelector(".main_img");
const IMG_NUM = 4;

function displayImage() {
    const ImageNumber = Math.floor(Math.random() * IMG_NUM);
    const background_img = new Image();
    // background_img.src = `../static/img/${ImageNumber + 1}.jpg`;
    // background_img.src = "{{ url_for('static',filename = img/" + `${ImageNumber + 1}` + ".jpg) }}";
    background_img.src = `../static/img/${ImageNumber + 1}.jpg`;
    background_img.classList.add("backgroundIMG");
    mainimg.appendChild(background_img);
}



function init() {
    displayImage();
}

init();