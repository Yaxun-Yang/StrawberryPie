import this
from time import sleep

import cv2
index = 1

# def faces_exist(flags):
#     return flags


def save_video(video, num):
    sz = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    fps = 20
    # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    # fourcc = cv2.VideoWriter_fourcc('m', 'p', 'e', 'g')
    fourcc = cv2.VideoWriter_fourcc(*'mpeg')

    ## open and set props
    path = "./App/static/"
    vout = cv2.VideoWriter()
    vout.open(path+str(num)+'.mp4', fourcc, fps, sz, True)

    cnt = 0
    while cnt < 20:
        cnt += 1
        print(cnt)
        _, frame = video.read()
        cv2.putText(frame, str(cnt), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
        vout.write(frame)
    vout.release()


def make(video):
    cascPath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    # 打开视频捕获设备
    if not video.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

        # 读视频帧
    ret, frame = video.read()
    # 转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 调用分类器进行检测
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    if len(faces) > 0:
        # faces_exist(True)
        save_video(video, index)
    # save_video(faces)
    # 画矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame
    # 显示视频
    # cv2.imshow('Video', frame)
    # self.video.frame = frame
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    # 关闭摄像头设备


#     video.release()
# # 关闭所有窗口
#     cv2.destroyAllWindows()

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)

        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        global index
        index = index + 1
        make(self.video)
        success, image = self.video.read()
        image = make(self.video)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        # make(self.video)
        # if True:
        #     save_video(self.video, index)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

