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
        self.iso_num = float(iso_num)
        self.all_len = [int(x[3])-int(x[2]) for x in exonlen_list if x[0] == iso_id]
        self.av_len = [sum(self.all_len)/self.iso_num]

        self.save_files()

    def save_files(self):
        with  open('average_circ_intron_len_num.txt', 'a') as f:
            f.write("%s\t%.3f\t%.3f\n" % (self.iso_id, self.iso_num, self.av_len[0]))


try:
    os.remove("average_circ_intron_len_num.txt")
except:
    pass


#for individual exon length:

exonlen_file = "circ_intron.saf"

exonlen_list = []
with open(exonlen_file) as inputfile:
    for line in inputfile:
        exonlen_list.append(line.strip().split('\t'))

# Dictionary will give the no. of exons/isoform.
ids=[item[0] for item in exonlen_list]

counts = dict()

transformtuple = tuple(ids)

for p in transformtuple:
   counts[p] = counts.get(p, 0) + 1

#print counts

for k,v in counts.items():
    iso_id = iso_set(k,v)
    print k,v
    print iso_id.__dict__
