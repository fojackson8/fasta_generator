
# coding: utf-8


import random

all_chroms = []
def fasta_generator(seq_length, n_chrom):
    global allchroms
    global each_chrom
    seq = 'chop'
    for j in range(1,n_chrom +1):
        name = '>chr%d\n' % j
        for i in range(1,seq_length+1):
            base = random.choice('ACGT')
            seq = seq+base
            final_seq = seq[4:] + '\n'
        each_chrom = name+final_seq
        # Need to reset seq for each iteration (/find another way around this?)
        seq = 'chop'
        all_chroms.append(each_chrom)
        
        # Now write fasta sequence to a text file
        with open("fasta_sample.txt", "a") as fasta_file:
            fasta_file.write(all_chroms[j-1])
   
fasta_generator(1000,20)

# How can I generate reads with a varying degree of overlap?







