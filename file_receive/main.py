import os
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "super secret key"

@app.get("/")
def page():
    return send_file("index.html")

@app.post('/upload')
def upload():
    files = request.files.getlist("files")
    print(files)
    for file in files:
        if file.filename == "":
            flash("No selected file")
            continue
        filename = secure_filename(file.filename)
        file.save(os.path.join("received", filename))
    return f"Đã tải {len(files)} tệp lên thành công!"

app.run("0.0.0.0", port=80)
