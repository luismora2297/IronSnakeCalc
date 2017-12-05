import flask
import numpy

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/ironAlgebraCalculator", methods=['POST'])
def ironAlgebraCalculator():
    user = flask.request.form['username']



@app.route("/ironLagrange", methods=['POST'])
def ironLagrange():
    lg = []
    fx = []
    table = []
    xenter = "x2"
    z = 0
    for number1, number2 in zip(lg, fx):
        rowprint = str(z) + "   " + str(number1) + "  " + str(number2)
        z += 1
        table.append(rowprint)


    U = fx
    T = lg
    equation = 0
    for j in range(len(lg)):
        equation_t = U[j]
        for k in range(len(lg)):
            if k == j:
                continue
            fac = T[j] - T[k]
            polynomium = numpy.poly1d([1.0, -T[k]])
            equation_t *= polynomium / fac
        equation += equation_t
    iron_snake_lagrange = numpy.polyval(equation, eval(xenter))
    return iron_snake_lagrange


if __name__ == "__main__":
    app.run()
