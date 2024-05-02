// Scripts for to-do app

document.addEventListener('DOMContentLoaded', () => {

    // By default, submit button is disabled (until we type something on New Task field).
    document.querySelector('#submit_task').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if (document.querySelector('#task').value.length > 0) {
            document.querySelector('#submit_task').disabled = false;
        } else {
            document.querySelector('#submit_task').disabled = true;
        }
    };

    document.querySelector('#add_task_form').onsubmit = () => {
        const task = document.querySelector('#task').value;
        // console.log(task);

        const li = document.createElement('li');
        li.innerHTML = task;

        document.querySelector('#todolist').append(li);

        document.querySelector('#task').value = '';
        document.querySelector('#submit_task').disabled = true;

        // Stop form from submitting
        return false;
    };
});
