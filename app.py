import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
   
    cash = int(request.form['cash'])
    toll = int(request.form['toll'])
    gas = int(request.form['gas'])
    operator = int(request.form['operator'])
    gpay = int(request.form['gpay'])
    r1 = cash - toll - gas
    r2 = (operator/2) - r1
    if r2>0:
     result = abs(r2)-(gas/2)-gpay      
    else:
     result = abs(r2)+(gas/2)-gpay

    return render_template('index.html', prediction_text="Take {}rs from driver".format(result))


if __name__ == "__main__":
    app.run(debug=True)
