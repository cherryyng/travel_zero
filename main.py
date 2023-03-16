from flask import Flask, request, render_template, url_for
import requests

app = Flask(__name__)  # Create an Instance


@app.route('/')  # Route the Function
def landing():
  return render_template('landing.html')

@app.route('/main') 
def main():
  return render_template('main.html')

app.run(host='0.0.0.0', port=5000,
        debug=True)  # Run the Application (in debug mode)
')
api_key = "0GDMS8995VMZ4MP3XMPVMKAJ86ND"
ESTIMATE_ENDPOINT = "https://beta3.api.climatiq.io/estimate"

@app.route('/carbon_footprint', methods=['GET', 'POST'])
def carbon_footprint():
  if request.method == 'POST':
    # Handle POST request
    # Get data from request form
    # origin = request.form['origin']
    # destination = request.form['destination']
    # distance = CALCULATION METHOD
    # transport_mode = request.form['transport_mode']
    # distance_unit = 'km'

    # Set up API request
    url = "https://beta3.api.climatiq.io/estimate"
    api_key = "0GDMS8995VMZ4MP3XMPVMKAJ86ND"
    activity_id = "passenger_vehicle-vehicle_type_automobile-fuel_source_na-distance_na-engine_size_na"
    region = "GLOBAL"

    # Set up request body
    json_body = {
        "emission_factor": {
            "activity_id": activity_id,
            "source": "GHG Protocol",
            "region": region,
            "year": "2017",
            "lca_activity": "unknown"
        },
        "parameters": {
            "distance": 167,
            "distance_unit": "km"
        }
    }

    # Send request to API
    headers = {"Authorization": f"Bearer: {api_key}"}
    response = requests.post(url, json=json_body, headers=headers)

    # Parse response and extract carbon footprint
    data = response.json()
    carbon_footprint = data["carbon"]["value"]

    # Render template with carbon footprint data
    return render_template('carbon_footprint.html', carbon_footprint=carbon_footprint)
  # else:
  #   return render_template('carbon_footprint.html')

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', debug=True, port=8080)

#DISTANCE CALCULATIONS
endpoint = 'https://api.openrouteservice.org/v2/matrix/driving-car'
api_key = '5b3ce3597851110001cf6248ea51806fe39949ccb5b9b5d9638da93b'


def calculateDistance():

  origin = request.form['pointA']
  destination = request.form['pointB']

  def geocode(address):
    url = f'https://nominatim.openstreetmap.org/search/{address}?format=json'
    response = requests.get(url).json()
    if response:
      return response[0]['lon'], response[0]['lat']
    else:
      return None

  originCoordinates = geocode(origin)
  destinationCoordinates = geocode(destination)

  body = {
    'locations': f'{originCoordinates[0]},{originCoordinates[1]}{destinationCoordinates[0]},{destinationCoordinates[1]}',
    'metrics': '[distance]',
    'api_key': api_key,
    'units':'km'
  }
  
  headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization':
    '5b3ce3597851110001cf6248ea51806fe39949ccb5b9b5d9638da93b',
    'Content-Type': 'application/json; charset=utf-8'
  }
  
  call = requests.post('https://api.openrouteservice.org/v2/matrix/drivingcar', json=body, headers=headers)
  
  data = call.json()
  matrix = data['distance']


  
  return render_template('main.html', matrix = matrix)



  #carbon footprint calculations
  ')
api_key = "0GDMS8995VMZ4MP3XMPVMKAJ86ND"
ESTIMATE_ENDPOINT = "https://beta3.api.climatiq.io/estimate"

@app.route('/carbon_footprint', methods=['GET', 'POST'])
def carbon_footprint():
  if request.method == 'POST':
    # Handle POST request
    # Get data from request form
    # origin = request.form['origin']
    # destination = request.form['destination']
    # distance = CALCULATION METHOD
    # transport_mode = request.form['transport_mode']
    # distance_unit = 'km'

    # Set up API request
    url = "https://beta3.api.climatiq.io/estimate"
    api_key = "0GDMS8995VMZ4MP3XMPVMKAJ86ND"
    activity_id = "passenger_vehicle-vehicle_type_automobile-fuel_source_na-distance_na-engine_size_na"
    region = "GLOBAL"

    # Set up request body
    json_body = {
        "emission_factor": {
            "activity_id": activity_id,
            "source": "GHG Protocol",
            "region": region,
            "year": "2017",
            "lca_activity": "unknown"
        },
        "parameters": {
            "distance": 167,
            "distance_unit": "km"
        }
    }

    # Send request to API
    headers = {"Authorization": f"Bearer: {api_key}"}
    response = requests.post(url, json=json_body, headers=headers)

    # Parse response and extract carbon footprint
    data = response.json()
    carbon_footprint = data["carbon"]["value"]

    # Render template with carbon footprint data
    return render_template('carbon_footprint.html', carbon_footprint=carbon_footprint)
  # else:
  #   return render_template('carbon_footprint.html')
