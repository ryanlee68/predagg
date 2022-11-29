from sqlalchemy import create_engine
from models import Canon, Base, Isoform, Metascores
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\main.db", echo=True)
Session = sessionmaker(bind=engine)
# session = Session()
Base.metadata.create_all(engine)

with Session() as session:
    # canon = session.get(Canon, 'O43497')
    # print(canon.isoforms)

# Isoform.__table__.drop(engine)
# getting info from fasta
# from Bio import SeqIO

# with open("humengenome.fasta") as handle:
#     for record in SeqIO.parse(handle, "fasta"):
#         base_name = record.name.split("|")
#         uniprotid = base_name[1]
#         # # family_member = base_name[2]
#         # sequence = str(record.seq)

#         if '-' in uniprotid:
#             # print('- not in uniprotid')
#             # print(type(uniprotid))
#             # print(type(family_member))
#             # print(type(sequence))
#             # print(sequence)
#             # eg_canon = Canon(id=uniprotid, family_member=family_member, sequence=sequence)

#             # session.add(eg_canon)

#             base_name = record.name.split("|")
#             iso_uniprotid = uniprotid.replace('-', '_')
#             # family_member = base_name[2]
#             iso_sequence = str(record.seq)
#             iso_id = uniprotid.split('-', 1)[0]

#             print("iso uniprotid " + iso_uniprotid)
#             print("iso_sequence " + iso_sequence)
#             print("iso id " + iso_id)

#             eg_isoform = Isoform(id=iso_uniprotid, sequence=iso_sequence, canon_id=iso_id)

#             session.add(eg_isoform)

        
        # print("Uniprot Id: " + uniprotid)
        # print("Family Member: " + family_member)
        # print("Sequence: " + sequence)

# eg_canon = Canon(id="junk", family_member="fam member", sequence="seqjunk")

# print(eg_canon.id)
# print(eg_canon.family_member)
# print(eg_canon.sequence)

# session.add(eg_canon)

# ?