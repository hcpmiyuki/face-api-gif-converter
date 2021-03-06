import cognitive_face as CF
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
import gif
import settings
import sys
from time import sleep

# face api準備
KEY = settings.AP
BASE_URL = 'https://westus2.api.cognitive.microsoft.com/face/v1.0/'
CF.Key.set(KEY)
CF.BaseUrl.set(BASE_URL)

# 1分間のAPIの制限
API_LIMIT = 20
# 制限に達したら65秒まつ
SLEEP_TIME = 65

FONT_SCALE = 1.2
COLOR_DIC = {
    'anger':(255,0,0),
    'contempt':(0,0,128),
    'disgust': (128,0,128),
    'fear':(0,0,255),
    'happiness': (255,0,255),
    'neutral': (128,128,128),
    'sadness': (100,149,237),
    'surprise': (244,164,96)
}
FONT_FACE = cv2.FONT_HERSHEY_DUPLEX
FRAME_THICKNESS = 6
FONT_THICKNESS = 2


@gif.frame
def analyze_face_emotion(img_path):
    faces = CF.face.detect(img_path, attributes='emotion')
    img = cv2.imread(img_path)
    for face in faces:
        rect = face['faceRectangle']
        width = rect['width']
        height = rect['height']
        top = rect['top']
        left = rect['left']
        
        emotion_dic = face['faceAttributes']['emotion']
        best_index = np.argmax(list(emotion_dic.values()))
        emotion_label = list(emotion_dic.keys())[best_index]
        emotion_conf = list(emotion_dic.values())[best_index]
        emotion_color = COLOR_DIC[emotion_label]
        
        cv2.rectangle(img,
                    (int(left), int(top)),
                    (int(left+width), int(top+height)),
                    emotion_color,
                    FRAME_THICKNESS)
        
        cv2.putText(img,
                    emotion_label + ": " + str(emotion_conf),
                    (int(left), top+height+30),
                    FONT_FACE,
                    FONT_SCALE,
                    emotion_color,
                    FONT_THICKNESS)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    
    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('引数が足りないよ')
    
    # 画像が保存されているディレクトリのパス
    IMG_DIR_PATH = './images'
    # gifを保存する時のパス
    SAVE_FILE_PATH = './gifs/sample.gif'
    
    img_names = sorted([_ for _ in os.listdir(IMG_DIR_PATH) if _.endswith('.jpg')])
    # グラフのアニメーション作成
    frames = []
    
    count = 0
    for img_name in img_names:
        img_path = os.path.join(IMG_DIR_PATH, img_name)
        frame = analyze_face_emotion(img_path)
        frames.append(frame)
        count += 1
        
        if count % API_LIMIT == 0 and count != 100:
            print('{}回目のapiのリクエスト制限に達しました。寝ます。。。'.format(count // API_LIMIT))
            sleep(65)
            
    # gifを保存
    gif.save(frames, SAVE_FILE_PATH, duration=1, unit="s", between="startend")