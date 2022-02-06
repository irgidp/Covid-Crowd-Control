import cv2
from cv2 import FONT_HERSHEY_SCRIPT_SIMPLEX
import matplotlib.pyplot as plt
import pymsgbox

config_file = 'assets/file/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'assets/file/frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
file_name = 'assets/file/Labels.txt'
with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
    # classLabels.append(fpt.read())


model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# img = cv2.imread('test1.jpg')
# plt.imshow(img)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# ClassIndex, confidece, bbox = model.detect(img, confThreshold=0.5)

# font_scale = 3
# font = cv2.FONT_HERSHEY_PLAIN
# for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
#     cv2.rectangle(img, boxes, (255, 0, 0), 2)
#     cv2.putText(img, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+40),
#                 font, fontScale=font_scale, color=(0, 255, 0), thickness=3)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot Open Video")

font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

while True:
    ret, frame = cap.read()

    ClassIndex, confidece, bbox = model.detect(frame, confThreshold=0.5)

    print(ClassIndex)
    if(len(ClassIndex) != 0):
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):
            if(ClassInd <= 1):
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                cv2.putText(frame, classLabels[ClassInd-1], (boxes[0]+10, boxes[1]+40),
                            font, fontScale=font_scale, color=(0, 255, 0), thickness=3)

    i = 0
    for z in ClassIndex:
        if(z == 1):
            i += 1
        if(i >= 2):
            pymsgbox.alert('Lebih Dari 2', timeout=1000)

    cv2.imshow('Object Detection Tutorial', frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
