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

        self.iso_id = iso_id[:9]
        self.iso_num = float(iso_num)

        self.as_numbers()
        self.save_files()

    def as_numbers(self):
        self.as_list = []

        for i in refs: 
            if self.iso_id == i:
                self.as_list.append(i)

        self.as_num = len(self.as_list)

        return self.as_list, self.as_num

    def save_files(self):
        with  open('circ_host_as_nums.txt', 'a') as f:
            f.write("%s\t%d\n" % (self.iso_id, self.as_num))


try:
    os.remove("circ_host_as_nums.txt")
except:
    pass


#for individual exon length:

ref_file = "../workfiles/Arabidopsis_thaliana.TAIR10.34.genome_background.txt"
#ref_file = "test.txt"
ref_list = []
with open(ref_file) as inputfile:
    for line in inputfile:
        ref_list.append(line.strip().split('\t'))

refs = [item[0][:9] for item in ref_list]

print refs[:5]

circ_file = "../workfiles/merge_RnaseR_polyA_loose_forplots.saf"

circ_list = []
with open(circ_file) as inputfile:
    for line in inputfile:
        circ_list.append(line.strip().split('\t'))

# Dictionary will give the no. of exons/isoform.
ids=[item[0] for item in circ_list]

counts = dict()

transformtuple = tuple(ids)

for p in transformtuple:
   counts[p] = counts.get(p, 0) + 1

#print counts

for k,v in counts.items():
    iso_id = iso_set(k,v)
    print k,v
    print iso_id.__dict__
