const form = document.querySelector(".form__todo");
const input = form.querySelector("input");
const TodoList = document.querySelector(".TodoProblem");
const FinishList = document.querySelector(".FinishProblem");

const TODO_LS = "pending";
const FINISH_LS = "finish";

let todoList = [];
let finishList = [];




function removeTodo(taskID) {
    todoList = todoList.filter(function (task) {
        return task.id != taskID;
    })
}
function removeFin(taskID) {
    finishList = finishList.filter(function (task) {
        return taskID != task.id;
    })
}
function saveTodoList() {
    localStorage.setItem(TODO_LS, JSON.stringify(todoList));
}
function saveFinishList() {
    localStorage.setItem(FINISH_LS, JSON.stringify(finishList));
}
function addFin(task) {
    finishList.push(task);
}
function addTodo(task) {
    todoList.push(task);
}

function findFin(taskID) {
    // console.log(taskID);
    // console.log(finishList);
    return findList = finishList.find(function (task) {
        return taskID === task.id;
    });
}
function findTodo(taskID) {
    // console.log(taskID);
    // console.log(todoList);
    return findList = todoList.find(function (task) {
        return taskID === task.id;
    });
}

function delteTask(event) {

    const li = event.target.parentNode.parentNode;
    li.parentNode.removeChild(li);
    removeFin(li.id);
    removeTodo(li.id);
    saveTodoList();
    saveFinishList();
}
// todolist로 보내는 함수
function TodoTask(event) {
    console.log(event.target);
    const li = event.target.parentNode.parentNode;
    // console.log(li);

    li.parentNode.removeChild(li);
    const handing = findFin(li.id);
    // console.log("todo:", handing);
    removeFin(li.id);
    addTodo(handing);
    getTodoList(handing);
    saveTodoList();
    saveFinishList();
}
// finish list로 보내는 함수
function FinishTask(event) {
    // console.log(todoList);
    // console.log(event.target);
    const li = event.target.parentNode.parentNode;
    // console.log(li);
    // console.log(li.parentNode);
    li.parentNode.removeChild(li);
    const handing = findTodo(li.id);
    console.log(li);
    // console.log(li.id);
    removeTodo(li.id);
    addFin(handing);
    getFinList(handing);
    saveTodoList();
    saveFinishList();

}


function basicForm(toDO) {
    // console.log(toDO);
    const li = document.createElement("li");
    const li_span = document.createElement("span");
    const deleBtn = document.createElement("button");
    deleBtn.innerHTML = `<span>❌</span>`;
    // console.log(deleBtn);
    deleBtn.addEventListener("click", delteTask);
    // console.log(deleBtn);
    li_span.innerText = toDO.text;
    li.appendChild(li_span);
    li.appendChild(deleBtn);
    li.id = toDO.id;
    return li;
}
function getFinList(input_text) {
    // console.log(input_text);
    const basicli = basicForm(input_text);
    const backBtn = document.createElement("button");
    backBtn.innerHTML = `<span>⏪</span>`;
    backBtn.addEventListener("click", TodoTask);
    console.log(backBtn);
    basicli.appendChild(backBtn);
    FinishList.appendChild(basicli);
}

function getTodoList(input_text) {
    // console.log(input_text);
    const basicli = basicForm(input_text);
    const finBtn = document.createElement("button");
    finBtn.innerHTML = `<i class="fas fa-check"></i>`;
    // finBtn.innerHTML = "X";
    finBtn.addEventListener("click", FinishTask);
    basicli.appendChild(finBtn);
    TodoList.appendChild(basicli);
}
function UpdateTodoList(task) {
    todoList.push(task);
}
function getObject(text) {
    return {
        id: String(Date.now()),
        text
    };
}
function Update(event) {
    event.preventDefault();
    const input__text = getObject(input.value);
    // console.input__text;
    getTodoList(input__text);
    UpdateTodoList(input__text);
    input.value = "";
    saveFinishList();
    saveTodoList();

}

function loadTodo() {
    todoList = JSON.parse(localStorage.getItem(TODO_LS)) || [];
    finishList = JSON.parse(localStorage.getItem(FINISH_LS)) || [];
    todoList.forEach(function (pend) {
        getTodoList(pend);
    });
    finishList.forEach(function (fin) {
        getFinList(fin);
    });

}


function init() {
    form.addEventListener("submit", Update);
    loadTodo();
}

init();