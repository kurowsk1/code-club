def picapture (input):
  if input == True:
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    sleep(3)
    camera.capture(photo_path)
    camera.stop_preview()
  else:
    pass

while True:
  x = 0 # capture button current state
  picapture(x)