// Scripts for form.js

document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#f_1').onsubmit = function () {
        const name = document.querySelector('#name').value;

        document.querySelector('h5').innerHTML = `Welcome, ${name}!`;
        return false;
    };

});
