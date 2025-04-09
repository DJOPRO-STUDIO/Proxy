from flask import *
import json
import requests

app = Flask(__name__)

@app.route("/roblox_image_extract/<id>")
def home(id):
  a = json.loads(requests.get(f"https://thumbnails.roblox.com/v1/assets?assetIds={id}&size=420x420&format=Png&isCircular=false").content)
  if a and a.data[0].state == "Completed":
    return a.data[0].imageUrl
  return ""
