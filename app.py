from flask import Flask, render_template,request, send_from_directory
import os
import ipinfo

app = Flask(__name__)

"""
Loads API key from Heroku configuration variables (confirgured on Heroku dashboard)
"""

#IPINFO_API_KEY = os.getenv('IPINFO_API_KEY')
IPINFO_API_KEY = '10ad7587605c57'

"""
The code below loads the little icon that shows up at the top of the browser next to the website Title.
"""
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Recieves Summoner Username as a query and builds API URL and then sends back information recieved from Riot Games
@app.route('/')
def index():
    """Return homepage."""
    
    handler = ipinfo.getHandler(IPINFO_API_KEY)
    details = handler.getDetails().all
    ip = details['ip']
    city = details['city']
    region = details['region']
    country = details['country_name']
    postal = details['postal']
    timezone = details['timezone']
    latitude = details['latitude']
    longitude = details['longitude']

    # Render the 'index.html' template, passing all parsed parameters
    return render_template("index.html", ip=ip, city=city, region=region, country=country, postal=postal, timezone=timezone, latitude=latitude, longitude=longitude)