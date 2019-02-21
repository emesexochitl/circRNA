#!/usr/bin/python

import datetime
import math

reffile="own_ref_coord.txt"
#reffile="test.txt"

reflist=[]
with open(reffile) as inputfile:
    for line in inputfile:
        reflist.append(line.strip().split('\t'))

ref1=[item[0] for item in reflist] # Chr
ref2=[int(item[1]) for item in reflist] # Circ start
ref3=[int(item[2]) for item in reflist] # Circ end


bigfile="own_big_coord.txt"

biglist=[]
with open(bigfile) as inputfile:
    for line in inputfile:
        biglist.append(line.strip().split('\t'))

big1=[item[0] for item in biglist] # Chr
big2=[int(item[1]) for item in biglist] # Circ start
big3=[int(item[2]) for item in biglist] # Circ end
big4=[item[4] for item in biglist] # Software

chr = None
circ_start = 0
circ_end = 0
hitlist = []

cs1 = 0
cs2 = 0
cs3 = 0
cs4 = 0
cs12 = 0
cs23 = 0
cs34 = 0
cs24 = 0
cs13 = 0
cs14 = 0
cs124 = 0
cs123 = 0
cs134 = 0
cs234 = 0
cs1234 = 0

#n12: The size of the intersection between the first and the second set
#n13: The size of the intersection between the first and the third set
#n14: The size of the intersection between the first and the fourth set
#n23: The size of the intersection between the second and the third set
#n24: The size of the intersection between the second and the fourth set
#n34: The size of the intersection between the third and the fourth set
#n123: The size of the intersection between the first, second and third sets
#n124: The size of the intersection between the first, second and fourth sets
#n134: The size of the intersection between the first, third and fourth sets
#n234: The size of the intersection between the second, third and fourth sets
#n1234: The size of the intersection between all four sets

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
    
    if hitlist == ['CIRI2', 'MapSplice2.2', 'find_circ', 'segemehl_0.2.0']:
        cs1234 = cs1234 +1

    if hitlist == ['CIRI2']:
        cs1 = cs1 +1

    if hitlist == ['MapSplice2.2']:
        cs2 = cs2 +1

    if hitlist == ['find_circ']:
        cs3 = cs3 +1

    if hitlist == ['segemehl_0.2.0']:
        cs4 = cs4 +1

    if hitlist == ['CIRI2', 'MapSplice2.2']:
        cs12 = cs12 +1

    if hitlist == ['MapSplice2.2', 'find_circ']:
        cs23 = cs23 +1

    if hitlist == ['find_circ', 'segemehl_0.2.0']:
        cs34 = cs34 +1

    if hitlist == ['MapSplice2.2', 'segemehl_0.2.0']:
        cs24 = cs24 +1

    if hitlist == ['CIRI2', 'segemehl_0.2.0']:
        cs14 = cs14 +1

    if hitlist == ['CIRI2', 'find_circ']:
        cs13 = cs13 +1

    if hitlist == ['CIRI2', 'MapSplice2.2', 'find_circ']:
        cs123 = cs123 +1

    if hitlist == ['CIRI2', 'find_circ', 'segemehl_0.2.0']:
        cs134 = cs134 +1

    if hitlist == ['MapSplice2.2', 'find_circ', 'segemehl_0.2.0']:
        cs234 = cs234 +1

    if hitlist == ['CIRI2', 'MapSplice2.2',  'segemehl_0.2.0']:
        cs124 = cs124 +1

print "cs1, cs2, cs3, cs4, cs12, cs23, cs14, cs24, cs123, cs134, cs124, cs234, cs1234"

print cs1, cs2, cs3, cs4, cs12, cs23, cs14, cs24, cs13, cs123, cs134, cs124, cs234, cs1234

print "n12 = ", cs12 + cs123 + cs124 + cs1234
print "n13 = ", cs13 + cs123 + cs134 + cs1234
print "n14 = ", cs14 + cs124 + cs134 + cs1234
print "n23 = ", cs23 + cs123 + cs234 + cs1234
print "n24 = ", cs24 + cs124 + cs234 + cs1234
print "n34 = ", cs34 + cs134 + cs234 + cs1234
print "n123 = ", cs123 + cs1234
print "n124 = ", cs124 + cs1234              
print "n134 = ", cs134 + cs1234                      
print "n234 = ", cs234 + cs1234              
print "n1234 = ", cs1234                       


print "for checking  R:", cs12, cs13, cs14, cs23, cs24, cs34, cs123, cs124, cs134, cs234, cs1234

    #myfile.write("%s\t%d\t%.3f\t%.3f\t%.3f\n" % (fc1[j], fc2[j], fc3[j], tpm, tpmlog2))    
#myfile.close()
