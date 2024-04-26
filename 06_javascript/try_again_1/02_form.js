// Scripts for form.js

document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#f_1').onsubmit = function () {
        let msg = document.querySelector('h5');
        const name = document.querySelector('#name').value;

        msg.innerHTML = `Welcome, ${name}!`;
    };

});
