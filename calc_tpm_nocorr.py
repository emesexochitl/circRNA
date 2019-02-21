#!/usr/bin/python

import datetime
import math

fcfile="counts_lariat_WT.txt"

fclist=[]
with open(fcfile) as inputfile:
    for line in inputfile:
        fclist.append(line.strip().split(' '))

fc1=[item[0] for item in fclist]
fc2=[float(item[1]) for item in fclist]
fc3=[float(item[2]) for item in fclist]

sum = 0
tpm = 0
fpkm_sum = 0
tpm_sum = 0

for i in xrange(0, len(fclist)):
    rpk = float(fc3[i])/float(fc2[i])
    #print rpk
    sum = sum + rpk
print sum

scaling_factor = float(sum/1000000)

print scaling_factor

outfile="lariat_WT_TPM_vals.txt"
myfile= open(outfile, "w")

for j in xrange(0, len(fclist)):
    if fc3[j] > 0:
        tpm = (fc3[j]/fc2[j])/scaling_factor
        fpkm_sum= fpkm_sum +  float(fc3[j]/fc2[j])
        tpm_sum = tpm_sum + tpm
        tpmlog2 = math.log(tpm,2)

        #print fc1[j], fc2[j], fc3[j], tpm, tpmlog2
        myfile.write("%s\t%d\t%.3f\t%.10f\t%.3f\n" % (fc1[j], fc2[j], fc3[j], tpm, tpmlog2))    

print fpkm_sum, tpm_sum
myfile.close()
