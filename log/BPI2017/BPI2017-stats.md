##### Descriptive Statistics for BPI2017/run1


|       |   Number of Classes |   Number of Attributes |           Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|-----------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 2                   | 6                      | 38.16 / ±141.84369545209304 | 31509             | 100%       |            1202267 |            180 |              10 |
| Train | -                   | -                      | -                           | 25206             | 80.00%     |             961148 |            180 |              10 |
| Test  | -                   | -                      | -                           | 6303              | 20.00%     |             241119 |            180 |              10 |

&nbsp;

###### Attributes: Action, User, EventOrigin, Duration, tid, label


###### MAT Attributes: 'LoanGoal', 'ApplicationType', 'RequestedAmount', 'ApplicationID', 'traceDuration'


###### Labels: low, high

&nbsp;

|        | Action      | User    | EventOrigin   | Duration           | label   |
|--------|-------------|---------|---------------|--------------------|---------|
| count  | 1202267     | 1202267 | 1202267       | 1202267.0          | 1202267 |
| unique | 5           | 149     | 3             |                    | 2       |
| top    | statechange | User_1  | Workflow      |                    | low     |
| freq   | 358940      | 148404  | 768823        |                    | 1132197 |
| mean   |             |         |               | 13.77458746361301  |         |
| std    |             |         |               | 64.70712225479774  |         |
| min    |             |         |               | 0.0                |         |
| 25%    |             |         |               | 0.0                |         |
| 50%    |             |         |               | 0.0013888888888888 |         |
| 75%    |             |         |               | 0.0722222222222222 |         |
| max    |             |         |               | 3267.020833333333  |         |

&nbsp;

Descriptive Statistics (by Variance): 


|             | Mean              |   Std.Dev |     Variance |
|-------------|-------------------|-----------|--------------|
| Duration    | 13.77458746361301 | 64.7071   | 4187.01      |
| User        | User_4            | 40.5714   | 1646.04      |
| Action      | Deleted           |  1.40058  |    1.96162   |
| EventOrigin | Workflow          |  0.599228 |    0.359074  |
| label       | low               |  0.234275 |    0.0548848 |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 25206
Samples by Class:

| Label   |     # |
|---------|-------|
| low     | 24177 |
| high    |  1029 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 6303
Samples by Class:

| Label   |    # |
|---------|------|
| low     | 6045 |
| high    |  258 |