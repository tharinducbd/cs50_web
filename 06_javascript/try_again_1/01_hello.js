// hello() to switch between hello and goodbye
// counter() to count from zero

function hello() {
    const heading = document.querySelector('h3');
    const change_button = document.querySelector('#change');
    if (heading.innerHTML === 'Hello!') {
        heading.innerHTML = 'Goodbye!';
        change_button.innerHTML = 'Back to hi';
    }
    else {
        heading.innerHTML = 'Hello!';
        change_button.innerHTML = 'All done.';
    }
}


if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0)
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h4').innerHTML = counter;
    localStorage.setItem('counter', counter);
}


document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('h4').innerHTML = localStorage.getItem('counter');

    document.querySelector('#change').onclick = hello;
    document.querySelector('#count').onclick = count;

    setInterval(hello, 3000);
    setInterval(count, 2000);

});
