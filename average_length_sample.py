#!/usr/bin/python

import datetime
import operator
import math
import scipy
from scipy import stats
from numpy import *
import os

now = datetime.datetime.now()

print now

class iso_set():

    def __init__(self,iso_id,exon_num):

        # Collect known informations for GTF based file.

        self.iso_id = iso_id
        self.exon_num = float(exon_num)
        self.exon_all_len = [int(x[3])-int(x[2]) for x in exonlen_list if x[0] == iso_id]
        self.exon_av_len = sum(self.exon_all_len)/self.exon_num
        self.exon_total_len = sum(self.exon_all_len) # for mature length

        self.intron_num = self.exon_num - 1
        self.intron_all_len = [int(x[3])-int(x[2]) for x in intronlen_list if x[0] == iso_id]
        self.intron_sum_len = sum(self.intron_all_len) # ?
        self.intron_av_len = sum(self.intron_all_len)/self.intron_num if self.intron_num > 0 else 0

        self.gene_id = self.iso_id[:9]
        self.chr = [x[1] for x in ref_list if x[0] == iso_id][0]
        self.start = [int(x[2]) for x in ref_list if x[0] == iso_id][0]
        self.end = [int(x[3]) for x in ref_list if x[0] == iso_id][0]
        self.ori = [x[5] for x in ref_list if x[0] == iso_id][0]
        self.note = str([x[6] for x in ref_list if x[0] == iso_id][0])
        self.sample = [x[4] for x in sample_list if x[0] == str(self.chr) and x[1] == str(self.start) and x[2] == str(self.end)]

        self.left_introns()
        self.right_introns()
        #self.printing()
        #self.save_files()

    def save_files(self):
        with  open('average_circ_intron_len_num_RnaseR_polyAmin.txt', 'a') as f:
            f.write("%s\t%.3f\t%d\t%.3f\n" % (self.iso_id, self.iso_num,self.sum_len[0],self.av_len[0]))


    def left_introns(self):

        self.left_flag = None
        self.upstream = None
        self.downstream = None
        self.up_start = None
        self.up_end = None
        self.down_start = None
        self.down_end = None

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
        
        if self.ori == "+":
            self.upstream = self.left_len
            self.up_start = self.left_i_start
            self.up_end = self.left_i_end
        if self.ori == "-":
            self.downstream = self.left_len
            self.down_start = self.left_i_end
            self.down_end = self.left_i_start

        return self.left_i_start, self.left_i_end, self.left_flag, self.left_len, self.upstream, self.downstream, self.up_start, self.up_end, self.down_start, self.down_end


    def right_introns(self):

        self.right_flag = None

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

        if self.ori == "-" and self.upstream == None:
            self.upstream = self.right_len
            self.up_start = self.right_i_end
            self.up_end = self.right_i_start

        if self.ori == "+" and self.downstream == None:
            self.downstream = self.right_len
            self.down_start = self.right_i_start
            self.down_end = self.right_i_end

        return self.right_i_start, self.right_i_end, self.right_flag, self.right_len, self.upstream, self.downstream, self.up_start, self.up_end, self.down_start, self.down_end

try:
    os.remove("average_circ_feature_len_num_RnaseR_polyAmin_sum.txt")
except:
    pass

#try:
#    os.remove("average_circ_feature_anchor_intron_coord.txt")
#except:
#    pass

## need reference file: merge_RnaseR_polyA_loose_forplots.txt
## need coordiates from ref and also from exon saf
## need sample info from bigfile

ref_file = "merge_RnaseR_polyA_loose_forplots.txt"
#ref_file = "test.txt"
ref_list = []
with open(ref_file) as inputfile:
    for line in inputfile:
        ref_list.append(line.strip().split('\t'))

sample_file = "ciri2_big_coord5.txt"
sample_list = []
with open(sample_file) as inputfile:
    for line in inputfile:
        sample_list.append(line.strip().split('\t'))

exonlen_file = "merge_RnaseR_polyA_loose_forplots.saf"

exonlen_list = []
with open(exonlen_file) as inputfile:
    for line in inputfile:
        exonlen_list.append(line.strip().split('\t'))

intronlen_file = "circ_intron_RnaseR_polyAmin.saf"

intronlen_list = []
with open(intronlen_file) as inputfile:
    for line in inputfile:
        intronlen_list.append(line.strip().split('\t'))

intron_file = "Arabidopsis_thaliana.TAIR10.34_isoform_intron_unique.saf"
intron_list = []
with open(intron_file) as inputfile:
    for line in inputfile:
        intron_list.append(line.strip().split('\t'))

intron_id =[item[0] for item in intron_list]
intron_chr =[item[1] for item in intron_list]
intron_start =[int(item[2]) for item in intron_list]
intron_end =[int(item[3]) for item in intron_list]

# Dictionary will give the no. of exons/isoform.
ids=[item[0] for item in exonlen_list]

counts = dict()

transformtuple = tuple(ids)

for p in transformtuple:
   counts[p] = counts.get(p, 0) + 1

out_file = open("average_circ_feature_len_num_RnaseR_polyAmin_sum.txt", "w")

out_file.write("ID\tSample\tChr\tStart\tEnd\tOri\tNote\tMature_len\tExon_num\tAv_exon_len\tIntron_num\tAv_intron_len\tUpstream\tDownstream\tLeft\tRight\n")

#out_file2 = open("average_circ_feature_anchor_intron_coord.txt", "w")


for k,v in counts.items():
    iso_id = iso_set(k,v)

    out_file.write("%s\t%s\t%s\t%d\t%d\t%s\t%s\t%d\t%d\t%.3f\t%d\t%.3f\t%d\t%d\t%s\t%s\n" % (iso_id.iso_id, iso_id.sample, iso_id.chr, iso_id.start, iso_id.end, iso_id.ori, iso_id.note, iso_id.exon_total_len,iso_id.exon_num, iso_id.exon_av_len, iso_id.intron_num, iso_id.intron_av_len, iso_id.upstream, iso_id.downstream, iso_id.left_flag, iso_id.right_flag))



    for i in iso_id.sample:
        print i, iso_id.gene_id
        #print iso_id.iso_id, i, iso_id.chr, iso_id.start, iso_id.end, iso_id.ori, iso_id.note,iso_id.exon_total_len, iso_id.exon_num, iso_id.exon_av_len, iso_id.intron_num, iso_id.intron_av_len, iso_id.upstream, iso_id.left_flag, iso_id.downstream, iso_id.right_flag

        #out_file.write("%s\t%s\t%s\t%d\t%d\t%s\t%s\t%d\t%d\t%.3f\t%d\t%.3f\t%d\t%d\t%s\t%s\n" % (iso_id.iso_id, i, iso_id.chr, iso_id.start, iso_id.end, iso_id.ori, iso_id.note, iso_id.exon_total_len,iso_id.exon_num, iso_id.exon_av_len, iso_id.intron_num, iso_id.intron_av_len, iso_id.upstream, iso_id.downstream, iso_id.left_flag, iso_id.right_flag))

        #print iso_id.chr, iso_id.left_i_start, iso_id.left_i_end, i, iso_id.ori
        #print iso_id.chr, iso_id.right_i_start, iso_id.right_i_end, i, iso_id.ori

        #out_file2.write("%s:%d-%d\t%s\t%s\tleft\n" % (iso_id.chr, iso_id.left_i_start, iso_id.left_i_end, i, iso_id.ori))

        #out_file2.write("%s:%d-%d\t%s\t%s\tright\n" % (iso_id.chr, iso_id.right_i_start, iso_id.right_i_end, i, iso_id.ori))
out_file.close()
#out_file.close2()
