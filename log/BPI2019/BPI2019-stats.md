##### Descriptive Statistics for BPI2019/run1

&nbsp;

|       |   Number of Classes |   Number of Attributes |         Avg Size of Trajs |   Number of Trajs | Hold-out   |   Number of Points |   Longest Size |   Shortest Size |
|-------|---------------------|------------------------|---------------------------|-------------------|------------|--------------------|----------------|-----------------|
| Total | 2                   | 6                      | 6.34 / ±983.6602802958679 | 251734            | 100%       |            1595923 |            990 |               1 |
| Train | -                   | -                      | -                         | 201386            | 80.00%     |            1276896 |            990 |               1 |
| Test  | -                   | -                      | -                         | 50348             | 20.00%     |             319027 |            833 |               1 |

&nbsp;

###### Attributes: User, PurchaseEvent, CumulativeNetWorth, timestamp, tid, label

###### MAT Attributes: 'SpendAreaText', 'Company',  'DocumentType',  'SubSpendAreaText',  'PurchasingDocument',  'PurchDocCategory',  'VendorID',  'ItemType',  'ItemCategory',  'SpendClassification',  'Source',  'VendorName',  'GRBasedInvoice',  'ItemID',  'GoodsReceipt',  'traceDuration',  'duration',

&nbsp;


###### Labels: low, high

&nbsp;

|        | User    | PurchaseEvent        | CumulativeNetWorth   | timestamp          | label   |
|--------|---------|----------------------|----------------------|--------------------|---------|
| count  | 1595923 | 1595923              | 1595923.0            | 1595923.0          | 1595923 |
| unique | 628     | 42                   |                      |                    | 2       |
| top    | NONE    | Record Goods Receipt |                      |                    | low     |
| freq   | 399090  | 314097               |                      |                    | 1580216 |
| mean   |         |                      | 17888.974151635135   | 1531532341.7240682 |         |
| std    |         |                      | 222772.3383659214    | 10859949.33021026  |         |
| min    |         |                      | 0.0                  | -692067660.0       |         |
| 25%    |         |                      | 145.0                | 1524175140.0       |         |
| 50%    |         |                      | 536.0                | 1531473420.0       |         |
| 75%    |         |                      | 2481.0               | 1538982120.0       |         |
| max    |         |                      | 28994530.0           | 1586469540.0       |         |

&nbsp;

Descriptive Statistics (by Variance): 


|                    | Mean                   |          Std.Dev |        Variance |
|--------------------|------------------------|------------------|-----------------|
| timestamp          | 1531532341.7240682     |      1.08599e+07 |     1.17938e+14 |
| CumulativeNetWorth | 17888.974151635135     | 222772           |     4.96275e+10 |
| User               | user_015               |    102.643       | 10535.7         |
| PurchaseEvent      | Record Invoice Receipt |      5.93993     |    35.2828      |
| label              | low                    |      0.0987172   |     0.00974509  |

&nbsp;

###### Labels for TRAIN:


Number of Samples: 201386
Samples by Class:

| Label   |      # |
|---------|--------|
| low     | 201226 |
| high    |    160 |

&nbsp;

###### Labels for TEST.:


Number of Samples: 50348
Samples by Class:

| Label   |     # |
|---------|-------|
| low     | 50307 |
| high    |    41 |