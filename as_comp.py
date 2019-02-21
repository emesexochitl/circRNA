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
        self.as_event = [x[1] for x in as_list if x[0] == self.gene_id]

        #self.save_files()

    def save_files(self):
        with  open('circ_as_events.txt', 'a') as f:
            f.write("%s\t%s\n" % (self.iso_id, self.as_event))


#try:
#    os.remove("circ_as_events.txt")
#except:
#    pass


exonlen_file = "merge_RnaseR_polyA_loose_forplots.txt"

exonlen_list = []
with open(exonlen_file) as inputfile:
    for line in inputfile:
        exonlen_list.append(line.strip().split('\t'))

ids=[item[0] for item in exonlen_list]

as_file = "arabidopsis_as.txt"

as_list = []
with open(as_file) as inputfile:
    for line in inputfile:
        as_list.append(line.strip().split('\t'))

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n12 = 0
n13 = 0
n14 = 0
n15 = 0
n23 = 0
n24 = 0
n25 = 0
n34 = 0
n35 = 0
n45 = 0
n123 = 0
n124 = 0
n125 = 0
n134 = 0
n135 = 0
n145 = 0
n234 = 0
n235 = 0
n245 = 0
n345 = 0
n1234 = 0
n1235 = 0
n1245 = 0
n1345 = 0
n2345 = 0
n12345 = 0


for i in ids:
    iso_id = iso_set(i)
    
    hitlist = iso_id.as_event
    print hitlist
    if hitlist == ['AltA,AltD,AltP,ExonS,IntronR']:
        n12345 = n12345 +1

    if hitlist == ['AltA']:
        n1 = n1 +1

    if hitlist == ['AltD']:
        n2 = n2 +1

    if hitlist == ['AltP']:
        n3 = n3 +1

    if hitlist == ['ExonS']:
        n4 = n4 +1

    if hitlist == ['IntronR']:
        n5 = n5 +1

    if hitlist == ['AltA,AltD']:
        n12 = n12 +1

    if hitlist == ['AltA,AltP']:
        n13 = n13 +1

    if hitlist == ['AltA,ExonS']:
        n14 = n14 +1

    if hitlist == ['AltA,IntronR']:
        n15 = n15 +1

    if hitlist == ['AltD,AltP']:
        n23 = n23 +1

    if hitlist == ['AltD,ExonS']:
        n24 = n24 +1

    if hitlist == ['AltD,IntronR']:
        n25 = n25 +1

    if hitlist == ['AltP,ExonS']:
        n34 = n34 +1

    if hitlist == ['AltP,IntronR']:
        n35 = n35 +1

    if hitlist == ['ExonS,IntronR']:
        n45 = n45 +1

    if hitlist == ['AltA,AltD,AltP']:
        n123 = n123 +1

    if hitlist == ['AltA,AltD,ExonS']:
        n124 = n124 +1

    if hitlist == ['AltA,AltD,IntronR']:
        n125 = n125 +1

    if hitlist == ['AltA,AltP,ExonS']:
        n134 = n134 +1

    if hitlist == ['AltA,AltP,IntronR']:
        n135 = n135 +1

    if hitlist == ['AltA,ExonS,IntronR']:
        n145 = n145 +1

    if hitlist == ['AltD,AltP,ExonS']:
        n234 = n234 +1

    if hitlist == ['AltD,AltP,IntronR']:
        n235 = n235 +1

    if hitlist == ['AltD,ExonS, IntronR']:
        n245 = n245 +1

    if hitlist == ['AltP,ExonS,IntronR']:
        n345 = n345 +1

    if hitlist == ['AltA,AltD,AltP,ExonS']:
        n1234 = n1234 +1

    if hitlist == ['AltA,AltD,AltP,IntronR']:
        n1235 = n1235 +1

    if hitlist == ['AltA,AltD,ExonS,IntronR']:
        n1245 = n1245 +1

    if hitlist == ['AltA,AltP,ExonS,IntronR']:
        n1345 = n1345 +1

    if hitlist == ['AltD,AltP,ExonS,IntronR']:
        n2345 = n2345 +1
print "n12 = ", n12 + n123 + n124 + n125 + n1234 + n1235 + n1245 + n12345
print "n13 = ", n13 + n123 + n134 + n135 + n1234 + n1235 + n1345 + n12345
print "n14 = ", n14 + n124 + n134 + n145 + n1234 + n1245 + n1345 + n12345
print "n15 = ", n15 + n125 + n135 + n145 + n1235 + n1245 + n1345 + n12345

print "n23 = ", n23 + n123 + n234 + n235 + n1234 + n1235 + n2345 + n12345
print "n24 = ", n24 + n124 + n234 + n245 + n1234 + n1245 + n2345 + n12345
print "n25 = ", n25 + n125 + n235 + n245 + n1235 + n1245 + n2345 + n12345
print "n34 = ", n34 + n134 + n234 + n345 + n1234 + n1345 + n2345 + n12345
print "n35 = ", n35 + n135 + n235 + n345 + n1235 + n1345 + n2345 + n12345
print "n45 = ", n45 + n145 + n245 + n345 + n1245 + n1345 + n2345 + n12345

print "n123 = ", n123 + n1234 + n1235 + n12345
print "n124 = ", n124 + n1234 + n1245 + n12345
print "n125 = ", n125 + n1235 + n1245 + n12345
print "n134 = ", n134 + n1234 + n1345 + n12345
print "n135 = ", n135 + n1235 + n1345 + n12345
print "n145 = ", n145 + n1245 + n1345 + n12345

print "n234 = ", n234 + n1234 + n2345 + n12345
print "n235 = ", n235 + n1235 + n2345 + n12345
print "n245 = ", n245 + n1245 + n2345 + n12345
print "n345 = ", n345 + n1345 + n2345 + n12345

print "n1234 = ", n1234 + n12345
print "n1235 = ", n1235 + n12345
print "n1245 = ", n1245 + n12345
print "n1345 = ", n1345 + n12345
print "n2345 = ", n2345 + n12345
print "n12345 = ", n12345
