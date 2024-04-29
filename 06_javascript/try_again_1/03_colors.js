document.addEventListener('DOMContentLoaded', () => {

    // Method 1: Not so effective due to repetition...
    document.querySelector('#red').onclick = function () {
        document.querySelector('#heading_1').style.color = 'red';
    };
    document.querySelector('#green').onclick = function () {
        document.querySelector('#heading_1').style.color = 'green';
    };
    document.querySelector('#blue').onclick = () => {
        document.querySelector('#heading_1').style.color = 'blue';
    };

    // Method 2: 'data' attribute
    document.querySelectorAll('.btns_gr_2').forEach(function(button) {
        button.onclick = function() {
            document.querySelector('#heading_2').style.color = button.dataset.color;
        }
    });

    // Method 2 A: shorthand notation for the function call
    // document.querySelectorAll('.btns_gr_2').forEach((button) => {
    //     button.onclick = function() {
    //         document.querySelector('#heading_2').style.color = button.dataset.color;
    //     }
    // });
});
