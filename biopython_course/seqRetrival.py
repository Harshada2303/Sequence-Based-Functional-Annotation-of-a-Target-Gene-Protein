from Bio import SeqIO 

record = SeqIO. read("sequence.fasta","fasta")

print("Sequence ID:",record.id) 
print("Sequence:") 
print(record.seq)
print("Sequence Length:",len(record.seq))

