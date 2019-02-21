#!/usr/bin/python

import datetime
import operator
import math
import scipy
import numpy
from scipy import stats
from numpy import *
import os

now = datetime.datetime.now()

print now

class iso_set():

    def __init__(self,iso_id,iso_num):

        # Collect known informations for GTF based file.

        self.iso_id = iso_id
        self.all_len = [int(x[5])-int(x[4]) for x in exonlen_list if x[1] == iso_id]
        self.iso_num = float(iso_num)
        self.all_len = sum(self.all_len)
        self.av_len = [sum(self.all_len)/self.iso_num]

        self.save_files()

    def save_files(self):
        with  open('average_exp1_exon_len_num2.txt', 'a') as f:
            f.write("%s\t%d\t%d\t%.3f\n" % (self.iso_id,self.iso_num,self.all_len,self.av_len[0]))


try:
    os.remove("average_exp1_exon_len_num2.txt")
except:
    pass


#for individual exon length:

ref_file = "lariat_WT_TPM_1_vals.txt"
ref_list = []
with open(ref_file) as inputfile:
    for line in inputfile:
        ref_list.append(line.strip().split(' '))

# Dictionary will give the no. of exons/isoform.
pre_ids=[item[0] for item in ref_list]


exonlen_file = "../references/Arabidopsis_thaliana.TAIR10.34_isoform_exon_coordinates_det.txt"

exonlen_list = []
with open(exonlen_file) as inputfile:
    for line in inputfile:
        exonlen_list.append(line.strip().split('\t'))


ids=[item[1] for item in exonlen_list if item[1] in pre_ids]

counts = dict()

transformtuple = tuple(ids)

for p in transformtuple:
   counts[p] = counts.get(p, 0) + 1

#print counts

for k,v in counts.items():
    iso_id = iso_set(k,v)
    print k,v
    print iso_id.__dict__
