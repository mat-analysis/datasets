Data from a Kaggle competition
https://www.kaggle.com/c/decoding-the-human-brain/data

This problem is extracted from just the train set from the website. 
Our training data consist of MEG recordings and the class labels (Face/Scramble), from 10 subjects (subject01 to subject10), test data from 6 subjects (subject11 to 16). 
For each subject approximately 580-590 trials are available. Each trial consists of 1.5 seconds of MEG recording (starting 0.5sec before the stimulus starts) and the 
related class label, Face (class 1) or Scramble (class 0). 
The data were down-sampled to 250Hz and high-pass filtered at 1Hz. 306 timeseries were recorded, one for each of the 306 channels, for each trial. 
All the pre-processing steps were carried out with mne-python. The trials of each subject are arranged into a 3D data matrix (trial x channel x time) of size 580 x 306 x 375. 
