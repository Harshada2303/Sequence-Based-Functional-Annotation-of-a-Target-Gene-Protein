from Bio.Blast import NCBIXML

with open("blast_result_xml") as handle:
    blast_record = NCBIXML.read(handle)

    blast_record.alignments
    alignment = blast_record.alignments[0] 
    hsp = alignment.hsps[0]

    print("Top Hit:", alignment.title)
    print("Protein Description:",alignment.hit_def) 
    print("alignment score:", hsp.score)
    print("E-value:", hsp.expect)