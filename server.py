###
#	Video Server
#
#
###

#!/usr/bin/env python
from flask import Flask, render_template, Response, request
from fakeCamera import Camera
import json


app = Flask(__name__)

##
#	Default index, renders the test pages
#
@app.route('/')
def index():
    return render_template('index.html')

##
#	Generates a camera frame from whatever camera is default
#
def gen(camera):
    while True:
        frame = camera.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


##
#	frame endpoint that serves the motionJpeg output from the camera
# 	- access as IP/motionJpeg
#
@app.route('/motionJpeg')
def motionJpeg():
    return Response(gen(cam),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


##
#	Endpoint to update the FPS of the video server
# 
@app.route('/fps', methods=['POST'])
def setFPS():
    if(not request.json):
        abort(400)
        print("Bad Response")


    print(request.json["fps"])
    cam.setFPS(request.json["fps"])
    return json.dumps(request.json)


##
#	Run app 
#
if (__name__ == '__main__'):		
	cam = Camera()							# Generate the new camera
	app.run(host='0.0.0.0', debug=True)		# Start the server