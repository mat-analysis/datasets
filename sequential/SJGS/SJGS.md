##### Splice-junction Gene Sequences - Molecular Biology Data Set

Primate splice-junction gene sequences (DNA) with associated imperfect domain theory.

Splice junctions are points on a DNA sequence at which 'superfluous' DNA is removed during the process of protein creation in higher organisms. The problem posed in this dataset is to recognize, given a sequence of DNA, the boundaries between exons (the parts of the DNA sequence retained after splicing) and introns (the parts of the DNA sequence that are spliced out). This problem consists of two subtasks: recognizing exon/intron boundaries (referred to as EI sites), and recognizing intron/exon boundaries (IE sites). (In the biological community, IE borders are referred to a 'acceptors' while EI borders are referred to as 'donors'.)

This dataset has been developed to help evaluate a "hybrid" learning algorithm (KBANN) that uses examples to inductively refine preexisting knowledge. Using a "ten-fold cross-validation" methodology on 1000 examples randomly selected from the complete set of 3190, the following error rates were produced by various ML algorithms (all experiments run at the Univ. of Wisconsin, sometimes with local implementations of published algorithms).


	Data Set Characteristics:  Sequential, Domain-Theory
	Number of Instances: 3190
	Area: Life
	Attribute Characteristics: Categorical
	Sequence Size: 61
	Missing Values? No

Creators:

1. All examples taken from Genbank 64.1 (ftp site: genbank.bio.net)
2. Categories "ei" and "ie" include every "split-gene" for primates in Genbank 64.1
3. non-splice examples taken from sequences known not to include a splicing site

Attribute Information:

1. One of {n ei ie}, indicating the class.
2. The instance name.
3. The remaining 60 fields are the sequence, starting at position -30 and ending at position +30. Each of these fields is almost always filled by one of {a, g, t, c}. Other characters indicate ambiguity among the standard characters according to the following table:

Character: meaning

	D: A or G or T
	N: A or G or C or T
	S: C or G
	R: A or G

Source: [UCI Splice-junction Gene Sequences](http://archive.ics.uci.edu/ml/datasets/Molecular+Biology+%28Splice-junction+Gene+Sequences%29)