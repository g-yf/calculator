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
        year = float(form['numThree'])
        rate = float(form['numFour'])
        period = float(form['numFive'])
        n=numPay*year
        i=rate/period
        a= 1+ i
        b=a**n
        c = b-1
        d = c/(i *b)
        calc = loan/d
        return render_template('index.html', display=calc, pageTitle='My Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
