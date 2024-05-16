Source: California Department of Transportation, www.pems.dot.ca.gov
Creator: Marco Cuturi, Kyoto University, mcuturi '@' i.kyoto-u.ac.jp

Data Set Information:

15 months worth of daily data from the California Department of Transportation PEMS website. The data describes the occupancy
rate, between 0 and 1, of different car lanes of San Francisco bay area freeways. The measurements cover the period from Jan. 1st 2008 to Mar. 30th 2009 and are sampled every 10 minutes. We consider each day in this database as a single time series of dimension 963 (the number of sensors which functioned consistently throughout the studied period) and length 6 x 24=144. We remove public holidays from the dataset, as well
as two days with anomalies (March 8th 2009 and March 9th 2008) where all sensors were muted between 2:00 and 3:00 AM.
This results in a database of 440 time series.

The task is to classify each observed day as the correct day of the week, from Monday to Sunday, e.g. label it with an integer in {1,2,3,4,5,6,7}.
Each attribute describes the measurement of the occupancy rate (between 0 and 1) of a captor location as recorded by a measuring station, at a given timestamp in time during the day. The ID of each station is given in the stations_list text file. For more information on the location (GPS, Highway, Direction) of each station please refer to the PEMS website. There are 963 (stations) x 144 (timestamps) = 138.672 attributes for each record.

Relevant Papers:
[1] M. Cuturi, Fast Global Alignment Kernels, Proceedings of the Intern. Conference on Machine Learning 2011.
