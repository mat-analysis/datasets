A UCI Archive dataset. See this link for more detailed information: https://archive.ics.uci.edu/ml/datasets/Japanese+Vowels
Paper: M. Kudo, J. Toyama and M. Shimbo. (1999). "Multidimensional Curve Classification Using Passing-Through Regions". Pattern Recognition Letters, Vol. 20, No. 11--13, pages 1103--1111. 


9 Japanese-male speakers were recorded saying the vowels 'a' and 'e'. A '12-degree linear prediction analysis' is applied to the raw recordings to obtain time-series with 12 dimensions, a originally a length between 7 and 29. In this dataset, instances have been padded to the longest length, 29. The classification task is to predict the speaker. Therefore, each instance is a transformed utterance, 12*29 values with a single class label attached, [1...9].

The given training set is comprised of 30 utterances for each speaker, however the test set has a varied distribution based on external factors of timing and experimenal availability, between 24 and 88 instances per speaker. 
