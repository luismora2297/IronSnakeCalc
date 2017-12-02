$(document).ready(function()
{
    $('#mainNavigation').attr("hidden", true);
	setTimeout(function()
    {
	    $('body').addClass('log-body');
	    $('#mainNavigation').attr("hidden", false);
	},5000);

});

function IronSnakeCalcBtn(button)
{
    var x = button.value;
	document.getElementById("demo").innerHTML += x;
}

$("#menu-toggle").click(function(e)
{
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});