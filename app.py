from flask import Flask,render_template,request
import pickle
import numpy as np



model = pickle.load(open('xgbre.pkl','rb'))

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['GET','POST'])
def predict():
    T=request.form['T']
    TM=request.form['TM']
    Tm=request.form['Tm']
    SLP=request.form['SLP']
    H=request.form['H']
    VV=request.form['VV']
    V=request.form['V']
    VM=request.form['VM']

    predictions = model.predict(np.array([[T,TM,Tm,SLP,H,VV,V,VM]]))
    print(predictions[0])
    a = int(predictions[0])
    return render_template('result.html',lower=a-47,upper=a+47)
    


if __name__ == '__main__':
    app.run(debug=True)