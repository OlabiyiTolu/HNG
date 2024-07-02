from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual WeatherAPI.com API key
API_KEY = 'd95126981fce444098a124134240207'

@app.route('/api/hello')
def hello():
    name = request.args.get('visitor_name')
    # if name is None:
    #     name = "Guest"

    # Get client IP address from headers (handle proxy)
    # ip = request.headers.get('X-Forwarded-For', request.remote_addr)  
    ip = '102.89.45.44'

    # Use WeatherAPI.com's IP Lookup API to get location
    base_url = "http://api.weatherapi.com/v1/ip.json"
    params = {
        "key": API_KEY,
        "q": ip 
    }
    response = requests.get(base_url, params=params)


    data = response.json()
    location = data['region']

    # Get current weather data for the location
    weather_url = "http://api.weatherapi.com/v1/current.json"
    weather_params = {
        "key": API_KEY,
        "q": location
    }
    weather_response = requests.get(weather_url, params=weather_params)

    
    weather_data = weather_response.json()
    temperature = weather_data['current']['temp_c']


    response_data = {
        "client ip": ip,
        "greetings": f"Hello, {name}!, the temperature is {int(temperature)} degrees Celcius in {location}",
        "location": location,
        # 'data': weather_data
    }
    return jsonify(response_data)  
    

if __name__ == "__main__":
    app.run(debug=True)