let counter = 0;

if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h3').innerHTML = counter;
    localStorage.setItem('counter', counter)
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});
