import json
from pathlib import Path
from typing import *
import cv2
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from .info import PRE_PATH, PROJECT_NAME, STATIC_DIR, VIEWS_DIR, UPLOAD_DIR

site = Blueprint("site", PROJECT_NAME, template_folder=VIEWS_DIR)

camera = cv2.

def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 
            
@app.route('/video_feed')
def video_feed():
    return <img src = Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')>

            
@site.route("/<lost>/")
def lostpage(lost):
    return """
<script>
alert("Are you sure this page really exists? We can't seem to find it.")
</script><h1>
<a href="/">Visit our app!</a></h1>
"""
