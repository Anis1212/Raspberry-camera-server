from flask import Flask, render_template, Response
import datetime
import time
import pika 
from camera import Camera
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html') 

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video():
     return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
