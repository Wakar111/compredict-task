import requests

payload = {
    "sensor_1": [5.44, 3.22, 6.55, 8.54, 1.24],
    "sensor_2": [5444.44, 33.22, 622.55, 812.54, 1233.24],
    "sensor_3": [0.44, 0.22, 0.55, 0.54, 0.24]
}
r = requests.post('http://127.0.0.1:5000/api/v1/standarize', data=payload)
print(r.status_code)