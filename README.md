## On Network Backbone Extraction for Modeling Online Collective Behavior

This repository includes the code for reproducing the results in the paper: *On Network Backbone Extraction for Modeling Online Collective Behavior* by Carlos H. G. Ferreira, Fabricio Murai, Ana P. C. Silva, Martino Trevisan, Luca Vassio, Idilio Drago, Marco Mellia, and Jussara M. Almeida. In te following, the instructions to execute our code and replicate the results.

## Note well: 

Results presented in the paper are obtained using two large datasets that are linked below. Given the size of these datasets, a machine with large amount of memory is needed to run some sets of the analysis.

All results have been obtained using a Linux server with 120 GB RAM and 60 CPU cores, even if most algorithms and post-processing steps can still be run on an ordinary laptop. 

Instead of re-implementing the tested backbone extraction algorithms, we rely on the source code provided by the original authors of each method to precisely reproduce their results. As such, the multiple backbone extraction methods are built using different programming languages and environments. We provide links to the websites from where source codes can be downloaded. Whenever possible, we provide scripts in the form of Jupyter notebooks to automate the download and execution of such external code. 

Notice however that some authors have provided us their source code without permissions for redistributing it. Moreover, some methods are implemented using proprietary tools (e.g., Matlab). For those cases we provide generic instructions on how to reproduce our results, together with pointers to help interested readers obtain the missing sources. 

Finally, we provide also the backbones extracted using all third-party algorithms. These files can be loaded directly in our jupyter notebooks to reproduce the downstream analysis presented in our paper.

## Pre-requisites:

All methods have been tested under Linux/Ubuntu, but they can run on different platforms as well. The main requirements per method are:

  - Python 3.6+ (TriBE, Noise Corrected, Disparity Filter, High Salient Skeleton, MLF)
  - R (SDSM)
  - MatLab (Polya Urn)
  - Java (RECAST)
  - C (GloSS Filter)
  - Gephi (Toy Example Section 2)

As described in the paper, we have two case studies, which we will refer to here as Case Study 1 (Instagram) and Case Study 2 (WhatsApp). We separate the data and our scripts for each case study into folders. Each case study contains the notebooks with links to the data, separated by work step (backbone extraction, community detection, visualization, etc). Download the dataset files and place them in the same folder as the notebooks. For this step, see the next section.

Finally, there is a folder called Toy Example that contains the data in Gephi format that corresponds to illustration shown in the paper.

As explained above, the backbone extraction algorithms are downloaded from the original sources. We thank all the researchers who provided us their implementation and source code, allowing such an external comparison and validation of their work. 

*For recognizing their effort, please cite the original papers when using the methods.*

## Dataset and code

Our scripts can be found in the sub directories of this repository.
It is in the form of Jupyter notebooks, that you must execute to reproduce our results.

The datasets are large, for the Instagram use case especially (210 GB uncompressed). Thus, they must be downloaded from a separate repository.
[Here](https://mplanestore.polito.it:5001/sharing/8MfeM2iWw) the link to download the datasets. We provide both the raw traces, as well as pre-processed files, e.g., the backbones extracted by each method.

## Case Study 1 (Instagram):

The code for the Instagram case study is into the `CS1 - Instagram` folder. Details on the algorithms we tested can be found in the papers below.

TriBE - Tripartide Backbone Extraction
  - Ferreira, Carlos HG, et al. "Unveiling community dynamics on      instagram political network." 12th ACM conference on web science. 2020. https://dl.acm.org/doi/fullHtml/10.1145/3394231.3397913
  - Ferreira, Carlos HG, et al. "On the dynamics of political discussions on Instagram: A network perspective." Online Social Networks and Media 25 (2021): 100155. https://www.sciencedirect.com/science/article/abs/pii/S2468696421000379
  - The jupyter notebooks in this repository include the source code of TriBe.

Stochastic Degree Sequence Model (SDSM)
  - Neal, Z. P., Domagalski, R., & Sagan, B. (2021). Comparing alternatives to the fixed degree sequence model for extracting the backbone of bipartite projections.  Scientific Reports, 11, 23929. https://doi.org/10.1038/s41598-021-03238-3
  - Neal, Z. P. (2022). backbone: An R package to extract network backbones. PLoS ONE 17, e0269137. https://doi.org/10.1371/journal.pone.0269137
  - Link to download: Neal, Z. P. (2022). backbone: An R package to extract network backbones. PLoS ONE 17, e0269137. https://doi.org/10.1371/journal.pone.0269137

Noise Corrected:
  - Coscia, Michele, and Frank MH Neffke. "Network backboning with noisy data." 2017 IEEE 33rd International Conference on Data Engineering (ICDE). IEEE, 2017.
  - Link to download: https://www.michelecoscia.com/?page_id=287 

MLF:  
  - Dianati, Navid. "Unwinding the hairball graph: Pruning algorithms for weighted complex networks." Physical Review E 93.1 (2016): 012304.
  - Please contact the authors directly to obtain their source code.

GloSS Filter: 
  - Radicchi, Filippo, José J. Ramasco, and Santo Fortunato. "Information filtering in complex weighted networks." Physical Review E 83.4 (2011): 046101.
  - Link to downlaod: https://cgi.luddy.indiana.edu/~filiradi/resources.html

## Case Study 2 (WhatsApp):

The code for the Whatsapp case study is into the `CS2 - Whatsapp` folder. Details on the algorithms we tested can be found in the papers below.

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
  - This method is trivial: It is enough to set a threshold for the edge weights. Our scripts include this procedure.

If you have any questions, please contact the authors at chgferreira@dcc.ufmg.br or chgferreira@ufop.edu.br
