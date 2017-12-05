$(document).ready(function()
{
    $('#ironNavigation').attr("hidden", true);
	setTimeout(function()
    {
	    $('body').addClass('ironBody');
	    $('#ironNavigation').attr("hidden", false);
	},5000);

});

$('.ironCalculator').click (function()
{
   $('#ironShow').val($('#ironShow').val()+$(this).val());
});

$("#menu-toggle").click(function(e)
{
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});

$("#ironCalculatorReset").click(function(e)
{
  e.preventDefault();
  $('#ironShow').val('');
});

$("#ironCalculatorDelete").click(function(e)
{
  e.preventDefault();
  $('#ironShow').val($("#ironShow").val().substring(0, $("#ironShow").val().length - 1));
});
