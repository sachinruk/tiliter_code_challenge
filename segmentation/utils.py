import cv2

def show_frames(**kwargs):
    for k,v in kwargs.items():
        if v is not None:
            cv2.imshow(k, v)