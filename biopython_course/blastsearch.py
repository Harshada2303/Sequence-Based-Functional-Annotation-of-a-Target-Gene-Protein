from Bio import SeqIO
from Bio.Blast import NCBIWWW

record = SeqIO.read("sequence.fasta", "fasta")
seq =record.seq

result_handle = NCBIWWW.qblast("blastp", "nr", seq)

with open ("blast_result_xml", "w") as out:
    out.write(result_handle.read())
    result_handle.close()

print("Blast completed. Results saved as blast_result_xml")