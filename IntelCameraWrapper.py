from time import time

import pyrealsense2 as rs
## UNTESTED IDK IF THIS WORKS

fps = 30		# FPS
class Camera(object):
    
	#
	# Wrapper around intel camera
	#
    def __init__(self):
    	pipe = rs.pipeline()
      
    def startCam(self):
    	pipeline.start()

    def get_frame(self):
    	frames = pipeline.wait_for_frames()
    	colorFrame = frames.get_color_frame()
        return colorFrame
