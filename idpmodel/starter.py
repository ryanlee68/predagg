from Bio import SeqIO

with open("fastainf.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        base_name = record.name.split("|")
        uniprotid = base_name[1]
        family_member = base_name[2]
        sequence = record.seq

        print("Uniprot Id: " + uniprotid)
        print("Family Member: " + family_member)
        print("Sequence: " + sequence)