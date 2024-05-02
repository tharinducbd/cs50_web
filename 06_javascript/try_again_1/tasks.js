// Scripts for to-do app

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#add_task_form').onsubmit = () => {
        const task = document.querySelector('#task').value;
        // console.log(task);

        const li = document.createElement('li');
        li.innerHTML = task;

        document.querySelector('#todolist').append(li);

        // Stop form from submitting
        return false;
    };
});
