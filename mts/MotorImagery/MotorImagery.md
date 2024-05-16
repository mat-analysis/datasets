Problem BCI III Dataset 1
http://bbci.de/competition/iii/desc_I.html

Data set I �motor imagery in ECoG recordings, session-to-session transfer�
Data set provided by University of T�bingen, Germany, Dept. of Computer Engineering (Prof. Rosenstiel) and Institute of Medical Psychology and Behavioral Neurobiology (Niels Birbaumer), and 
Max-Planck-Institute for Biological Cybernetics, T�bingen, Germany (Bernhard Sch�lkopf), and 
Universit�t Bonn, Germany, Dept. of Epileptology (Prof. Elger)
Correspondence to Michael Schr�der <schroedm@informatik.uni-tuebingen.de>

The Thrill
The design of a classifier for a BCI system is very challenging when a classifier that was trained on the first day shall classify data recorded during 
following days (if possible, without retraining): the patient might be in a different state concerning motivation, fatigue etc. so that his brain will show different electrical activity. In addition, the recording system might have undergone slight changes concerning electrode positions and impedances. Our data set reflects this sitation: training data and test data were recorded from the same subject and with the same task, but on two different days with about 1 week in between. Learn on the data of the first session and do your best on the data of the second session!
Experiment
During the BCI experiment, a subject had to perform imagined movements of either the left small finger or the tongue. 
The time series of the electrical brain activity was picked up during these trials using a 8x8 ECoG platinum electrode grid which 
was placed on the contralateral (right) motor cortex. The grid was assumed to cover the right motor cortex completely, 
but due to its size (approx. 8x8cm) it partly covered also surrounding cortex areas. All recordings were performed with a sampling rate of 1000Hz. 
After amplification the recorded potentials were stored as microvolt values. Every trial consisted of either an imagined tongue or an 
imagined finger movement and was recorded for 3 seconds duration. To avoid visually evoked potentials being reflected by the data, 
the recording intervals started 0.5 seconds after the visual cue had ended.
Format of the Data

The EEG data has 64 dimensions, each of which is 3000 long (3 seconds measurement). 
The train data has 278 cases, the test data 100. The class labels are finger or tongue (the imagined movements). 

The best submitted solution obtained 91% accuracy on the test data.
http://bbci.de/competition/iii/results/index.html

Reference:
Thomas Lal, Thilo Hinterberger, Guido Widman, Michael Schr�der, Jeremy Hill, Wolfgang Rosenstiel, Christian Elger, Bernhard Sch�lkopf, Niels Birbaumer. Methods Towards Invasive Human Brain Computer Interfaces. Advances in Neural Information Processing Systems (NIPS), 2004
