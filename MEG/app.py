from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import json



app = Flask(__name__)

def p(temp, meg_val):
    
    if meg_val == 0:
        return 1.4e-7*temp**6 + 1.85e-5*temp**5 + 3.36e-4*temp**4 + 8.44e-4*temp**3 + 4.63e-2 * temp**2 + 1.28*temp + 1.44e1
    elif meg_val == 5:
        return 4.32e-7*temp**6 + 2.27e-5*temp**5 + 2.97e-4*temp**4 + 1.82e-3*temp**3 + 8.06e-2*temp**2 + 1.55*temp + 1.56e1
    elif meg_val == 10:
        return 2.36e-7*temp**6 + 2.86e-5*temp**5 + 6.26e-4*temp**4 + 3.69e-3*temp**3 + 7.18e-2*temp**2 + 1.84*temp + 1.82e1
    elif meg_val == 15:
        return 4.72e-7*temp**6 + 3.9e-5*temp**5 + 8.36e-4*temp**4 + 6.4e-3*temp**3 + 1.01e-2*temp**2 + 2.24*temp + 2.12e1
    elif meg_val == 20:
        return 8.64e-8*temp**6 + 4.28e-5*temp**5 + 1.45e-3*temp**4 + 1.52e-2*temp**3 + 1.29e-1*temp**2 + 2.57*temp + 2.55e1
    elif meg_val == 25:
        return 7.42e-8*temp**6 + 5.39e-5*temp**5 + 2.13e-3*temp**4 + 2.84e-2*temp**3 + 2.36e-1*temp**2 + 3.26e0*temp + 3.09e1
    elif meg_val == 30:
        return 2.63e-7*temp**6 + 7.51e-5*temp**5 + 3.19e-3*temp**4 + 5.19e-2*temp**3 + 4.73e-1*temp**2 + 4.7e0*temp + 3.89e1
    elif meg_val == 35:
        return 5.5e-7*temp**6 + 1.18e-4*temp**5 + 5.27e-3*temp**4 + 9.86e-2*temp**3 + 9.99e-1*temp**2 + 8.01e0*temp + 5.3e1
    elif meg_val == 40:
        return 6.62e-7*temp**6 + 1.6e-4*temp**5 + 8.5e-3*temp**4 + 1.94e-1*temp**3 + 2.3e0*temp**2 + 1.68e1*temp + 8.41e1
    elif meg_val == 45:
        return 3.08e-6*temp**6 + 4.28e-4*temp**5 + 2.08e-2*temp**4 + 4.86e-1*temp**3 + 6.13e0*temp**2 + 4.38e1*temp + 1.73e2
    elif meg_val == 50:
        return 2.51e-5*temp**6 + 2.51e-3*temp**5 + 1.03e-1*temp**4 + 2.23e0*temp**3 + 2.72e1*temp**2 + 1.83e2*temp + 5.80e2



#Loads home page
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predictMEG', methods=["POST"])
def csvInfo():
	try:
		pressure = request.form['pressure'];
		temp = request.form['temp'];

		print(pressure)
		print(temp)
		def predidct_meg( tAct,pAct):
		    for i in range(0,11):
		        nearestMeg = i*5
		        pPredict = p(tAct, nearestMeg)
		        if(pPredict > pAct):
		            return nearestMeg

		try:
			meg = predidct_meg(float(temp), float(pressure))

		except:
			meg = "invalid!"

		print(meg)
		response=app.response_class(
			response= json.dumps(
			{"meg":meg
			}),
			status=200,
			mimetype='application/json'
			)
	except Exception as e:
		response = app.response_class(
		response=json.dumps({"message":str(e)}),
		status = 400,
		mimetype='application/json'
		)
	return response


if __name__ == '__main__':
#	app.run(host='0.0.0.0',debug=True)
#	app.run(host='0.0.0.0', port='5000',debug=True, threaded=True)
	app.run(host='localhost', port='5000',debug=False, threaded=False)

