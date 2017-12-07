import flask
import numpy
import sympy

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/ironAlgebraCalculator", methods=['POST'])
def ironAlgebraCalculator():
    iron_input = flask.request.form['ironInputAlg']
    iron_algebra_answer = sympy.N(iron_input)
    return str(iron_algebra_answer)


@app.route("/ironTablelgGen", methods=['POST'])
def ironTablelgGen():
    iron_table_rows_number_01 = int(flask.request.form['ironAddLgRow'])
    if iron_table_rows_number_01 <= 1:
        iron_message = "¡Error! ¡No es válido el valor insertado para generar filas!"
        return flask.render_template('iron_errors.html', iron_add_message=iron_message)
    else:
     return flask.render_template('iron_table_rows.html', ironaddrows=iron_table_rows_number_01)


@app.route("/ironLagrangeCalculator", methods=['POST'])
def ironLagrange():
    lg = flask.request.form.getlist('iron_lg_x[]')
    fx = flask.request.form.getlist('iron_lg_fx[]')
    iron_table_number = []
    iron_number_1 = []
    iron_number_2 = []
    xenter = flask.request.form['iron_xenter']
    #Verificar valor de Xenter
    y=0
    x=0
    for z in range(len(lg)):
        x = z

    if float(xenter) < float(lg[y]) or float(xenter) > float(lg[x]):
       iron_message="¡Error! ¡El valor de interpolación no esta en el rango!"
       return flask.render_template('iron_errors.html', iron_add_message=iron_message)
    else:
        z = 0
        # Añadiendo una tabla de Lagrange Para imprimir
        for number1, number2 in zip(lg, fx):
            ironrowprint = z
            iron_graph_1 = number1
            iron_graph_2 = number2
            z += 1
            iron_table_number.append(ironrowprint)
            iron_number_1.append(iron_graph_1)
            iron_number_2.append(iron_graph_2)
        # Para añadir el resultado
        U = fx
        T = lg
        equation = 0
        for j in range(len(lg)):
            equation_t = float(U[j])
            for k in range(len(lg)):
                if k == j:
                    continue
                res_1 = float(T[j])
                res_2 = float(T[k])
                fac = res_1 - res_2
                polynomium = numpy.poly1d([1.0, -res_2])
                equation_t *= polynomium / fac
            equation += equation_t
        iron_snake_lagrange = numpy.polyval(equation, eval(xenter))
        return flask.render_template('iron_lagrange.html',
                                     iron_lg_table=zip(iron_table_number,iron_number_1,iron_number_2),
                                     iron_graph=zip(iron_number_1, iron_number_2),
                                     iron_lg_result=iron_snake_lagrange,
                                     iron_lg_equation=equation,
                                     iron_lg_entered=xenter)


if __name__ == "__main__":
    app.run()
