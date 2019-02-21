#!/usr/bin/python

import datetime

ref="circ_ref.txt"
references=[]
with open(ref) as inputfile:
    for line in inputfile:
       references.append(line.strip().split(' '))

ref1=[item[0] for item in references]
ref2=[item[1] for item in references]
ref3=[item[2] for item in references]
ref4=[item[3] for item in references]
ref5=[item[4] for item in references]
ref6=[item[5] for item in references]

#merge_file= open("reference.txt", "w")
#for i in xrange(0,len(references)):
#     merge_file.write("%s_%s_%s\t\n" % (ref1[i], ref2[i], ref3[i]))
#merge_file.close()

samples=["SRR3087771", "SRR3087772", "SRR3087773", "SRR3087774", "SRR3087775", "SRR3087776", "SRR3087777", "SRR3087779", "SRR3087780", "SRR3087781", "SRR3087782", "SRR3087783", "SRR3087784", "SRR3087785", "SRR3087786"]

for libnum in samples:

    input = "circ_cov%s.txt" % (libnum)
    output="circ_bp_%s_de.txt" % (libnum)
    now = datetime.datetime.now()
 
    results=[]
    with open(input) as inputfile:
        for line in inputfile:
            results.append(line.strip().split(' '))

    res1=[item[0] for item in results]
    res2=[item[1] for item in results]
    res3=[item[2] for item in results]
    res4=[item[3] for item in results]

    myfile= open(output, "w")
 
    for i in xrange(0,len(references)):
        for j in xrange(0,len(results)):   
            hit=False

            if ref1[i]==res1[j] and ref2[i]==res2[j] and ref3[i]==res3[j]:
                #print "%s_%s_%s\t%s" % (ref1[i], ref2[i], ref3[i], res4[j])
                hit=True
                myfile.write("%s_%s_%s_%s_%s_%s\t%s\n" % (ref1[i], ref2[i], ref3[i], ref4[i], ref5[i], ref6[i], res4[j]))
                #appendfile.write("\t%s" % (res4[j]))
                break
            elif ref1[i]!=res1[j] and ref2[i]!=res2[j] and ref3[i]!=res3[j]:
                continue            
        
        if hit == False:
           #print "%s_%s_%s\t0" % (ref1[i], ref2[i], ref3[i])
           myfile.write("%s_%s_%s_%s_%s_%s\t0\n" % (ref1[i], ref2[i], ref3[i], ref4[i], ref5[i], ref6[i]))
           #appendfile.write("\t0")

    myfile.close()

print now
