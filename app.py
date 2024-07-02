from flask import Flask, request, jsonify
import requests
import geocoder


app = Flask(__name__)

API_KEY = '27b597283caa2674af2979ade8fe7156'  # Replace with your actual API key

@app.route('/api/hello')
def hello():
    name = request.args.get('visitor_name')
    # if name is None:
    #     name = "Guest"
    # name = Tolu

    # Get client IP from headers
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)  # Check for X-Forwarded-For header

    geolocation = geocoder.ip(ip)
    location = geolocation.city


    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    temperature = (temperature - 273.15)
    
    response = {
        'client ip': ip,
        'location': location,
        'greetings' : f"Hello, {name}!, the temperature is {int(temperature)} degrees Celcius in {location}" 
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug = True) 