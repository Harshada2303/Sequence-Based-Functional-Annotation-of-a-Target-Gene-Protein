from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis 


record = SeqIO.read("Sequence.fasta", "fasta")
seq = record.seq 

print("Sequence Length",len(seq))

print("Sequence Type: protein")
protein = ProteinAnalysis(str(seq))
aa_comp = protein.get_amino_acids_percent ()
print("Amino Acid Composition")