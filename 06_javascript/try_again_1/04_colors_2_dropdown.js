// Scripts for the second version of 'Colors'

document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#color_menu').onchange = function() {
        document.querySelector('#heading_1').style.color = this.value;
    };

});
