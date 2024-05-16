The data set we will use comes from a University of Kansas class exercise on the Hugoton and Panoma gas fields. For more on the origin of the data, see Dubois et al. (2007) and the Jupyter notebook that accompanies this tutorial at http://github.com/seg.
The data set consists of seven features (five wireline log measurements and two indicator variables) and a facies label at half-foot depth intervals. In machine learning terminology, the set of measurements at each depth interval comprises a feature vector, each of which is associated with a class (the facies type). We will use the pandas library to load the data into a dataframe, which provides a convenient data structure to work with well-log data.
The data set we will use comes from a University of Kansas class exercise on the Hugoton and Panoma gas fields. For more on the origin of the data, see Dubois et al. (2007) and the Jupyter notebook that accompanies this tutorial at http://github.com/seg.
The data set consists of seven features (five wireline log measurements and two indicator variables) and a facies label at half-foot depth intervals. In machine learning terminology, the set of measurements at each depth interval comprises a feature vector, each of which is associated with a class (the facies type). We will use the pandas library to load the data into a dataframe, which provides a convenient data structure to work with well-log data.

Facies	Description	Label	Adjacent facies
1	Nonmarine sandstone	SS	2
2	Nonmarine coarse siltstone	CSiS	1,3
3	Nonmarine fine siltstone	FSiS	2
4	Marine siltstone and shale	SiSh	5
5	Mudstone	MS	4,6
6	Wackestone	WS	5,7,8
7	Dolomite	D	6,8
8	Packstone-grainstone	PS	6,7,9
9	Phylloid-algal bafflestone	BS	7,8

Link: https://library.seg.org/doi/epub/10.1190/tle35100906.1
@article{doi:10.1190/tle35100906.1,
author = {Brendon Hall},
title = {Facies classification using machine learning},
journal = {The Leading Edge},
volume = {35},
number = {10},
pages = {906-909},
year = {2016},
doi = {10.1190/tle35100906.1},

URL = { 
        https://doi.org/10.1190/tle35100906.1
    
},
eprint = { 
        https://doi.org/10.1190/tle35100906.1
    
}
,
    abstract = { There has been much excitement recently about big data and the dire need for data scientists who possess the ability to extract meaning from it. Geoscientists, meanwhile, have been doing science with voluminous data for years, without needing to brag about how big it is. But now that large, complex data sets are widely available, there has been a proliferation of tools and techniques for analyzing them. Many free and open-source packages now exist that provide powerful additions to the geoscientist's toolbox, much of which used to be only available in proprietary (and expensive) software platforms. }
}