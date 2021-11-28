import picamera

camera = picamera.PiCamera()
camera.start_recording('1.h264')
camera.wait_recording(2)
for i in range(2, 11):
	camera.split_recording('%d.h264' % i)
	camera.wait_recording(2)
camera.stop_recording()
