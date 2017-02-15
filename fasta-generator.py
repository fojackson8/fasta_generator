
# First I define a mutator, that randomly mutates one base every n bases, where n is the input to the mutator
# function (called mutant_freq). Then I define the fasta generator function, which takes as arguments the length of
# each chromosome, and the number of chromosomes you want. Then I call them both together. Both fasta 
# and mutated sequence are stored wherever you set their path to.

import random

# Set a place to store fasta and mutated sequence

fasta_path = "/wherever/you/want/" + "fasta_sequence%d.fa"
mutated_path = "/wherever/you/want/" + "mutated_sequence%d.fa"



def mutator(mutant_freq):
    final_seq_dup = final_seq[0:-1]
    targets = range(0,len(final_seq_dup),mutant_freq)
    global mutated_full
    almost_full = ''
    mutated_cut = ''
    mutated_full = ''
    
    for i in range(0,len(targets)-1,1):
            if final_seq_dup[targets[i]] == 'G':
                mutated_cut = random.choice('ACT') + final_seq_dup[targets[i]+1:targets[i+1]] 
            elif final_seq_dup[targets[i]] == 'C':
                mutated_cut = random.choice('AGT') + final_seq_dup[targets[i]+1:targets[i+1]] 
            elif final_seq_dup[targets[i]] == 'T':
                mutated_cut = random.choice('ACG') + final_seq_dup[targets[i]+1:targets[i+1]]
            elif final_seq_dup[targets[i]] == 'A':  
                mutated_cut = random.choice('GCT') + final_seq_dup[targets[i]+1:targets[i+1]]

            almost_full = almost_full + mutated_cut
            mutated_full = almost_full + final_seq_dup[targets[i+1]:] + '\n'

# This counter allows you to generate multiple random fasta and mutated sequences, and stores them in separate
# locations, by increasing the number appended to the file name by 1 each time.
counter = 5



all_chroms = []
all_mutated_chroms = []

def fasta_generator(seq_length, n_chrom, mutant_freq):
    global counter
    global allchroms
    global all_mutated_chroms
    global each_chrom
    global final_seq
    counter += 1
    seq = 'chop'
    for j in range(1,n_chrom +1):
        name = '>chr%d\n' % j
        for i in range(1,seq_length+1):
            base = random.choice('ACGT')
            seq = seq+base
            final_seq = seq[4:] + '\n'
        each_chrom = name+final_seq
        if mutant_freq > 0:
            mutator(mutant_freq)
            mutated_chrom = name + mutated_full
            all_mutated_chroms.append(mutated_chrom)
            
            with open(mutated_path %counter, "a") as fasta_file:
                fasta_file.write(all_mutated_chroms[j-1])
            
        # Need to reset seq for each iteration 
        seq = 'chop'
        all_chroms.append(each_chrom)
        
        
        # Now write fasta sequence to a text file
        with open(fasta_path %counter, "a") as fasta_file:
            fasta_file.write(all_chroms[j-1])
   
        
            
# Now, calling this function will create both a random fasta sequence and a mutated version of the same sequence.
# These two sequences will be stored in wherever you set path to be.

fasta_generator(500,23,10)







