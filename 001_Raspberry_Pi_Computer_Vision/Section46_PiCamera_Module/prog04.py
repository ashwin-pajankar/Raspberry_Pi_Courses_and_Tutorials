import picamera

camera = picamera.PiCamera()
camera.resolution = (320, 240)
camera.start_recording('my_video.h264')
camera.wait_recording(5) # record for 2 seconds
camera.stop_recording()
