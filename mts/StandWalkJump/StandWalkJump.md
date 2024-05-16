ECG_Activities Description:
Short duration ECG signals are recorded from a healthy 25-year-old male performing different physical activities to study the effect of motion artifacts on ECG signals and their sparsity.
The raw data was sampled at: 500 Hz, with a resolution of 16 bits before an analogue gain of 100 and ADC was applied.
A Spectrogram of each instance was then created with a window size of 0.061 seconds and an overlap of 70%.
Each instance in this multivariate dataset is arranged such that each dimension is a frequency band from the spectrogram.
There are three classes: standing, walking and jumping, each consists of 9 instances.

ECG_Activities Refrences:
Webpage: https://www.physionet.org/physiobank/database/macecgdb/
PhysioNet Refference: Goldberger AL, Amaral LAN, Glass L, Hausdorff JM, Ivanov PCh, Mark RG, Mietus JE, Moody GB, Peng CK, Stanley HE. PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals. Circulation 101(23):e215-e220 [Circulation Electronic Pages; http://circ.ahajournals.org/content/101/23/e215.full]; 2000 (June 13). PMID: 10851218; doi: 10.1161/01.CIR.101.23.e215
Publication: Vahid Behravan, Neil E. Glover, Rutger Farry, Mohammed Shoaib, Patrick Y. Chiang. Rate-Adaptive Compressed-Sensing and Sparsity Variance of Biomedical Signals. Body Sensor Networks (BSN) 2015 IEEE International Conference in June 2015.
