##### Descriptive Statistics for Geolife/run1


|       |   Number of Classes |   Number of Attributes |           Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|-----------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 6                   | 5                      | 119.79 / ±130.2097902097902 | 5434              | 100%       |             650940 |            250 |              31 |
| Train | -                   | -                      | -                           | 4346              | 79.98%     |             519276 |            250 |              31 |
| Test  | -                   | -                      | -                           | 1088              | 20.02%     |             131664 |            250 |              31 |

&nbsp;

###### Attributes: time, lat, lon, tid, label


###### Labels: train, taxibus, walk, subway, bike, car

&nbsp;

|        | time               | lat                | lon                | label   |
|--------|--------------------|--------------------|--------------------|---------|
| count  | 650940.0           | 650940.0           | 650940.0           | 650940  |
| unique |                    |                    |                    | 6       |
| top    |                    |                    |                    | walk    |
| freq   |                    |                    |                    | 359097  |
| mean   | 1227681185.6442146 | 39.65068313423152  | 115.4565844161574  |         |
| std    | 25192795.295363054 | 2.1629149883279783 | 13.665584780779312 |         |
| min    | 1176388703.0       | 18.2499            | -122.3307          |         |
| 25%    | 1215782864.75      | 39.92838           | 116.3211           |         |
| 50%    | 1222255172.0       | 39.97543           | 116.3368           |         |
| 75%    | 1229220877.75      | 39.9897272         | 116.4226           |         |
| max    | 1325343022.0       | 51.41032           | 126.9835           |         |

&nbsp;

Descriptive Statistics (by Variance): 


|       | Mean               |      Std.Dev |      Variance |
|-------|--------------------|--------------|---------------|
| time  | 1227681185.6442146 |  2.51928e+07 |   6.34677e+14 |
| lon   | 115.4565844161574  | 13.6656      | 186.748       |
| lat   | 39.65068313423152  |  2.16291     |   4.6782      |
| label | walk               |  1.15038     |   1.32337     |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 4346
Samples by Class:
| Label   |    # |
|---------|------|
| walk    | 2544 |
| taxibus |  791 |
| bike    |  433 |
| car     |  311 |
| subway  |  220 |
| train   |   47 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 1088
Samples by Class:
| Label   |   # |
|---------|-----|
| walk    | 636 |
| taxibus | 198 |
| bike    | 109 |
| car     |  78 |
| subway  |  55 |
| train   |  12 |

&nbsp;

