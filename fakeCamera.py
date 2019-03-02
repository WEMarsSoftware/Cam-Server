from time import time


defaultSpeed = 120		# Default FPS speed
class Camera(object):
    
	#
	# Emulates a camera
	#
	def __init__(self):
		self.fps = defaultSpeed
		self.frames = [open(f + '.jpg', 'rb').read() for f in [ 'testFrames/f-0', 'testFrames/f-1','testFrames/f-2','testFrames/f-3', 
       															'testFrames/f-4','testFrames/f-5','testFrames/f-6', 'testFrames/f-7',
       															'testFrames/f-8' ]]
	def getFrame(self):
		return self.frames[int(time()*int(self.fps)) % 9]

	def setFPS(self, newFPS):
		self.fps = newFPS