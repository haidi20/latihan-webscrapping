import requests
from flask import jsonify
from bs4 import BeautifulSoup

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')

@app.route('/')
    def index():
        return jsonify(soup)

