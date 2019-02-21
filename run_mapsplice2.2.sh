#!/bin/bash

#for num in SRR2145235 SRR2145236 SRR2145238 SRR2145245 SRR2145246 SRR2145247 SRR2145248
for num in  SRR2145231
do

python ~/MapSplice-v2.2.0/mapsplice.py -p 8 --min-fusion-distance 200 --bam --fusion-non-canonical --filtering 1 --qual-scale phred33  --gene-gtf ../mapsplice2_references/Arabidopsis_thaliana.TAIR10.34.gtf -c ../mapsplice2_references\
 -1 ../ribo_trna_filtering/${num}_lariat_rt_filtered_1.fq -2 ../ribo_trna_filtering/${num}_lariat_rt_filtered_2.fq -o mapsplice2.2_out_${num}

#mv mapsplice_out/  mapsplice_out_${num}

done
