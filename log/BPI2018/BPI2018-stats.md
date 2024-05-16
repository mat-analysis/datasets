##### Descriptive Statistics for BPI2018/run1


|       |   Number of Classes |   Number of Attributes |           Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|-----------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 2                   | 10                     | 57.39 / ±2915.6084594489716 | 43809             | 100%       |            2514266 |           2973 |              31 |
| Train | -                   | -                      | -                           | 35046             | 80.00%     |            2012525 |           2973 |              24 |
| Test  | -                   | -                      | -                           | 8763              | 20.00%     |             501741 |            907 |              31 |

&nbsp;

###### Attributes: success, orgResource, doctype, subprocess, activity, note, timestamp, duration, tid, label

###### Attributes: 'young farmer',  'selected_random',  'penalty_AJLP',  'application',  'penalty_amount0',  'penalty_BGKV',  'penalty_AUVP',  'applicant',  'risk_factor',  'small farmer',  'penalty_BGP', 'department',  'penalty_C16',  'penalty_BGK',  'penalty_AVUVP',  'penalty_CC',  'penalty_AVJLP',  'penalty_C9',  'cross_compliance',  'rejected',  'penalty_C4',  'penalty_AVGP',  'penalty_ABP',  'penalty_B6',  'penalty_B4',  'penalty_B5',  'penalty_AVBP',  'penalty_B2',  'selected_risk',  'penalty_B3',  'area',  'selected_manually',  'penalty_AGP',  'penalty_B16',  'penalty_GP1',  'basic payment',  'penalty_B5F',  'penalty_V5',  'payment_actual0',  'amount_applied0',  'redistribution',  'penalty_JLP6',  'penalty_JLP7',  'year',  'penalty_JLP5',  'penalty_JLP2',  'penalty_JLP3',  'number_parcels',  'penalty_JLP1',  'traceDuration'

&nbsp;

###### Labels: low, high

&nbsp;

|        | success   | orgResource   | doctype             | subprocess   | activity   | note      | timestamp          | duration           | label   |
|--------|-----------|---------------|---------------------|--------------|------------|-----------|--------------------|--------------------|---------|
| count  | 2514266   | 2396132       | 2514266             | 2514266      | 2514266    | 1275309   | 2514266.0          | 2514266.0          | 2514266 |
| unique | 2         | 164           | 8                   | 8            | 41         | 136       |                    |                    | 2       |
| top    | True      | 727350        | Payment application | Application  | calculate  | automatic |                    |                    | low     |
| freq   | 2481899   | 748950        | 984613              | 928091       | 466141     | 1002487   |                    |                    | 2106963 |
| mean   |           |               |                     |              |            |           | 1477078075.3823583 | 140.2529708057552  |         |
| std    |           |               |                     |              |            |           | 26463649.083913155 | 495.21922950163423 |         |
| min    |           |               |                     |              |            |           | 1399154400.0       | 0.0                |         |
| 25%    |           |               |                     |              |            |           | 1449164093.0085    | 0.0005127777777777 |         |
| 50%    |           |               |                     |              |            |           | 1479392858.0195    | 0.0230555555555555 |         |
| 75%    |           |               |                     |              |            |           | 1502112842.5509999 | 75.82537840277777  |         |
| max    |           |               |                     |              |            |           | 1516363382.0       | 16828.057781944444 |         |

&nbsp;

Descriptive Statistics (by Variance): 


|             | Mean                          |       Std.Dev |         Variance |
|-------------|-------------------------------|---------------|------------------|
| timestamp   | 1477078075.3823583            |   2.64636e+07 |      7.00325e+14 |
| duration    | 140.2529708057552             | 495.219       | 245242           |
| orgResource | Document processing automaton |  40.7044      |   1656.85        |
| activity    | save                          |   6.2436      |     38.9825      |
| doctype     | Entitlement application       |   2.90617     |      8.44582     |
| subprocess  | Main                          |   2.4783      |      6.14199     |
| note        | automatic                     |   2.183       |      4.76548     |
| label       | low                           |   0.368448    |      0.135754    |
| success     | True                          |   0.112728    |      0.0127076   |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 35046
Samples by Class:

| Label   |     # |
|---------|-------|
| low     | 30729 |
| high    |  4317 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 8763
Samples by Class:

| Label   |    # |
|---------|------|
| low     | 7683 |
| high    | 1080 |