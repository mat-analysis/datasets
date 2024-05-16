##### Descriptive Statistics for StandWalkJump


|       |   Number of Classes |   Number of Attributes |   Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|---------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 3                   | 6                      | 2500.00 / ±0.0      | 27                | 100%       |              67500 |           2500 |            2500 |
| Train | -                   | -                      | -                   | 12                | 44.44%     |              30000 |           2500 |            2500 |
| Test  | -                   | -                      | -                   | 15                | 55.56%     |              37500 |           2500 |            2500 |

&nbsp;

###### Attributes: channel_1, channel_2, channel_3, channel_4, tid, label


###### Labels: standing, walking, jumping

&nbsp;

|        | channel_1            | channel_2            | channel_3            | channel_4            | label    |
|--------|----------------------|----------------------|----------------------|----------------------|----------|
| count  | 67500.0              | 67500.0              | 67500.0              | 67500.0              | 67500    |
| unique |                      |                      |                      |                      | 3        |
| top    |                      |                      |                      |                      | standing |
| freq   |                      |                      |                      |                      | 22500    |
| mean   | 0.007119851851851861 | 0.005739851851851961 | 0.005218370370370465 | 0.010983407407407456 |          |
| std    | 0.5084597875757156   | 0.534652421603174    | 0.4590575662290729   | 0.4567346604363858   |          |
| min    | -5.27                | -3.61                | -4.29                | -5.31                |          |
| 25%    | -0.12                | -0.14                | -0.11                | -0.12                |          |
| 50%    | -0.01                | -0.01                | -0.01                | -0.02                |          |
| 75%    | 0.05                 | 0.06                 | 0.07                 | 0.08                 |          |
| max    | 5.76                 | 7.06                 | 5.88                 | 7.06                 |          |

&nbsp;

Descriptive Statistics (by Variance): 


|           | Mean                 |   Std.Dev |   Variance |
|-----------|----------------------|-----------|------------|
| label     | walking              |  0.816497 |   0.666667 |
| channel_2 | 0.005739851851851961 |  0.534652 |   0.285853 |
| channel_1 | 0.007119851851851861 |  0.50846  |   0.258531 |
| channel_3 | 0.005218370370370465 |  0.459058 |   0.210734 |
| channel_4 | 0.010983407407407456 |  0.456735 |   0.208607 |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 12
Samples by Class:
| Label    |   # |
|----------|-----|
| jumping  |   4 |
| standing |   4 |
| walking  |   4 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 15
Samples by Class:
| Label    |   # |
|----------|-----|
| jumping  |   5 |
| standing |   5 |
| walking  |   5 |