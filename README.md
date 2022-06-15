# On Network Backbone Extraction for Modeling Online Collective Behavior
Carlos H. G. Ferreira, Fabricio Murai, Ana P. C. Silva, Martino Trevisan, Luca Vassio, Idilio Drago, Marco Mellia, and Jussara M. Almeida

Code and data for reproduction of the paper submitted to PloS ONE:

Pre-requisites: 
  - Python 3.6+ (TriBE, Noise Corrected, Disparity Filter, High Salient Skeleton, MLF, )
  - R (SDSM)
  - MatLab (Polya Urn)
  - Java (RECAST)
  - C (GloSS Filter)
  - Gephi (Toy Example Section 2)

As described in the paper, we have two case studies, which we will refer to here as Case Study 1 (Instagram) and Case Study 2 (WhatsApp). We then separate the data and codes from each of the two studies into folders. Each case study contains the notebooks and link to the data, separated by work step (backbone extraction, community detection, visualizations, etc.). Download these files and place them in the same folder as the notebooks. 

Finally, there is a folder called Toy Example that contains the data in Gephi format that corresponds to the views used in the work.

The backbone extraction methods and the implementation used (which must be downloaded from the original source) are described below. Please cite the original paper when using it:

Case Study 1 (Instagram): 

TriBE - Tripartide Backbone Extraction
  - Ferreira, Carlos HG, et al. "Unveiling community dynamics on      instagram political network." 12th ACM conference on web science. 2020.
  - Ferreira, Carlos HG, et al. "On the dynamics of political discussions on Instagram: A network perspective." Online Social Networks and Media 25 (2021): 100155.

Stochastic Degree Sequence Model (SDSM)
  - Neal, Z. P., Domagalski, R., & Sagan, B. (2021). Comparing alternatives to the fixed degree sequence model for extracting the backbone of bipartite projections.  Scientific Reports, 11, 23929. https://doi.org/10.1038/s41598-021-03238-3
  - Neal, Z. P. (2022). backbone: An R package to extract network backbones. PLoS ONE 17, e0269137. https://doi.org/10.1371/journal.pone.0269137
  - Link to download: Neal, Z. P. (2022). backbone: An R package to extract network backbones. PLoS ONE 17, e0269137. https://doi.org/10.1371/journal.pone.0269137

Noise Corrected:
  - Coscia, Michele, and Frank MH Neffke. "Network backboning with noisy data." 2017 IEEE 33rd International Conference on Data Engineering (ICDE). IEEE, 2017.
  - Link to download: https://www.michelecoscia.com/?page_id=287 

MLF:  
  - Unwinding the hairball graph: Pruning algorithms for weighted complex networks." Physical Review E 93.1 (2016): 012304
  - Link to download: Ask the author

GloSS Filter: 
  - Radicchi, Filippo, José J. Ramasco, and Santo Fortunato. "Information filtering in complex weighted networks." Physical Review E 83.4 (2011): 046101.
  - Link to downlaod: https://cgi.luddy.indiana.edu/~filiradi/resources.html

Case Study 2 (WhatsApp): 

Polya Urn Filter:
  - Marcaccioli, Riccardo, and Giacomo Livan. "A pólya urn approach to information filtering in complex networks." Nature communications 10.1 (2019): 1-10.
  - Link to download: https://www.mathworks.com/matlabcentral/fileexchange/69501-pf

Disparty Filter:
  - Serrano, M. Ángeles, Marián Boguná, and Alessandro Vespignani. "Extracting the multiscale backbone of complex weighted networks." Proceedings of the national academy of sciences 106.16 (2009): 6483-6488.
  - Link to download: https://www.michelecoscia.com/?page_id=287

RECAST:
  - Recast: Telling apart social and random relationships in dynamic networks." Performance Evaluation 87 (2015): 19-36.
  - Link to download: https://github.com/lab-csx-ufmg/RECAST/tree/master/RECAST

High Salient Skeleton (HSS):
  - Grady, Daniel, Christian Thiemann, and Dirk Brockmann. "Robust classification of salient links in complex networks." Nature communications 3.1 (2012): 1-10.
  - Link to download: https://www.michelecoscia.com/?page_id=287

Threshold: 
  - Just remove the edges according to a percentile

If you have any questions, please contact me at chgferreira@dcc.ufmg.br or chgferreira@ufop.edu.br
