import cv2
import sys
import time
import numpy as np
from parser import *
import argparse

SEC2MS = 1000

parser = argparse.ArgumentParser()
parser.add_argument("--video_file_path", help="video file path", type=str)
parser.add_argument("--fps", help="Frames per second", type=int, default=60)
parser.add_argument("--display_resolution", help="Resolution eg. 360x180", type=str, default='360x360')
parser.add_argument("--monochrome", help="grayscale or not", type=bool, default=False)
args = parser.parse_args()
 
video_file_path = args.video_file_path
fps = args.fps
delay = 1 / fps
display_resolution = res_input(args.display_resolution)
monochrome = args.monochrome

video = cv2.VideoCapture(video_file_path) # Read video
 
# Exit if video not opened
if not video.isOpened():
    print("Could not open video")
    sys.exit()

# Read first frame
ok, frame = video.read()
if not ok:
    print("Cannot read video file")
    sys.exit()

wait = int(delay * 1000)
start = time.time()
isPaused = False
frameBuffer = []
cursor = 0

while ok or cursor < len(frameBuffer):
    key = cv2.waitKey(wait) & 0xFF
    if  key == ord('q'): # quit
        break
    elif key == ord('p'): # pause/ play
        isPaused = not isPaused
        continue
    elif key == ord('b'): # step back
        cursor = max(cursor - 1, 0)
        print(f'Cursor at frame {cursor}')
        cv2.imshow("Frame", frameBuffer[cursor])
    
    # capture the frames from video regardless
    if ok:
        frame = cv2.resize(frame, display_resolution)
        if monochrome:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameBuffer.append(frame)
        ok, frame = video.read()
    
    if not isPaused:
        cv2.imshow("Frame", frameBuffer[cursor])
        cursor += 1
    
# close all windows
video.release()
cv2.destroyAllWindows()
print(f'Process took {time.time() - start:.2f} seconds')