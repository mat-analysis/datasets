##### Descriptive Statistics for RacketSports


|       |   Number of Classes |   Number of Attributes |   Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|---------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 4                   | 8                      | 30.00 / ±0.0        | 303               | 100%       |               9090 |             30 |              30 |
| Train | -                   | -                      | -                   | 151               | 49.83%     |               4530 |             30 |              30 |
| Test  | -                   | -                      | -                   | 152               | 50.17%     |               4560 |             30 |              30 |

&nbsp;

###### Attributes: channel_1, channel_2, channel_3, channel_4, channel_5, channel_6, tid, label


###### Labels: badminton_smash, badminton_clear, squash_forehandboast, squash_backhandboast

&nbsp;

|        | channel_1         | channel_2           | channel_3          | channel_4            | channel_5             | channel_6            | label           |
|--------|-------------------|---------------------|--------------------|----------------------|-----------------------|----------------------|-----------------|
| count  | 9090.0            | 9090.0              | 9090.0             | 9090.0               | 9090.0                | 9090.0               | 9090            |
| unique |                   |                     |                    |                      |                       |                      | 4               |
| top    |                   |                     |                    |                      |                       |                      | badminton_clear |
| freq   |                   |                     |                    |                      |                       |                      | 2580            |
| mean   | 2.733264254125404 | 0.08338527172717344 | -1.884903598349832 | -0.26211248668866793 | -0.06499243553355345  | -0.25613117843784294 |                 |
| std    | 7.615943525392861 | 6.5607305504950135  | 6.87621777758201   | 4.702129559958068    | 4.17827988281603      | 3.9317779817944487   |                 |
| min    | -29.32534         | -29.395939          | -29.294456         | -34.871536           | -34.639824            | -32.48249            |                 |
| 25%    | -0.763155         | -2.7349125          | -4.203197          | -1.214498            | -0.828309             | -0.929517            |                 |
| 50%    | 1.152154          | -0.05552            | -1.011441          | -0.069248            | -0.014648500000000002 | -0.071911            |                 |
| 75%    | 4.78317275        | 2.4090945           | 1.35539125         | 1.028062             | 0.729764              | 0.828309             |                 |
| max    | 29.385334         | 29.082859           | 27.494814          | 34.8742              | 34.61319              | 23.261896            |                 |

&nbsp;

Descriptive Statistics (by Variance): 


|           | Mean                 |   Std.Dev |   Variance |
|-----------|----------------------|-----------|------------|
| channel_1 | 2.733264254125404    |   7.61594 |   58.0026  |
| channel_3 | -1.884903598349832   |   6.87622 |   47.2824  |
| channel_2 | 0.08338527172717344  |   6.56073 |   43.0432  |
| channel_4 | -0.26211248668866793 |   4.70213 |   22.11    |
| channel_5 | -0.06499243553355345 |   4.17828 |   17.458   |
| channel_6 | -0.25613117843784294 |   3.93178 |   15.4589  |
| label     | badminton_clear      |   1.10171 |    1.21376 |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 151
Samples by Class:
| Label                |   # |
|----------------------|-----|
| badminton_clear      |  43 |
| badminton_smash      |  39 |
| squash_forehandboast |  35 |
| squash_backhandboast |  34 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 152
Samples by Class:
| Label                |   # |
|----------------------|-----|
| badminton_clear      |  43 |
| badminton_smash      |  40 |
| squash_forehandboast |  35 |
| squash_backhandboast |  34 |