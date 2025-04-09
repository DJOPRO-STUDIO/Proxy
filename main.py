from flask import *
import json
import requests
import os

app = Flask(__name__)

@app.route("/roblox_image_extract/<id>")
def home(id):
  a = json.loads(requests.get(f"https://thumbnails.roblox.com/v1/assets?assetIds={id}&size=420x420&format=Png&isCircular=false").content)
  if a and a.data[0].state == "Completed":
    return a.data[0].imageUrl
  return ""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
