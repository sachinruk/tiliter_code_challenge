# Tiliter Coding Challenge

## Video Playback and Segmentation
Both these two tasks let a user play, pause and rewind and exit the player. When playing a user can press:
- p: play/ pause
- b: back **one** frame
- q: quit

For segmentation I attempted to use opencv's `createBackgroundSubtractorMOG2` with poor results. Instead I converted the colour space to 'Lab' and looked at the difference after removing the 'L' (light intensity) channel. After that a simple threshold was used to classify as background and foreground. To smoothen the foreground mask I used opening and closing morphology operations.

### Usage
The parameters for these scripts are:
- video_file_path: path to video
- fps (optional): frames per second
- display_resolution (optional): resolution
- monochrome (optional): whether grayscale or not (not used in segment.py)
```
python vid_playback.py --v ./data/video_2.mp4 
python segment.py --v ./data/video_2.mp4 
```

## Machine Learning
Apologies for not using a script, but that would have ignored the intricacies of using fastai library.

### MNIST challenge
- Accuracy of 98.66% on test set.
- Accuracy of 83.39% on custom set.

Model is a usual stacked convolution layer, which is flattened at output layer. The accuracy on custom set is achieved by doing 1 - x before sending through model.

### Flowers challenge
- Accuracy of 87.04%.

I used transfer learning here by using resnet18 as a base. Due to the limited number of images I used data augmentation by using fastai's default transforms (eg. flipping, changing lighting etc.).
