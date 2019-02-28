from time import time


speed = 30		# FPS
class Camera(object):
    
	#
	# Emulates a camera
	#
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['testFrames/f-0', 'testFrames/f-1','testFrames/f-2',
        														'testFrames/f-3', 'testFrames/f-4','testFrames/f-5',
        														'testFrames/f-6', 'testFrames/f-7','testFrames/f-8']]

    def get_frame(self):
        return self.frames[int(time()*speed) % 9]
