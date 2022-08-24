#!/usr/bin/env python3

from dateutil import rrule
from datetime import date, datetime, timedelta
import itertools
from ast import literal_eval
import networkx as nx
import warnings
warnings.filterwarnings('ignore')
from sklearn import preprocessing
import pandas as pd
import gzip
import json 
import numpy as np
from ast import literal_eval
from sklearn.metrics.cluster import normalized_mutual_info_score
import random
import copy 
import pdb
import scipy
from collections import Counter
import pickle
from scipy.special import logsumexp
from tqdm import tnrange, tqdm_notebook
import matplotlib.pyplot as plt
import os.path
import pickle as pkl
from tqdm import tqdm
from tqdm import trange
from scipy.stats import ks_2samp
from multiprocessing import Pool #  Process pool
from multiprocessing import sharedctypes
from tqdm import *
import math

def get_node2id(influencer2data):
    set_commenters_all = set()
    for influencer in influencer2data.keys():
        for post, commenters in influencer2data[influencer].items():
            set_commenters_all.update(commenters)       
    set_commenters_all = sorted(set_commenters_all)        
    commenter2id_all = dict(zip(set_commenters_all, range(len(set_commenters_all))))
    return commenter2id_all



def ncr(n, r):
    import operator as op
    from functools import reduce
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def get_memory():
    import psutil
    return round(psutil.virtual_memory().used / (1024.0 ** 3),1)

def graph_to_backbone_tribe(influencer2data_parameter, percentile_parameter, PATH_File):
 
    global commenter2id_all
    global percentile
    global influencer2data
    global shared_array
    global dict_post2ncomments
    global dict_post2ncomments_total
    percentile = percentile_parameter
    influencer2data = influencer2data_parameter
    del influencer2data_parameter
    global influencer2commmenters
    global commenter2ncomments
    
   
    print("Pre-Computing data")
    
    with open(PATH_File+'-Log.txt', 'a+') as log:
        log.write(str(datetime.now()) +" - Pre-Computing data\n")
     
    
    set_commenters_all = set()
    dict_post2ncomments = {}
    dict_post2ncomments_total = {}
    for influencer in influencer2data.keys():
        dict_post2ncomments[influencer] = []
        dict_post2ncomments_total[influencer] = {}
        for post, commenters in influencer2data[influencer].items():
            set_commenters_all.update(commenters)       
            dict_post2ncomments[influencer].append(len(commenters))
        dict_post2ncomments_total[influencer] = np.sum(dict_post2ncomments[influencer])

       
    set_commenters_all = sorted(set_commenters_all)        
    commenter2id_all = dict(zip(set_commenters_all, range(len(set_commenters_all))))
    n = len(commenter2id_all)
    with open(PATH_File+'-Log.txt', 'a+') as log:
        log.write(str(datetime.now()) +" - Allocating the Adjacency Matrix"+'\n')
        
    m_final = np.empty((n, n), dtype=np.uint8)
    m_final[:] = 0
    

    influencer2commmenters = {}
    dict_influenecer_commenter_unique = {}
    commenter2ncomments = {}
    set_edges_considered_temp = set()
    total_edges = 0
    with open(PATH_File+'-Log.txt', 'a+') as log:
        log.write(str(datetime.now()) +' - Consuming: ' + str(get_memory()) + " GB.\n")
        log.write(str(datetime.now()) +" - Computing Co-apperance values"+'\n')  
    
    dict_co_appearance = {}
    compute_coapperance_matrix = True 
    
    if(os.path.exists(PATH_File+'-co-appearance.pkl')):
        compute_coapperance_matrix = True 
        with open(PATH_File+'-Log.txt', 'a+') as log:
            log.write(str(datetime.now()) +" - Co-apperance matrix.pkl already exists"+'\n')
    else:
        with open(PATH_File+'-Log.txt', 'a+') as log:
            log.write(str(datetime.now()) +' - Consuming: ' + str(get_memory()) + " GB.\n")
            log.write(str(datetime.now()) +" - Computing Co-apperance values"+'\n') 
       
   
    for influencer in influencer2data.keys(): 
        print(influencer, len(influencer2data[influencer]))
        with open(PATH_File+'-Log.txt', 'a+') as log:
            log.write("\t - "+ str(influencer) +" - "+ str(len(influencer2data[influencer]))+'\n')
        list_commenters_influencer = []
        influencer2commmenters[influencer] = {}
        commenter2ncomments[influencer] = {}
        dict_influenecer_commenter_unique[influencer] = set()
    
        for post, commenters in influencer2data[influencer].items():
            list_comment_post = []
            for c in commenters:
                list_commenters_influencer.append(commenter2id_all[c])
                list_comment_post.append(commenter2id_all[c])
            if (compute_coapperance_matrix):    
                for edge in itertools.combinations(sorted(list_comment_post), 2):
                    m_final[edge[0], edge[1]] += 1            
        counter_commenter = Counter(list_commenters_influencer)
        for commenter, ncomments in counter_commenter.items():
            if commenter not in influencer2commmenters[influencer]:
                influencer2commmenters[influencer][commenter] = {}
            commenter2ncomments[influencer][commenter] = ncomments

    total_relative = 0
    if (True): 
        with open(PATH_File+'-Log.txt', 'a+') as log:
            log.write(str(datetime.now()) +" - Saving Co-apperance values"+'\n')  

        print("Saving the analytic null model data... Co-appearance")
        pkl.dump(m_final, open(PATH_File+'-co-appearance.pkl', "wb"), protocol=4)
        m_final[:] = 0
    
    with open(PATH_File+'-Log.txt', 'a+') as log:
        log.write(str(datetime.now()) +" - Creating Shared Array"+'\n')  
    
    print("Starting the parallel computing")
    
    with open(PATH_File+'-Log.txt', 'a+') as log:
        log.write(str(datetime.now()) +' - Consuming: ' + str(get_memory()) + " GB.\n")
        log.write(str(datetime.now()) +" - Starting Parallel Computing"+'\n')   
        
   
    proc = Pool()   
    
    index = 0
    with open(PATH_File+'-Log.txt', 'a+') as log:
        log.write(str(datetime.now()) +" - Percentage Completed: 0 \n") 
        max_ = int(ncr(len(m_final), 2))
        percentage = int(0.05*max_)
        for u, v, final_exp_coappearances, final_limiar_rna in tqdm(proc.imap_unordered(compute_poisson_binomial_paralell, 
        itertools.combinations(range(0,len(m_final)), 2), chunksize=100), position= 0, leave=False, total=int(max_)):          
            index += 1
            if final_exp_coappearances != 0:
                m_final[u, v] = final_exp_coappearances
                m_final[v, u] = final_limiar_rna
        
    return m_final 

def compute_poisson_binomial_paralell(edge):    
    u = edge[0]
    v = edge[1]
    P_appear_final_u = np.array([])
    P_appear_final_v = np.array([])

    flag = False
    final_exp_coappearances = 0
    final_limiar_rna = 0
    
    for influencer, list_posts in influencer2data.items():
        if (u in influencer2commmenters[influencer]) & (v in influencer2commmenters[influencer]):
            flag = True
                        
            n_comments_u = commenter2ncomments[influencer][u]
            n_comments_v = commenter2ncomments[influencer][v]
                        
            total_n_comments = dict_post2ncomments_total[influencer]
                        
            # compute p_choose
            p_choose_u = n_comments_u/total_n_comments
            p_choose_v = n_comments_v/total_n_comments
                                
            # compute matriz P_appear where entry [c,p] is the prob that c appears on post p

            post2ncomments = dict_post2ncomments[influencer]
            P_appear_u = (1 - (1-p_choose_u) ** post2ncomments)
            P_appear_v = (1 - (1-p_choose_v) ** post2ncomments)
            
            P_appear_u = P_appear_u
            P_appear_v = P_appear_v

            
            exp_coappearances = P_appear_u @ P_appear_v.T 
            P_appear_final_u = np.append(P_appear_final_u, P_appear_u)
            P_appear_final_v = np.append(P_appear_final_v, P_appear_v)


            final_exp_coappearances += exp_coappearances
        
    pb_co_appearance_final = np.multiply(P_appear_final_u, P_appear_final_v)
    

    if flag == True:

        cdf_rna_alg = poibin_normal_aproximation(pb_co_appearance_final)
        for i in range(0, len(cdf_rna_alg)+1, 1):  
            if cdf_rna_alg[i] > percentile:
                final_limiar_rna = i
                break

        del P_appear_final_u
        del P_appear_final_v
        del P_appear_u
        del P_appear_v
        
        return u, v, final_exp_coappearances, final_limiar_rna
       
    else:
        return u,v, 0, 0



def compute_edges_pruned(edge):
    edge = edge.split(" ")
    i = int(edge[0])
    j = int(edge[1])
    w = int(edge[2])
    null_model
    threshold
    #print(null_model[i][j], w)
    if (w >= null_model[j][i] and null_model[j][i] > 0 and w > threshold):
        return True, (i, j, w)
    else:
        return False, (i,j, w)
    
def compute_edges(edge):
    i = edge[0]
    j = edge[1]
  
    if (m_coappearance[i][j] > 0):
        return True, (i,j, m_coappearance[i][j])
    else:
        return False, (i,j, m_coappearance[i][j])
    
    
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

################################
def poibin_normal_aproximation(pp): 
    pp = np.array(pp)
    from scipy.stats import norm
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    #https://cran.r-project.org/web/packages/poibin/poibin.pdf
    #kk The values where the cdf or pmf to be evaluated.
    #pp The vector for pj ’s which are the sucess probabilities for indicators
    kk = np.array(range(1, len(pp)+1))
    muk = sum(pp)
    sigmak = np.sqrt(sum(pp*(1-pp)))
    
    part1 = pp*(1-pp)
    part2 = 1-(2*pp)
    
    gammak = sum(part1*part2)   
    kk1=(kk+.5-muk)/sigmak
    vkk = norm.cdf(kk1)+gammak/(6*pow(sigmak,3))*(1-pow(kk1,2))*(norm.pdf(kk1))
    # Avoid precision error < 0 and >1
    vkk[vkk < 0] = 0
    vkk[vkk > 1] = 1
    vkk = np.insert(vkk, 0, 0)
    return vkk



