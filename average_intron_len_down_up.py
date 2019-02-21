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

    def __init__(self,iso_id):

        # Collect known informations for GTF based file.

        self.iso_id = iso_id
        self.gene_id = self.iso_id[:9]
        self.chr = [x[2] for x in ref_list if x[1] == iso_id][0]
        self.start = [int(x[3]) for x in ref_list if x[1] == iso_id][0]
        self.end = [int(x[4]) for x in ref_list if x[1] == iso_id][0]
        self.ori = [x[5] for x in ref_list if x[1] == iso_id][0]
        self.note = [x[7] for x in ref_list if x[1] == iso_id]

        self.left_introns()
        self.right_introns()
        self.printing()  
        self.save_files()

    def left_introns(self):

        self.left_flag = None

        for i in xrange(0, len(intron_list)):
   
            self.left_flag = None

            if self.chr == intron_chr[i] and self.gene_id == intron_id[i] and self.start-1 == intron_end[i]:

               self.left_i_start = intron_start[i]
               self.left_i_end = intron_end[i]
               self.left_flag = "Normal"
               break

            elif self.chr == intron_chr[i] and self.gene_id == intron_id[i] and self.start-1 != intron_end[i] and self.start > intron_end[i] and self.start < intron_start[i+1]:

                self.left_i_start = intron_start[i]
                self.left_i_end = self.start-1
                self.left_flag = "In_the_exon"
                break

            else:
               self.left_i_start = 0
               self.left_i_end = 0
               self.left_flag = "No_intron!"
         
        self.left_len = self.left_i_end - self.left_i_start

        return self.left_i_start, self.left_i_end, self.left_flag, self.left_len


    def right_introns(self):

        for i in xrange(0, len(intron_list)):

            self.right_flag = None

            if self.chr == intron_chr[i] and self.gene_id == intron_id[i] and self.end+1 == intron_start[i]:
                self.right_i_start = intron_start[i]
                self.right_i_end = intron_end[i]
                self.right_flag = "Normal"
                break

            elif self.chr == intron_chr[i] and self.gene_id == intron_id[i] and self.end+1 != intron_start[i] and self.end > intron_end[i-1] and self.end < intron_start[i]:
                self.right_i_start = self.end+1
                self.right_i_end = intron_end[i]
                self.right_flag = "In_the_exon"
                break

            else:
               self.right_i_start = 0
               self.right_i_end = 0
               self.right_flag = "No_intron!"

        self.right_len = self.right_i_end - self.right_i_start

        return self.right_i_start, self.right_i_end, self.right_flag, self.right_len


    def save_files(self):
       if self.ori == "+":
           with  open('circ_down_up_intron_len.txt', 'a') as f:
               f.write("%s\t%d\t%d\n" % (self.iso_id, self.left_len, self.right_len))

       if self.ori == "-":
           with  open('circ_down_up_intron_len.txt', 'a') as f:
               f.write("%s\t%d\t%d\n" % (self.iso_id, self.right_len, self.left_len))


    def printing(self):
       if self.ori == "+":
           print self.ori, self.iso_id, self.start, self.end, self.left_flag, self.left_i_start, self.left_i_end, self.right_flag, self.right_i_start, self.right_i_end, self.left_len, self.right_len

       if self.ori == "-":
           print self.ori, self.iso_id, self.start, self.end, self.right_flag, self.right_i_start, self.right_i_end, self.left_flag, self.left_i_start, self.left_i_end, self.right_len, self.left_len
try:
    os.remove("circ_down_up_intron_len.txt")
except:
    pass

ref_file = "ciri2.03_circ_exonnum_man2.txt"
#ref_file = "test.txt"
ref_list = []
with open(ref_file) as inputfile:
    for line in inputfile:
        ref_list.append(line.strip().split('\t'))

# Dictionary will give the no. of exons/isoform.
ids=[item[1] for item in ref_list]

#for individual exon length:

intron_file = "Arabidopsis_thaliana.TAIR10.34_isoform_intron.saf"
intron_list = []
with open(intron_file) as inputfile:
    for line in inputfile:
        intron_list.append(line.strip().split('\t'))

intron_id =[item[0][:9] for item in intron_list]
intron_chr =[item[1] for item in intron_list]
intron_start =[int(item[2]) for item in intron_list]
intron_end =[int(item[3]) for item in intron_list]

print intron_id[:5],  intron_chr[:5],  intron_start[:5],  intron_end[:5]

counts = dict()

transformtuple = tuple(ids)

for p in transformtuple:
   counts[p] = counts.get(p, 0) + 1

#print counts

for k,v in counts.items():
    iso_id = iso_set(k)
#    print k,v
#    print iso_id.__dict__
