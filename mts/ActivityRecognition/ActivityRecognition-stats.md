##### Descriptive Statistics for ActivityRecognition


|       |   Number of Classes |   Number of Attributes |             Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|-------------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 7                   | 5                      | 14245.76 / ±69502.24444444444 | 135               | 100%       |            1923177 |          83748 |             505 |
| Train | -                   | -                      | -                             | 91                | 67.41%     |            1262231 |          83660 |             320 |
| Test  | -                   | -                      | -                             | 44                | 32.59%     |             660946 |          83748 |             505 |

&nbsp;

###### Attributes: acceleration_x, acceleration_y, acceleration_z, tid, label


###### Labels: 1-workingatcomputer, 2-standingup-walking-updownstairs, 3-standing, 4-walking, 5-updownstairs, 6-walkingtalking, 7-talkingstanding

&nbsp;

|        | acceleration_x     | acceleration_y     | acceleration_z    | label               |
|--------|--------------------|--------------------|-------------------|---------------------|
| count  | 1923177.0          | 1923177.0          | 1923177.0         | 1923177             |
| unique |                    |                    |                   | 7                   |
| top    |                    |                    |                   | 1-workingatcomputer |
| freq   |                    |                    |                   | 608667              |
| mean   | 1987.4788763592742 | 2382.2996099682973 | 1970.488386664358 |                     |
| std    | 111.34080995427884 | 100.21072458396264 | 94.49120736909546 |                     |
| min    | 282.0              | 2.0                | 1.0               |                     |
| 25%    | 1904.0             | 2337.0             | 1918.0            |                     |
| 50%    | 1992.0             | 2367.0             | 1988.0            |                     |
| 75%    | 2076.0             | 2412.0             | 2032.0            |                     |
| max    | 3828.0             | 4095.0             | 4095.0            |                     |

&nbsp;

Descriptive Statistics (by Variance): 


|                | Mean               |   Std.Dev |    Variance |
|----------------|--------------------|-----------|-------------|
| acceleration_x | 1987.4788763592742 | 111.341   | 12396.8     |
| acceleration_y | 2382.2996099682973 | 100.211   | 10042.2     |
| acceleration_z | 1970.488386664358  |  94.4912  |  8928.59    |
| label          | 4-walking          |   2.43978 |     5.95255 |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 91
Samples by Class:
| Label                             |   # |
|-----------------------------------|-----|
| 3-standing                        |  31 |
| 1-workingatcomputer               |  10 |
| 2-standingup-walking-updownstairs |  10 |
| 4-walking                         |  10 |
| 5-updownstairs                    |  10 |
| 6-walkingtalking                  |  10 |
| 7-talkingstanding                 |  10 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 44
Samples by Class:
| Label                             |   # |
|-----------------------------------|-----|
| 3-standing                        |  14 |
| 1-workingatcomputer               |   5 |
| 2-standingup-walking-updownstairs |   5 |
| 4-walking                         |   5 |
| 5-updownstairs                    |   5 |
| 6-walkingtalking                  |   5 |
| 7-talkingstanding                 |   5 |