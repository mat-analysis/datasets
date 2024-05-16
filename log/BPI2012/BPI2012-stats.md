##### Descriptive Statistics for BPI2012/run1


|       |   Number of Classes |   Number of Attributes |           Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|-----------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 2                   | 8                      | 20.04 / ±154.96485061511424 | 13087             | 100%       |             262200 |            175 |               3 |
| Train | -                   | -                      | -                           | 10469             | 80.00%     |             209522 |            175 |               3 |
| Test  | -                   | -                      | -                           | 2618              | 20.00%     |              52678 |            151 |               3 |

&nbsp;

###### Attributes: originator, transition, timestamp, duration, sourceProcess, subProcess, tid, label

###### MAT Attributes: 'amountRequested', 'regDate', 'resource', 'traceDuration'

###### Labels: low, high

&nbsp;

|        | originator        | transition   | timestamp          | duration           | sourceProcess   | subProcess           | label   |
|--------|-------------------|--------------|--------------------|--------------------|-----------------|----------------------|---------|
| count  | 244190.0          | 262200       | 262200.0           | 262200.0           | 262200          | 262200               | 262200  |
| unique |                   | 3            |                    |                    | 3               | 21                   | 2       |
| top    |                   | COMPLETE     |                    |                    | W               | Completeren aanvraag | low     |
| freq   |                   | 164506       |                    |                    | 170107          | 54850                | 187091  |
| mean   | 8943.364687333633 |              | 1324764336.2537634 | 10.330456983610281 |                 |                      |         |
| std    | 4242.517644579129 |              | 3896798.703668832  | 40.57101669402956  |                 |                      |         |
| min    | 112.0             |              | 1317422324.546     | 0.0                |                 |                      |         |
| 25%    | 10609.0           |              | 1321376828.1360002 | 0.0002213888888888 |                 |                      |         |
| 50%    | 10931.0           |              | 1324980606.4850001 | 0.010865           |                 |                      |         |
| 75%    | 11122.0           |              | 1328179150.77375   | 0.188123125        |                 |                      |         |
| max    | 11339.0           |              | 1331737494.681     | 2468.4068797222226 |                 |                      |         |

&nbsp;

Descriptive Statistics (by Variance): 


|               | Mean               |     Std.Dev |      Variance |
|---------------|--------------------|-------------|---------------|
| timestamp     | 1324764336.2537634 |  3.8968e+06 |    1.5185e+13 |
| duration      | 10.330456983610281 | 40.571      | 1646.01       |
| originator    | 11122.0            | 17.6432     |  311.284      |
| subProcess    | Nabellen offertes  |  5.69881    |   32.4764     |
| transition    | COMPLETE           |  0.879471   |    0.773469   |
| sourceProcess | W                  |  0.581793   |    0.338483   |
| label         | low                |  0.452105   |    0.204399   |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 10469
Samples by Class:

| Label   |    # |
|---------|------|
| low     | 9119 |
| high    | 1350 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 2618
Samples by Class:

| Label   |    # |
|---------|------|
| low     | 2280 |
| high    |  338 |