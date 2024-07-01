from flask import Flask, request, jsonify
import requests
import geocoder
# from mykey import key

app = Flask(__name__)

API_KEY = '27b597283caa2674af2979ade8fe7156'

@app.route('/')
def hello():
    name = request.args.get('your name')
    if name is None:
        name = "Guest"
    # name = 'Tolu'
    ip = request.remote_addr

    geolocation = geocoder.ip(ip)
    location = geolocation.city
    # location = 'Lagos'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    temperature = (temperature - 273.15)

    response = {
        # 'name': name,
        'client ip': ip,
        'location': location,
        'greetings' : f"Hello, {name}!, the temperature is {int(temperature)} degrees Celcius in {location}" 
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug = True)