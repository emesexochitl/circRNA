#!/bin/bash
while read l
do

echo "$l"

reads1=`gunzip -c ${l}_1.fastq.gz | awk '{if (NR%4==1) print $1"/1"; else print $0}'`
reads2=`gunzip -c ${l}_2.fastq.gz | awk '{if (NR%4==1) print $1"/2"; else print $0}'`
python ~/MapSplice-v2.2.0/mapsplice.py -p 8 --min-fusion-distance 200 --bam --fusion-non-canonical --filtering 1 --qual-scale phred33  --gene-gtf ../../INTENSO1/circTREATMENT/references/Arabidopsis_thaliana.TAIR10.31.gtf -c ../../INTENSO1/circTREATMENT/mapsplice2_reference  -1 $reads1  -2 $reads2 -o maplsplice_out_${num}

done < sra_phos_list_ciri2.txt
