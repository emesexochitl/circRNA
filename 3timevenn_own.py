#!/usr/bin/python

import datetime
import math

reffile="mapsplice2_ref_coord.txt"
#reffile="test.txt"

reflist=[]
with open(reffile) as inputfile:
    for line in inputfile:
        reflist.append(line.strip().split('\t'))

ref1=[item[0] for item in reflist] # Chr
ref2=[int(item[1]) for item in reflist] # Circ start
ref3=[int(item[2]) for item in reflist] # Circ end


bigfile="mapsplice2_big_coord.txt"

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
n12 = 0
n23 = 0
n13 = 0
n123 = 0

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
    

    if hitlist == ['MeJa']:
        n1 = n1 +1

    if hitlist == ['Mock']:
        n2 = n2 +1

    if hitlist == ['SA']:
        n3 = n3 +1

    if hitlist == ['MeJa', 'Mock']:
        n12 = n12 +1

    if hitlist == ['MeJa', 'SA']:
        n13 = n13 +1

    if hitlist == ['Mock', 'SA']:
        n23 = n23 +1

    if hitlist == ['MeJa', 'Mock', 'SA']:
        n123 = n123 +1

print n1,n2,n3, n12, n23, n13, n123
print "n12 = ", n12 + n123
print "n23 = ", n23 + n123
print "n13 = ", n13 + n123
print "n123 = ", n123

    #myfile.write("%s\t%d\t%.3f\t%.3f\t%.3f\n" % (fc1[j], fc2[j], fc3[j], tpm, tpmlog2))    
#myfile.close()
