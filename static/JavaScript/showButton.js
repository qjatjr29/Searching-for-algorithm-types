// const showForm = document.querySelector(".showForm");
const option = document.querySelector(".option");
const showButton = document.querySelector(".showButton");
const showButtonIcon = showButton.querySelector("i");
const todoBox = document.querySelector(".outer__box");

// const hideButton = () => {
//     // e.preventDefault;
//     todoBox.classList.remove("showing");
//     todoBox.classList.add("hide");
//     // todoBox.style.display = "none";
//     showButton.value = "<";
// }
// const openButton = () => {
//     // e.preventDefault;
//     todoBox.classList.add("showing");
//     todoBox.classList.remove("hide");
//     // todoBox.style.display = "block";
//     showButton.value = ">";
// }

// const checkShow = (e) => {
//     if (todoBox.classList.contains("showing")) {
//         hideButton();
//     }
//     else {
//         openButton();
//     }
// }
function toggleSideBar() {
    todoBox.classList.toggle("hide");
    if (todoBox.classList.contains("hide")) {
        option.classList.add("check");
        showButton.classList.remove("buttonUp");
        showButtonIcon.classList.replace("fa-chevron-down", "fa-chevron-left");
    }
    else {
        showButton.classList.add("buttonUp");

        option.classList.remove("check");
        showButtonIcon.classList.replace("fa-chevron-left", "fa-chevron-down");
    }
}

function init() {
    showButton.addEventListener("click", toggleSideBar);
}

init();