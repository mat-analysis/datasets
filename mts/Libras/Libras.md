1. Title: LIBRAS Movement Database

2. Sources:

     (a) Creators: 
		Daniel Baptista Dias (Dias, D.B.)
            Sarajane Marques Peres (Peres, S. M.)
		Helton Hideraldo B?scaro (B?scaro. H. H.)
        {danielbdias,heltonhb, sarajane} at usp.br

     (b) Donor: 
		University of S?o Paulo
		School of Art, Sciences and Humanities
		S?o Paulo, SP, Brazil
		http://each.uspnet.usp.br/each/
			
     (c) Date: November, 2008


3. Past Usage:

   1. DIAS, D. B.; MADEO, R. C. B.; ROCHA, T.; B?SCARO, H. H.; PERES, S. M.. Hand Movement Recognition for 
	  Brazilian Sign Language: A Study Using Distance-Based Neural Networks. In: 2009 International Joint 
	  Conference on Neural Networks, 2009, Atlanta, GA. Proceedings of 2009 International Joint Conference 
	  on Neural Networks. Eau Claire, WI, USA : Documation LLC, 2009. p. 697-704. 
	  Digital Object Identifier 10.1109/IJCNN.2009.5178917 


4. Relevant Information:

   --- LIBRAS, acronym of the Portuguese name "L?ngua BRAsileira de Sinais", is the oficial brazilian sign language.

   --- The dataset (movement_libras) contains 15 classes of 24 instances each, where each class references to a hand 
       movement type in LIBRAS. The hand movement is represented as a bidimensional curve performed by the hand in a 
       period of time. The curves were obtained from videos of hand movements, with the Libras performance from 4 
       different people, during 2 sessions. Each video corresponds to only one hand movement and has about $7$ seconds. 

   --- Each video corresponds to a function F in a functions space which is the continual version of the input dataset.

   --- In the video pre-processing, a time normalization is carried out selecting 45 frames from each video, in according 
       to an uniform distribution. In each frame, the centroid pixels of the segmented objects (the hand) are found, which 
       compose the discrete version of the curve F with 45 points. All curves are normalized in the unitary space.

   --- In order to prepare these movements to be analysed by algorithms, we have carried out a mapping operation, that is, 
       each curve F is mapped in a representation with 90 features, with representing the coordinates of movement. 

   --- Each instance represents 45 points on a bi-dimensional space, which can be plotted in an ordered way (from 1 through
       45 as the X co-ordinate) in order to draw the path of the movement.

5. Number of Instances: 360 (24 in each of fifteen classes)

6. Number of Attributes: 90 numeric (double) and 1 for the class (integer)

7. Attribute Information:
   1. 1? coordinate abcissa
   2. 1? coordinate ordinate
   3. 2? coordinate abcissa
   4. 2? coordinate ordinate
   ...
   89. 45? coordinate abcissa
   90. 45? coordinate ordinate
   91. class: 
		-- 1: curved swing
		-- 2: horizontal swing
		-- 3: vertical swing
		-- 4: anti-clockwise arc
		-- 5: clockwise arc
		-- 6: circle
		-- 7: horizontal straight-line
		-- 8: vertical straight-line
		-- 9: horizontal zigzag
		-- 10: vertical zigzag
		-- 11: horizontal wavy
		-- 12: vertical wavy
		-- 13: face-up curve
		-- 14: face-down curve 
		-- 15: tremble

8. Missing Attribute Values: None

9. Class Distribution: 6.66% for each of 15 classes.

10. Extra Information

(a)
	Applying a simple k-nearest neighbors algorithm (with Euclidean distance), it has been obtained the values below:

--- (%) perc of instance which have been correctly placed in a same group 
--- using the complete dataset: 24 instances per class, 15 classes

				    |	mean of correct | standard deviate | max of correct / class | min of correct / class
				    |	grouping (%)    |			     | grouping (%)		| grouping (%)
-------------------------------------------------------------------------------------------------------------------
      24-nearest neighbors  |	0.3918	    | 0.1267	     | 0.5556	/	5	| 0.2587	/	10
-------------------------------------------------------------------------------------------------------------------
neighbors in a ratio = 1.0  |	0.2245  	    |	0.0979	     | 0.3957	/	9	| 0.1181	/	 1
-------------------------------------------------------------------------------------------------------------------
neighbors in a ratio = 2.0  |	0.3514	    |	0.1210	     | 0.4514	/	9	| 0.2500	/	10
-------------------------------------------------------------------------------------------------------------------
neighbors in a ratio = 3.0  |	0.3848	    |	0.1266	     | 0.5347	/	5	| 0.2587	/	10
-------------------------------------------------------------------------------------------------------------------


(b) 
	In order to support the comparisons with the experiments of the paper cited in 3(3.1) (Past Usage),
we supply you the sub-datasets:

	1. movement_libras_1.data
	2. movement_libras_5.data
	3. movement_libras_8.data
	4. movement_libras_9.data
	5. movement_libras_10.data
