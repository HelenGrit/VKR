import flask
from flask import render_template, request
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

app = flask.Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open('LR_final.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        param1 = float(flask.request.form['matrix_filler'])
        param2 = float(flask.request.form['density'])
        param3 = float(flask.request.form['elastic_modulus'])
        param4 = float(flask.request.form['hardener'])
        param5 = float(flask.request.form['epoxies'])
        param6 = float(flask.request.form['temp'])
        param7 = float(flask.request.form['surface_density'])
        param8 = float(flask.request.form['tensile_modulus'])
        param9 = float(flask.request.form['resin_consumption'])
        param10 = float(flask.request.form['patch_angle'])
        param11 = float(flask.request.form['patch_step'])
        param12 = float(flask.request.form['patch_density'])

        params = [param1, param2, param3, param4, param5, param6, param7, param8, param9, param10, param11, param12]
                                          
        preds = loaded_model.predict([params])
    return render_template('main.html', result = preds)

        
if __name__ == '_main__':
    app.run()