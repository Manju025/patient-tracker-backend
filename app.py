from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route('/')
def index():
    return jsonify({"message": "Backend is running 🔥"})

@app.route('/api/hospitals')
def get_hospitals():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if not lat or not lon:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    query = f"""
    [out:json];
    node["amenity"="hospital"](around:5000,{lat},{lon});
    out body;
    """
    overpass_url = "https://overpass-api.de/api/interpreter"
    response = requests.get(overpass_url, params={"data": query})
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
