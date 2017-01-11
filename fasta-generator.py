
# coding: utf-8

# In[31]:

test = range(1,11,1)
import random as random

from decimal import Decimal

a = Decimal(0.25)

type(a)


# In[268]:

# Would be good to include into this function a way of skewing the base picker with customised odds. Say you want G to
# appear slightly less than 1 times in 4..

import random 
seq = 'chop'

def random_seq(read_length,seed):
    
    global base
    global seq
    global final_seq1
    
    for i in range(read_length):
        random.seed(seed)
        choice = random.random()
           
        prob = 0.25
        if choice <= prob:
            base = 'a'
        elif prob < choice <= 2*prob:
            base = 'c'
        elif 2*prob < choice <= 3*prob:
            base = 't'
        else:
            base = 'g'
        
        seq = seq+base
        final_seq1= seq[4:] + '\n'


random_seq(10,1)
final_seq1


# In[17]:




# In[29]:

###This is the one that works!!
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




# In[18]:

all_chroms = []

def fasta_generator(read_length, n_chrom):
    global full_str
    global all_chroms
    global each_chrom
    
    for j in range(1,n_chrom+1):
        random_seq(read_length)
        name = '>chr%d\n' % j
        each_chrom = {'chr_name':name, 'seq':final_seq1}
        
        all_chroms.append(each_chrom)
        
        
        
fasta_generator(10,4)
      




# In[222]:

all_chroms = []

def fasta_generator(read_length, n_chrom):
    global full_str
    global all_chroms
    global full_fasta
    
    for j in range(1,n_chrom+1):
        random_seq(read_length)
        name = '>chr%d\n' % j
        full_str = name +final_seq1
        all_chroms.append(full_str)
        full_str
        final_seq1 = []
        
fasta_generator(10,4)
        
all_chroms
            
    


# In[171]:

name = 'chr%d \n' %1
bla = 'a'
test = name+bla
print(test)


# In[173]:

random_base(10).final_seq


# In[132]:

my_file = open("my_fasta.txt", "w+")


# In[ ]:



