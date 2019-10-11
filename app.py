from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Calculator')

@app.route('/divide', methods=['GET', 'POST'])
def divide():
    if request.method =='POST':
        form=request.form
        loan = float(form['numOne'])
        numPay = float(form['numTwo'])
        rate = float(form['numThree'])
        n=numPay*12
        i=rate/12
        a= 1+ i
        b=a**n
        c = b-1
        d = c/(i *b)
        calc = loan/d
        result = "Monthly payment is: ${0:6.2f}".format (calc)
        return render_template('index.html', display=result, pageTitle='My Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
