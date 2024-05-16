##### Descriptive Statistics for BPI2011/run1


|       |   Number of Classes |   Number of Attributes |            Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|------------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 2                   | 8                      | 131.49 / ±1682.5118110236222 | 1143              | 100%       |             150291 |           1814 |               1 |
| Train | -                   | -                      | -                            | 914               | 79.97%     |             118118 |           1814 |               1 |
| Test  | -                   | -                      | -                            | 229               | 20.03%     |              32173 |           1690 |               1 |

&nbsp;

###### Attributes: Group, ExecutionsNumber, SpecialismCode, ProducerCode, ActivityCode, duration, tid, label

###### MAT Attributes: 'Section', 'Age', 'TreatmentCode', 'Diagnosis', 'DiagnosisCode', 'DiagnosisTreatmentCombinationID', 'GeneralSpecialismCode', 'Patient', 'traceDuration'

###### Labels: low, high

&nbsp;

|        | Group                          | ExecutionsNumber   | SpecialismCode    | ProducerCode   | ActivityCode   | duration          | label   |
|--------|--------------------------------|--------------------|-------------------|----------------|----------------|-------------------|---------|
| count  | 150275                         | 150291.0           | 150291.0          | 150291         | 150291         | 150291.0          | 150291  |
| unique | 42                             |                    |                   | 117            | 710            |                   | 2       |
| top    | General Lab Clinical Chemistry |                    |                   | CHE2           | 370000         |                   | low     |
| freq   | 94917                          |                    |                   | 31859          | 15341          |                   | 139596  |
| mean   |                                | 1.7451144779128491 | 63.56994763492158 |                |                | 70.57412619518135 |         |
| std    |                                | 15.20378114407862  | 34.73461159376182 |                |                | 549.8360887926235 |         |
| min    |                                | -300.0             | 0.0               |                |                | 0.0               |         |
| 25%    |                                | 1.0                | 7.0               |                |                | 0.0               |         |
| 50%    |                                | 1.0                | 86.0              |                |                | 0.0               |         |
| 75%    |                                | 1.0                | 86.0              |                |                | 0.0               |         |
| max    |                                | 800.0              | 99.0              |                |                | 24720.0           |         |

&nbsp;

Descriptive Statistics (by Variance): 


|                  | Mean                           |    Std.Dev |       Variance |
|------------------|--------------------------------|------------|----------------|
| duration         | 70.57412619518135              | 549.836    | 302320         |
| ActivityCode     | 613000                         |  62.7582   |   3938.59      |
| SpecialismCode   | 63.56994763492158              |  34.7346   |   1206.49      |
| ExecutionsNumber | 1.7451144779128491             |  15.2038   |    231.155     |
| ProducerCode     | H5ZU                           |   8.985    |     80.7302    |
| Group            | General Lab Clinical Chemistry |   2.2649   |      5.12978   |
| label            | low                            |   0.257095 |      0.0660979 |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 914
Samples by Class:

| Label   |   # |
|---------|-----|
| low     | 874 |
| high    |  40 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 229
Samples by Class:

| Label   |   # |
|---------|-----|
| low     | 219 |
| high    |  10 |