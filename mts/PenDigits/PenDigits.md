A UCI Archive dataset. See this link for more detailed information: https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits
Paper and image source: F. Alimoglu (1996) Combining Multiple Classifiers for Pen-Based Handwritten Digit Recognition, MSc Thesis, Institute of Graduate Studies in Science and Engineering, Bogazici University.

This is a handwritten digit classification task. 44 writers were asked to draw the digits [0...9], where instances are made up of the x and y coordinates of the pen traced across a digital screen. 

The data was originally recording these coordinates at a 500x500 pixel resolution, however was normalised and sampled to 100x100. Then, on expert knowledge from the dataset's authors, the data was spatially resampled such that instead of each consecutive attribute having a constant time step (100ms) but variable spatial step, they instead had constant spatial step and variable time step. From experimentation by the authors, the data was resampled to 8 spatial points, such that each instance is 2 dimenions of 8 points, with a single class label [0...9] being the digit drawn.
