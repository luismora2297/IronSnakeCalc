var ironAllowedNumbers = '0123456789^+-*/%()Ee ';
var ironSqrt = 'sqrt';
var ironPi = 'pi';
var ironSin = 'sin';
var ironCos = 'cos';
var ironTan = 'tan';
var iron = 'pow';

//Ocultar Formularios
//$('#ironNewtonCalculator').attr("hidden", true);
//$('#ironLagrangeCalculator').attr("hidden", true);
//$('#ironAlgebraCalculator').attr("hidden", true);

// Cantidad de elementos de formulario con Display
var ironForms = $('.ironFormCalculator').filter(function() { return $(this).css('display') !== 'none'; } ).length;

//Ocultar Barra al comenzar
$('#ironNavigation').attr("hidden", true);

//Mostrar Barra
$(document).ready(function()
{
    //$('#ironOutputAlg').val('');
    $('#ironInputAlg').val('');

	setTimeout(function()
    {
	    $('body').addClass('ironBody');
	    $('#ironNavigation').attr("hidden", false);
	},5000);

    //Verificar
    console.log(ironForms);

    //Calculadora de Algebra
    $("#ironAlgebraCalculatorForm").validate
    ({
        onkeyup: false,
        submitHandler: function(form)
        {
            $.ajax
            ({
                url: '/ironAlgebraCalculator',
                type: 'POST',
                data: $(form).serialize(),
                success: function(response)
                {
                    $('#ironOutputAlg').val(response);
                },
                error: function(error)
                {
                    $('#ironOutputAlg').val('Error, datos mal ingresados');
                }
            });
            return false;
        }
    });

    //Añadiendo Filas a la tabla de Lagrange
    $("#ironAddRowsLagrange").validate
    ({
        onkeyup: false,
        submitHandler: function(form)
        {
            $.ajax
            ({
                url: '/ironTablelgGen',
                type: 'POST',
                data: $("#ironAddRowsLagrange").serialize(),
                success: function(response)
                {
                    //Añadir a la tabla
                    $('#ironTableLagrange').html(response);
                },
                error: function(error)
                {
                    $('#ironTableLagrange').html('Error de Vyperion al Generar las filas :(');
                }
            });
            return false;
        }
    });

    //Calculadora de Lagrange
    $("#ironLagrangeCalculatorForm").validate
    ({
        onkeyup: false,
        submitHandler: function(form)
        {
            $.ajax
            ({
                url: '/ironLagrangeCalculator',
                type: 'POST',
                data: $(form).serialize(),
                success: function(response)
                {
                    $('#ironLagrangeTableReq').addClass("animated fadeOut").attr("hidden",true);
                    $('#ironLagrangeDiv').html(response);
                },
                error: function(error)
                {
                    $('#ironLagrangeDiv').val('Error, Vyperion no pudo Procesar :(');
                }
            });
            return false;
        }
    });

    //Calculadora de Newton
    $("#ironNewtonCalculatorForm").validate
    ({
        onkeyup: false,
        submitHandler: function(form)
        {
            $.ajax
            ({
                url: '/ironAlgebraCalculator',
                type: 'POST',
                data: $(form).serialize(),
                success: function(response)
                {
                    $('#ironOutputAlg').val(response);
                },
                error: function(error)
                {
                    $('#ironOutputAlg').val('Error, datos númericos mal ingresados.');
                }
            });
            return false;
        }
    });
});


/*===================================================
* ========== Begin Algebra Calculator ===============
=====================================================*/
$('.ironCalculator').click(function()
{
   $('#ironInputAlg').val($('#ironInputAlg').val()+$(this).val());
});

$("#ironCalculatorReset").click(function(e)
{
  e.preventDefault();
  $('#ironInputAlg').val('');
});

$("#ironCalculatorDelete").click(function(e)
{
  e.preventDefault();
  $('#ironInputAlg').val($("#ironInputAlg").val().substring(0, $("#ironInputAlg").val().length - 1));
});

/*===================================================
* ============ End Algebra Calculator ===============
* =================================================*/

$("#menu-toggle").click(function(e)
{
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});

$("#menu-toggle_2").click(function(e)
{
  e.preventDefault();
  $("#wrapper").toggleClass("toggled");
});
