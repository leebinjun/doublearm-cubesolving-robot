import numpy as np
import cv2
import dlib

detector = dlib.simple_object_detector("detector.svm")
predictor = dlib.shape_predictor('predictor.dat')

cap = cv2.VideoCapture(0)
ret, img = cap.read()

while ret:
    ret, img = cap.read()
    # 灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 识别结果rects
    rects = detector(img_gray, 0)
    for (i,rect) in enumerate(rects):
        x1, y1, x2, y2, w, h = rect.left(), rect.top(), rect.right() + \
            1, rect.bottom() + 1, rect.width(), rect.height()
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (205, 92, 92), 2)
        cv2.putText(img, "magic cube", (x1 - 20, y1 - 20), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (205, 92, 92), 2)

        landmarks = np.matrix([[p.x, p.y] for p in predictor(img,rects[i]).parts()])
        for idx, point in enumerate(landmarks):
            # 六个点的坐标
            pos = (point[0, 0], point[0, 1])
            print(idx, pos)

            # 利用cv2.circle给每个特征点画一个圈，共6个
            cv2.circle(img, pos, 5, color=(0, 255, 0))
            # 利用cv2.putText输出1-6
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(idx+1), pos, font, 0.8, (0, 0, 255), 1,cv2.LINE_AA)

    cv2.namedWindow("img", 2)
    cv2.imshow("img", img)
    key = cv2.waitKey(2)

    if key == ord("q"):
        break
