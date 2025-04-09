from flask import *
import json
import requests
import os

app = Flask(__name__)

@app.route("/roblox_image_extract/<id>")
def home(id):
    # Get the image data from Roblox API
    response = requests.get(f"https://thumbnails.roblox.com/v1/assets?assetIds={id}&size=420x420&format=Png&isCircular=false")
    a = response.json()  # Use .json() to directly parse the JSON response
    
    # Check if the data is available and its state is "Completed"
    if a and a['data'][0]['state'] == "Completed":
        return a['data'][0]['imageUrl']
    
    return ""  # Return empty string if the condition is not met

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)  # Run the app on all interfaces
