import cv2
import numpy as np

COUNTER_THRESH = 50
DIFF_THRESH = 50

class Background():
    def __init__(self):
        # self.backSub = cv2.createBackgroundSubtractorMOG2()
        self.background = None
        self.counter = 0
        self.kernel = np.ones((5,5),np.uint8)
        
    def subtract(self, frame):
        # mask = self.backSub.apply(frame)
        if self.background is None:
            self.background = self.cvt_colorspace(frame)
        elif self.counter < COUNTER_THRESH:
            self.update_bg(frame)
            self.counter += 1
        
        mask2 = self.get_fg(frame)
        
        return mask2[...,None] * frame
        # return cv2.bitwise_and(frame, frame, mask = mask)
    
    def update_bg(self, frame, alpha=0.9):
        frame = self.cvt_colorspace(frame)
        self.background = alpha * self.background + (1-alpha) * frame
        # self.background = self.background.astype(np.uint8)
        
    def get_fg(self, frame):
        diff = self.cvt_colorspace(frame) - self.background
        diff = np.square(diff.astype(float)).sum(axis=-1)
        mask = diff > DIFF_THRESH
        mask = self.smoothen_mask(mask)
        return mask
    
    def cvt_colorspace(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)[...,1:]
    
    def smoothen_mask(self, mask):
        mask = cv2.morphologyEx(mask.astype(np.uint8), cv2.MORPH_OPEN, self.kernel)
        mask = cv2.morphologyEx(mask.astype(np.uint8), cv2.MORPH_CLOSE, self.kernel)
        return mask