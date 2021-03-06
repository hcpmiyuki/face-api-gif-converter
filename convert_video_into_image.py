import sys
import cv2
import os

def save_frame_play(video_path, dir_path, basename, ext='jpg', delay=0, window_name='frame'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow(window_name, frame)
            key = cv2.waitKey(delay) & 0xFF
            if key == ord('c'):
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            elif key == ord('q'):
                break
            n += 1
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            n = 0

    cv2.destroyWindow(window_name)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('引数が足りないよ')
    
    # 元動画のパス
    VIDEO_PATH = './videos/sample.mp4'
    # 画像の保存先のパス
    RESULT_PATH = './images'
    # 画像を保存する時の名前(これに番号が振られる)
    BASE_NAME = 'video_cap'
    
    save_frame_play(VIDEO_PATH, RESULT_PATH, BASE_NAME, delay=0)
