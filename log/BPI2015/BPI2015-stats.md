##### Descriptive Statistics for BPI2015/run1


|       |   Number of Classes |   Number of Attributes |           Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|-----------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 5                   | 12                     | 46.49 / ±107.50893963533369 | 5649              | 100%       |             262628 |            154 |               1 |
| Train | -                   | -                      | -                           | 4517              | 79.96%     |             210084 |            154 |               1 |
| Test  | -                   | -                      | -                           | 1132              | 20.04%     |              52544 |            116 |               1 |

&nbsp;

###### Attributes: question, dateFinished, actionCode, activityNameEN, planned, monitoringResource, executingResource, conceptName, duration, durationClass, tid, label


###### MAT Attributes: 'endDate', 'caseStatus', 'SUMleges', 'lastPhase', 'responsibleActor', 'parts', 'startDate', 'requestComplete', 'IDofConceptCase', 'includesSubCases', 'traceDuration', 'generalConceptName'


###### Labels: 1, 2, 3, 4, 5

&nbsp;

|        | question   | dateFinished      | actionCode   | activityNameEN            | planned            | monitoringResource   | executingResource   | conceptName       | duration           | durationClass   | label              |
|--------|------------|-------------------|--------------|---------------------------|--------------------|----------------------|---------------------|-------------------|--------------------|-----------------|--------------------|
| count  | 262628     | 262628.0          | 262405       | 262628                    | 222226.0           | 262628.0             | 262628.0            | 262628.0          | 262628.0           | 262628          | 262628.0           |
| unique | 1666       |                   | 495          | 356                       |                    |                      |                     |                   |                    | 2               |                    |
| top    | EMPTY      |                   | 01_HOOFD_010 | send confirmation receipt |                    |                      |                     |                   |                    | low             |                    |
| freq   | 141063     |                   | 5644         | 9090                      |                    |                      |                     |                   |                    | 245612          |                    |
| mean   |            | 1357074253.088947 |              |                           | 1361538212.0493193 | 1136039.5681838952   | 1150551.3755464002  | 7911533.890133573 | 52.3020252547779   |                 | 3.0634776185326773 |
| std    |            | 38567560.96596588 |              |                           | 39951639.33152545  | 1138139.3406258733   | 1961550.3821030098  | 5018565.870902556 | 386.5975535454301  |                 | 1.428325253431176  |
| min    |            | 1286447963.0      |              |                           | 1286017481.0       | 6.0                  | 6.0                 | 2742737.0         | 0.0                |                 | 1.0                |
| 25%    |            | 1323084338.0      |              |                           | 1326380889.0       | 560530.0             | 560532.0            | 4535665.0         | 0.0                |                 | 2.0                |
| 50%    |            | 1355917186.0      |              |                           | 1365057875.5       | 560696.0             | 560749.0            | 6376407.0         | 0.0                |                 | 3.0                |
| 75%    |            | 1389830400.0      |              |                           | 1395239143.75      | 1550894.0            | 560890.0            | 9025494.0         | 0.0019444444444444 |                 | 4.0                |
| max    |            | 1425427200.0      |              |                           | 1425565688.0       | 22445896.0           | 22445896.0          | 24154137.0        | 32363.351944444443 |                 | 5.0                |

&nbsp;

Descriptive Statistics (by Variance): 


|                    | Mean                       |         Std.Dev |         Variance |
|--------------------|----------------------------|-----------------|------------------|
| dateFinished       | 1357074253.088947          |     3.85676e+07 |      1.48746e+15 |
| conceptName        | 7911533.890133573          |     5.01857e+06 |      2.5186e+13  |
| executingResource  | 1150551.3755464002         |     1.96155e+06 |      3.84768e+12 |
| monitoringResource | 1136039.5681838952         |     1.13814e+06 |      1.29536e+12 |
| planned            | 1371651015.0               | 51620           |      2.66463e+09 |
| duration           | 52.3020252547779           |   386.598       | 149458           |
| question           | EMPTY                      |    88.8863      |   7900.78        |
| actionCode         | 01_HOOFD_510_1             |    82.8467      |   6863.57        |
| activityNameEN     | completed subcases content |    58.5253      |   3425.21        |
| label              | 3.0634776185326773         |     1.42833     |      2.04011     |
| durationClass      | low                        |     0.246157    |      0.0605934   |

&nbsp;

###### Labels for TRAIN:

Number of Samples: 4517
Samples by Class:

|   Label |    # |
|---------|------|
|       3 | 1127 |
|       1 |  959 |
|       5 |  924 |
|       4 |  842 |
|       2 |  665 |

&nbsp;

###### Labels for TEST.:

Number of Samples: 1132
Samples by Class:

|   Label |   # |
|---------|-----|
|       3 | 282 |
|       1 | 240 |
|       5 | 232 |
|       4 | 211 |
|       2 | 167 |