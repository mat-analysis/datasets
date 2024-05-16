##### Descriptive Statistics for Epilepsy


|       |   Number of Classes |   Number of Attributes |   Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|---------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 4                   | 5                      | 206.00 / ±0.0       | 275               | 100%       |              56650 |            206 |             206 |
| Train | -                   | -                      | -                   | 137               | 49.82%     |              28222 |            206 |             206 |
| Test  | -                   | -                      | -                   | 138               | 50.18%     |              28428 |            206 |             206 |

&nbsp;

###### Attributes: channel_1, channel_2, channel_3, tid, label


###### Labels: epilepsy, walking, running, sawing

&nbsp;

|        | channel_1            | channel_2           | channel_3            | label   |
|--------|----------------------|---------------------|----------------------|---------|
| count  | 56650.0              | 56650.0             | 56650.0              | 56650   |
| unique |                      |                     |                      | 4       |
| top    |                      |                     |                      | walking |
| freq   |                      |                     |                      | 15244   |
| mean   | -0.03905366284201208 | -0.2603154457193266 | -0.12904165931156267 |         |
| std    | 1.0102332111974488   | 1.0118214701610089  | 0.5078352647314333   |         |
| min    | -3.59                | -3.59               | -2.19                |         |
| 25%    | -0.82                | -0.75               | -0.47                |         |
| 50%    | -0.01                | -0.27               | -0.11                |         |
| 75%    | 0.76                 | 0.36                | 0.17                 |         |
| max    | 3.59                 | 3.59                | 2.58                 |         |

&nbsp;

Descriptive Statistics (by Variance): 


|           | Mean                 |   Std.Dev |   Variance |
|-----------|----------------------|-----------|------------|
| label     | walking              |  1.08575  |   1.17884  |
| channel_2 | -0.2603154457193266  |  1.01182  |   1.02378  |
| channel_1 | -0.03905366284201208 |  1.01023  |   1.02057  |
| channel_3 | -0.12904165931156267 |  0.507835 |   0.257897 |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 137
Samples by Class:
| Label    |   # |
|----------|-----|
| walking  |  37 |
| running  |  36 |
| epilepsy |  34 |
| sawing   |  30 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 138
Samples by Class:
| Label    |   # |
|----------|-----|
| running  |  37 |
| walking  |  37 |
| epilepsy |  34 |
| sawing   |  30 |