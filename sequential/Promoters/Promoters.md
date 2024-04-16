##### Promoter Gene Sequences - Molecular Biology Data Set

E. Coli promoter gene sequences (DNA) with partial domain theory. 


Data Set Characteristics:  Sequential, Domain-Theory
Number of Instances: 106
Area: Life
Attribute Characteristics: Categorical
DNA sequence Size: 58
Missing Values? No
Type of domain: non-numeric, nominal (one of A, G, T, C)

Creators:
	1. promoter instances: C. Harley (CHARLEY '@' McMaster.CA) and R. Reynolds
	2. non-promoter instances and domain theory: M. Noordewier
	-- (non-promoters derived from work of lab of Prof. Tom Record, University of Wisconsin Biochemistry Department)


Note: DNA nucleotides can be grouped into a hierarchy, as shown below:

	X (any)
	/ \
	(purine) R Y (pyrimidine)
	/ \ / \
	A G T C


Here is that hierachy in a text-friendly format:

	X (any)
	. R (purine)
	. . A
	. . G
	. Y (pyrimidine)
	. . T
	. . C


Attribute Information:

1. One of {+/-}, indicating the class ("+" = promoter).
2. The instance name (non-promoters named by position in the 1500-long nucleotide sequence provided by T. Record).
3. The remaining 57 fields are the sequence, starting at position -50 (p-50) and ending at position +7 (p7). Each of these fields is filled by one of {a, g, t, c}.


Source: [UCI Molecular Biology (Promoter Gene Sequences)](https://archive.ics.uci.edu/ml/datasets/Molecular+Biology+%28Promoter+Gene+Sequences%29)
