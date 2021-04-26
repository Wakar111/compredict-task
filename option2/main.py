from flask import jsonify, request, Flask
from sklearn import preprocessing
from helperFuncs import inputValueSensor
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Compredict Task</h1><p>continue <a href='/api/v1/standarize'><button>here</button></a> and enter a number in the terminal</p>"


@app.route('/api/v1/standarize', methods=['GET', 'POST'])
def api_all():
    inputCalls = input('how many numbers entry do you want to have? ')
    if request.method == 'GET':
        sensor1 = inputValueSensor(int(inputCalls))
        sensor2 = inputValueSensor(int(inputCalls))
        sensor3 = inputValueSensor(int(inputCalls))
        if len(sensor1) == len(sensor2) == len(sensor3):
            allSensor = np.array([sensor1, sensor2, sensor3])
            scaler = preprocessing.StandardScaler().fit(allSensor)

            X_scaled = scaler.transform(allSensor)

            temp = {}
            counterName = 1
            for sen in X_scaled:
                temp['sensor_' + str(counterName)] = sen.tolist()
                counterName += 1
            return jsonify({'result': temp})
        else:
            return print("the length of the sensors schould be same!!!")


if __name__ == '__main__':
    app.run(debug=True)
