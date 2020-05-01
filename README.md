
# Virtual Accessory Fitting Program
<p>2020 Spring CPS497 Independent Study<br>
Joonwoo Park<br>
Central Michigan University</p>


## Introduction
Fitting virtual accessory by face detection and computer vision for independent study project

## How it works

This project use __OpenCV__'s prebuilt _Cascade Classifier for frontal face detection_.
```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
```

_detectMultiScale_ method detect present frame's face location.<br>
variable x, y store face coordinates<br>
variable w, h store face width and height
```python
faces = face_cascade.detectMultiScale(frame, 1.1, 4)
for (x, y, w, h) in faces:
roi_color = frame[y:y + h, x:x + w]
```
ㅓㅗㅜㅡㅏ


## Feature
  - ***face detection on & off***<br>
  The program wait user's key input.
  Face detecting can be on and off when user push '1'.<br>
  
![detecting_onoff](docs/detecting_onoff.png)
&nbsp;




  - ***Exception handling for image out of frame range***<br>
  When the accessory locate on the out of frame, program does not show the accessory for fitting.
  This exception handling over top, bottom, left and right side of frame.
  <br>
  
![range_over](docs/range_over.png)
&nbsp;


  - ***Auto recording and export as video***<br>
  User can record the video as default.<br>
  When the program begin, it automatically record the video.<br>
  Then, user can check the output as .avi file at src folder.<br>
  
![record_msg](docs/record_msg.PNG)
![saved_file](docs/saved_file.PNG)
&nbsp;

## Reference





