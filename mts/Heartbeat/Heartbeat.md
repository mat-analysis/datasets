Heartbeat Description:
This dataset is derived from the PhysioNet/CinC Challenge 2016.
Heart sound recordings were sourced from several contributors around the world, collected at either a clinical or nonclinical environment, from both healthy subjects and pathological patients.
The heart sound recordings were collected from different locations on the body. The typical four locations are aortic area, pulmonic area, tricuspid area and mitral area, but could be one of nine different locations. 
The sounds were divided into two classes: normal and abnormal. The normal recordings were from healthy subjects and the abnormal ones were from patients with a confirmed cardiac diagnosis. 
The patients suffer from a variety of illnesses, but typically they are heart valve defects and coronary artery disease patients. 
Heart valve defects include mitral valve prolapse, mitral regurgitation, aortic stenosis and valvular surgery. All the recordings from the patients were generally labeled as abnormal.
Both healthy subjects and pathological patients include both children and adults.

Each recording was truncated to 5 seconds. A Spectrogram of each instance was then created with a window size of 0.061 seconds and an overlap of 70%.
Each instance in this multivariate dataset is arranged such that each dimension is a frequency band from the spectrogram.
The two classes normal and abnormal consist of 113 and 296 respectivley. 

Heartbeat Refferences:
Webpage: https://www.physionet.org/physiobank/database/challenge/2016/
PhysioNet Refference: Goldberger AL, Amaral LAN, Glass L, Hausdorff JM, Ivanov PCh, Mark RG, Mietus JE, Moody GB, Peng CK, Stanley HE. PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals. Circulation 101(23):e215-e220 [Circulation Electronic Pages; http://circ.ahajournals.org/content/101/23/e215.full]; 2000 (June 13). PMID: 10851218; doi: 10.1161/01.CIR.101.23.e215
Publication: Liu et al. An open access database for the evaluation of heart sound algorithms. Physiol Meas. 2016 Nov 21;37(12):2181-2213 https://www.ncbi.nlm.nih.gov/pubmed/27869105
