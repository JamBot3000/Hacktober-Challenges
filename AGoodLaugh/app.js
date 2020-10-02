let comeco = new Audio('comeco.wav'), 
    fim = new Audio('fim.wav');

$("#devitoButton").click(e => {
    comeco.play();
    $("#sure").attr("style", "display: none");
});

$(document).ready(event =>
{
    $("#cabeca img").draggable();
    $("#inter").droppable({
        drop: function(e) {
            fim.play();
        }
    });
});