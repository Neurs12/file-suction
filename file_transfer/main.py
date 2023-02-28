from flask import Flask, send_file
import os

app = Flask(__name__)

@app.get("/<file>")
def lol(file):
    return send_file(file)

app.run("0.0.0.0", port=80)
