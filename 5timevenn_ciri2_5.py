#!/usr/bin/python

import datetime
import math

reffile="ciri2_ref_coord5.txt"
#reffile="test.txt"

reflist=[]
with open(reffile) as inputfile:
    for line in inputfile:
        reflist.append(line.strip().split('\t'))

ref1=[item[0] for item in reflist] # Chr
ref2=[int(item[1]) for item in reflist] # Circ start
ref3=[int(item[2]) for item in reflist] # Circ end


bigfile="ciri2_big_coord5.txt"

biglist=[]
with open(bigfile) as inputfile:
    for line in inputfile:
        biglist.append(line.strip().split('\t'))

big1=[item[0] for item in biglist] # Chr
big2=[int(item[1]) for item in biglist] # Circ start
big3=[int(item[2]) for item in biglist] # Circ end
big4=[item[4] for item in biglist] # Sample name

chr = None
circ_start = 0
circ_end = 0
hitlist = []

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


#outfile="all_4timevenn_list.txt"
#myfile= open(outfile, "w")

for i in xrange(0, len(reflist)):

    chr = None
    circ_start = 0 
    circ_end = 0
    hitlist = []

    for j in xrange(0, len(biglist)):
    
        if ref1[i]==big1[j] and ref2[i]==big2[j] and ref3[i]==big3[j]:

            chr = big1[j]
            circ_start = big2[j]
            circ_end = big3[j]
            hitlist.append(big4[j])
            hitlist.sort()

    #print hitlist
    
    if hitlist == ['MeJa', 'Mock', 'SA', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n12345 = n12345 +1

    if hitlist == ['MeJa']:
        n1 = n1 +1

    if hitlist == ['Mock']:
        n2 = n2 +1

    if hitlist == ['SA']:
        n3 = n3 +1

    if hitlist == ['WT-RnaseR-PolyAmin']:
        n4 = n4 +1

    if hitlist == ['WT-RnaseR-PolyAmin']:
        n5 = n5 +1

    if hitlist == ['MeJa', 'Mock']:
        n12 = n12 +1

    if hitlist == ['MeJa', 'SA']:
        n13 = n13 +1

    if hitlist == ['MeJa', 'WT-RnaseR-PolyAmin']:
        n14 = n14 +1

    if hitlist == ['MeJa', 'dbr1-2-RnaseR-PolyAmin']:
        n15 = n15 +1

    if hitlist == ['Mock', 'SA']:
        n23 = n23 +1

    if hitlist == ['Mock', 'dbr1-2-RnaseR-PolyAmin']:
        n24 = n24 +1

    if hitlist == ['Mock', 'dbr1-2-RnaseR-PolyAmin']:
        n25 = n25 +1

    if hitlist == ['SA', 'WT-RnaseR-PolyAmin']:
        n34 = n34 +1

    if hitlist == ['SA', 'dbr1-2-RnaseR-PolyAmin']:
        n35 = n35 +1

    if hitlist == ['WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n45 = n45 +1

    if hitlist == ['MeJa', 'Mock', 'SA']:
        n123 = n123 +1

    if hitlist == ['MeJa', 'Mock', 'WT-RnaseR-PolyAmin']:
        n124 = n124 +1

    if hitlist == ['MeJa', 'Mock', 'dbr1-2-RnaseR-PolyAmin']:
        n125 = n125 +1

    if hitlist == ['MeJa', 'SA', 'WT-RnaseR-PolyAmin']:
        n134 = n134 +1

    if hitlist == ['MeJa', 'SA', 'dbr1-2-RnaseR-PolyAmin']:
        n135 = n135 +1

    if hitlist == ['MeJa', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n145 = n145 +1

    if hitlist == ['Mock', 'SA', 'WT-RnaseR-PolyAmin']:
        n234 = n234 +1

    if hitlist == ['Mock', 'SA', 'dbr1-2-RnaseR-PolyAmin']:
        n235 = n235 +1

    if hitlist == ['Mock', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n245 = n245 +1

    if hitlist == ['SA', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n345 = n345 +1

    if hitlist == ['MeJa', 'Mock', 'SA', 'WT-RnaseR-PolyAmin']:
        n1234 = n1234 +1

    if hitlist == ['MeJa', 'Mock', 'SA', 'dbr1-2-RnaseR-PolyAmin']:
        n1235 = n1235 +1

    if hitlist == ['MeJa', 'Mock', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n1245 = n1245 +1

    if hitlist == ['MeJa', 'SA', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n1345 = n1345 +1

    if hitlist == ['Mock', 'SA', 'WT-RnaseR-PolyAmin', 'dbr1-2-RnaseR-PolyAmin']:
        n2345 = n2345 +1

#print "n1, n2, n3, n4, n12, n23, n14, n24, n123, n134, n124, n234, n1234"

print n1, n2, n3, n4, n5, n12, n13, n14, n15, n23, n24, n25, n34, n35, n45, "!", n123, n124, n125, n134, n135, n145, n234, n235, n345, n1234, n1235, n1245, n1345, n12345

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


#print "for checking  R:", cs12, cs13, cs14, cs23, cs24, cs34, cs123, cs124, cs134, cs234, cs1234

    #myfile.write("%s\t%d\t%.3f\t%.3f\t%.3f\n" % (fc1[j], fc2[j], fc3[j], tpm, tpmlog2))    
#myfile.close()
