taken from the UCI data set

Ben H Williams 
School of Informatics, 
University of Edinburgh, 
ben.williams '@' ed.ac.uk 


Data Set Information:

The characters here were used for a PhD study on primitive extraction using HMM based models. The data consists of 2858 character samples, The data was 
captured using a WACOM tablet. 3 Dimensions were kept - x, y, and pen tip force. The data has been numerically differentiated and Gaussian smoothed, 
with a sigma value of 2. Data was captured at 200Hz. The data was normalised. Only characters with a single 'PEN-DOWN' segment were considered. 
Character segmentation was performed using a pen tip force cut-off point. The characters have also been shifted so that their velocity profiles best 
match the mean of the set.


Each instance is a 3-dimensional pen tip velocity trajectory. The original data has different length cases. The class label is one of 20 characters
'a'    'b'    'c'    'd'    'e'    'g'    'h'    'l'    'm'    'n'    'o'    'p'

  'q'    'r'    's'    'u'    'v'    'w'    'y'    'z'
To conform with the repository, we have truncated all series to the length of the shortest, which is 182, which will no doubt make classification harder. 




Relevant Papers:

B.H. Williams, M.Toussaint, and A.J. Storkey. Extracting motion primitives from natural handwriting data. In ICANN, volume 2, pages 634�643, 2006. 

B.H. Williams, M.Toussaint, and A.J. Storkey. A primitive based generative model to infer timing information in unpartitioned handwriting data. In IJCAI, pages 1119�1124, 2007. 

B.H. Williams, M. Toussaint, and A.J. Storkey. Modelling motion primitives and their timing in biologically executed movements. In J.C. Platt, D. Koller, Y. Singer, and S. Roweis, editors, Advances in Neural Information Processing Systems 20, pages 1609�1616. MIT Press, Cambridge, MA, 2008. 

