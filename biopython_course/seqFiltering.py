from Bio import SeqIO
from Bio.SeqUtils import ProtParam

MIN_LENGTH = 10

record = SeqIO.read("sequence.fasta", "fasta")
seq = record.seq
print("sequence ID:", record.id)
print("sequence length:", len(seq))

len(seq) < MIN_LENGTH
print("Sequence is too short for downstream analysis")
print("Sequence is suitable for further analysis")