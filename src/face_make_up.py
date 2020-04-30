import cv2
import numpy as np
import easygui as e
import random
from datetime import datetime

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
INFO = 'Press Key \'1\'- Face Makeup ON/OFF \'q\'- Exit'
METADATA = datetime.now().strftime("%Y%m%d_%h_%m")
FILE_NAME = 'FMK_'+METADATA+'.avi'

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(FILE_NAME, fourcc, 20.0, (640,480))

FACE_DEC_ACT = True
EYE_DEC_ACT = False

def ran_rgb():
    rgb = random.randint(0, 25)*10, random.randint(0, 25)*10, random.randint(0, 25)*10
    return rgb

if cap.isOpened():
    cam_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    cam_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    while cap.isOpened():
        ret, frame = cap.read()
        print(frame.shape)
        if ret:
            datet = str(datetime.now())
            frame = cv2.putText(frame, datet, (0, int(cam_h) - 3), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
            frame = cv2.putText(frame, INFO, (0, 20), font, 0.6, ran_rgb(), 1, cv2.LINE_AA)

            faces = face_cascade.detectMultiScale(frame, 1.1, 4)

            if FACE_DEC_ACT:
                for (x, y, w, h) in faces:
                    roi_color = frame[y:y + h, x:x + w]

                    # fitting hat
                    hat_img = cv2.imread('../img/hat.png')
                    hat_width = int(w * 1.55)
                    hat_height = int(h * 0.6)
                    diff_width = int(abs((x - hat_width) / 2))
                    diff_height = int(abs((y - hat_height) / 2))
                    hat_x = x - diff_width
                    hat_y = y + diff_height

                    hat_img = cv2.resize(hat_img, (hat_width, hat_height), interpolation=cv2.INTER_AREA)
                    hat_gray = cv2.cvtColor(hat_img, cv2.COLOR_BGR2GRAY)
                    thresh, hat_mask = cv2.threshold(hat_gray, 230, 255, cv2.THRESH_BINARY)
                    hat_img[hat_mask == 255] = 0
                    hat_area = frame[hat_y-hat_height:hat_y, hat_x:hat_x + hat_width]
                    try:
                        masked_hat_area = cv2.bitwise_and(hat_area, hat_area, mask=hat_mask)
                        final_hat = cv2.add(masked_hat_area, hat_img)
                        frame[hat_y-hat_height:hat_y, hat_x:hat_x + hat_width] = final_hat
                    except:
                        print("RANGE OUT")

            out.write(frame)
            cv2.imshow('frame', frame)

            # give user to select options
            USER_INPUT = cv2.waitKey(1)
            if USER_INPUT == ord('q'):
                break
            elif USER_INPUT == ord('1'):
                if FACE_DEC_ACT:
                    FACE_DEC_ACT = False
                else:
                    FACE_DEC_ACT = True
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
else:
    e.msgbox("The Web-cam does not work :(")