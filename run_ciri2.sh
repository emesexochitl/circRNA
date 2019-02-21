#!/bin/bash

while read l
do

echo "$l"

bwa mem -T 19 ../references/Araport11/TAIR10_Chr.all.fasta ${l}_rt_filtered_1.fq.gz ${l}_rt_filtered_2.fq.gz 1> aln-pe_circwt3.sam 2> aln-pe_circwt3.log

perl ~/CIRI_v2.0.2/CIRI_v2.0.2/CIRI_v2.0.2.pl -I aln-pe_circwt3.sam -O aln-pe_circwt3.out -F ../references/Arabidopsis_thaliana.TAIR10.31.dna.genome.fa -A ../references/Arabidopsis_thaliana.TAIR10.31.gtf

done < sra_phos_list.txt

