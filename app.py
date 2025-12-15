from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

ISS_API = "http://api.open-notify.org/iss-now.json"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iss")
def iss_position():
    data = requests.get(ISS_API).json()
    lat = float(data["iss_position"]["latitude"])
    lon = float(data["iss_position"]["longitude"])
    return jsonify({
        "lat": lat,
        "lon": lon
    })

if __name__ == "__main__":
    print("🚀 ISS Tracker Running...")
    app.run(debug=True)
