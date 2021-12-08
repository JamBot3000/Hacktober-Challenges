let comeco = new Audio('comeco.wav'),
    fim = new Audio('fim.wav'),
    strange = document.getElementById('color');


$("#devitoButton").click(e => {
    comeco.play();
    $("#sure").attr("style", "display: none");
});

$(document).ready(event => {
    $("#cabeca img").draggable();
    $("#inter").droppable({
        drop: function (e) {
            fim.play();
            strange.classList.add("color");
        }
    });
});