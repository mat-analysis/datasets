A starlight curve is a time series of brightness of a celestial
object as a function of time. The study of light curves in
astronomy is associated with the study of variability of
sources.

This is a dataset with 1,000 (purportedly) phase-aligned starlight
curves of length 1,024, whose class has been determined by an
expert.


Clustering of Star Light Curves is an important problem in
astronomy [20], as it can be a preprocessing step in outlier
detection [31]. We consider a dataset with 1,000 (purportedly)
phase-aligned light curves of length 1,024, whose class has been
determined by an expert [31]. Doing spectral clustering on this
data with DTW (R = 5%) takes about 23 minutes for all algorithms,
and averaged over 100 runs we find the Rand-Index is 0.62. While
this time may seem slow, recall that we must do 499,500 DTW
calculations with relatively long sequences. As we do not trust the
original claim of phase alignment, we further do rotation-invariant
DTW that dramatically increases Rand-Index to 0.76. Using SOTA,
this takes 16.57 days, but if we use the UCR suite, this time falls
by an order of magnitude, to just 1.47 days on a single core.
