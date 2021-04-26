import numpy as np
from flask import jsonify, request, Flask
from sklearn import preprocessing


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Compredict Task</h1>"


@app.route('/api/v1/standarize', methods=['POST'])
def standarizeScaler():
    sensor1 = request.form.getlist('sensor_1')
    sensor2 = request.form.getlist('sensor_2')
    sensor3 = request.form.getlist('sensor_3')
    if len(sensor1) == len(sensor2) == len(sensor3):
        allSensor = np.array([sensor1, sensor2, sensor3])
        scaler = preprocessing.StandardScaler().fit(allSensor)

        X_scaled = scaler.transform(allSensor)

        temp = {}
        counterName = 1
        for sen in X_scaled:
            temp['sensor_' + str(counterName)] = sen.tolist()
            counterName += 1
        print(temp)
        return jsonify(temp), 200
    else:
        return print("the length of the sensors lists schould be same!!!")


if __name__ == '__main__':
    app.run(debug=True)
