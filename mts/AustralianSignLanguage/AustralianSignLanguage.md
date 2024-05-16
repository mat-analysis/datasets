Australian Sign Language signs (High Quality) Data Set
Download: Data Folder, Data Set Description

Abstract: This data consists of sample of Auslan (Australian Sign Language) signs. 27 examples of each of 95 Auslan signs were captured from a native signer using high-quality position trackers


Data Set Characteristics:  

Multivariate, Time-Series

Number of Instances:

2565

Area:

N/A

Attribute Characteristics:

Real

Number of Attributes:

22

Date Donated

2002-02-26

Associated Tasks:

Classification

Missing Values?

N/A

Number of Web Hits:

119081


Source:

Original Owner and Donor:

Mohammed Waleed Kadous
School of Computer Science of Engineering
University of New South Wales
Sydney NSW 2052 Australia
Tel: 61 2 9385 6922
waleed '@' cse.unsw.edu.au


Data Set Information:

Data was captured using a setup that consisted of:

- Two Fifth Dimension Technologies (5DT) gloves, one right and one left
- Two Ascension Flock-of-Birds magnetic position trackers, one attached to each hand
- A four-port serial card to cope with four data sources
- A PC (128MB RAM, Intel Pentium II 266MHz) was used

In terms of the quality of the data, the Flock system was far superior to the Nintendo system also available from the same donor. Firstly, this was a two-hand system. Secondly, each position tracker provided 6 degrees of freedom - i.e. roll, pitch and yaw as well as x, y and z. The gloves also provided a full five fingers of data. But the big improvements were in resolution - both accuracy and temporal. Position and orientation were defined to 14-bit accuracy, giving position information with a typical positional error less than one centimetre and angle error less than one half of a degree. Finger bend was measured with 8 bits per finger, of which probably 6 bits were usable once the glove was calibrated. The refresh rate of the complete system was close to 100 frames per second; and all signals had significantly less noise than the Nintendo data.

Samples from a single signer (a native Auslan signer) were collected over a period of nine weeks. In total, 27 samples per sign, and a total of 2565 signs were collected. The average length of each sign was approximately 57 frames.

The data was collected from a volunteer native Auslan signer

The data presented is the raw data with no filtering.

The file consists of 9 subdirectories tctodd1-9. Each directory consists of 3 samples of each sign, captured on a different day. In total there are 95 different signs, with 27 samples per sign. Signs were provided by a native signer volunteer.

Each file consists of a sequence of lines. Each line consists of 22 whitespace-separated numbers representing the 22 channels of information. The list of channels can be found in the domain description file. It also lists the classes. More information can be found here: [Web Link].





Attribute Information:

The following data were recorded for each hand:

* x position expressed relative to a zero point set slightly below the chin. Expressed in meters.

* y position expressed relative to a zero point set slightly below the chin. Expressed in meters.

* z position expressed relative to a zero point set slightly below the chin. Expressed in meters.

* roll expressed as a value between -0.5 and 0.5 with 0 being palm down. Positive means the palm is rolled clockwise from the perspective of the signer. To get degrees, multiply by 180.

* pitch expressed as a value between -0.5 and 0.5 with 0 being palm flat (horizontal). Positive means the palm is pointing up. To get degrees, multiply by 180.

* yaw expressed a value between -1.0 and 1.0 with 0 being palm straight ahead from the perspective of the signer. Positive means clockwise from the perspective above the signer. To get degrees, multiply by 180.

* Thumb bend measure between 0 and 1. 0 means totally flat, 1 means totally bent. However, the finger bend measurements are not very exact.

* Forefinger bend measure between 0 and 1. 0 means totally flat, 1 means totally bent. However, the finger bend measurements are not very exact.

* Middle finger bend measure between 0 and 1. 0 means totally flat, 1 means totally bent. However, the finger bend measurements are not very exact.

* Ring finger bend measure between 0 and 1. 0 means totally flat, 1 means totally bent. However, the finger bend measurements are not very exact.

* Little finger bend measure between 0 and 1. 0 means totally flat, 1 means totally bent. However, the finger bend measurements are not very exact.


Relevant Papers:

Kadous, M. W., "Temporal Classification: Extending the Classification Paradigm to Multivariate Time Series", PhD Thesis (draft), School of Computer Science and Engineering, University of New South Wales, 2002.
[Web Link]

Also available from: [Web Link]


Papers That Cite This Data Set1:


Mohammed Waleed Kadous and Claude Sammut. The University of New South Wales School of Computer Science and Engineering Temporal Classification: Extending the Classification Paradigm to Multivariate Time Series. [View Context].



Citation Request:

Please cite the PhD thesis above as the data source:

Kadous, M. W., "Temporal Classification: Extending the Classification
Paradigm to Multivariate Time Series", PhD Thesis (draft), School of
Computer Science and Engineering, University of New South Wales, 2002.

Source: https://archive.ics.uci.edu/ml/datasets/Australian+Sign+Language+signs+(High+Quality)