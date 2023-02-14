from sqlalchemy import create_engine
from models import Canon, Base, Isoform
from sqlalchemy.orm import sessionmaker
import metapredict as meta
import sys
import numpy as np
from Bio import SeqIO
np.set_printoptions(threshold=sys.maxsize)

# testing db
engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\214db.db", echo=False)
# below is for windows
# engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\main.db", echo=True)
# below is for mac
# engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/main.db", echo=True)


Session = sessionmaker(bind=engine)
# session = Session()
Base.metadata.create_all(engine)

with Session() as session:
    c = 0
    # canon = session.query(Canon).get("P04637")
    # print(canon)
    with open("C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\214fasta.fasta") as handle:
        # i = 0
        for record in SeqIO.parse(handle, "fasta"):

            # if i < 1000:
            #     pass
            # else:

            base_name = record.name.split("|")
            uniprotid = base_name[1]
            family_member = base_name[2]
            sequence = str(record.seq)

            if '-' in uniprotid:
                # print('- not in uniprotid')
                # print(type(uniprotid))
                # print(type(family_member))
                # print(type(sequence))
                # print(sequence)
                # eg_canon = Canon(id=uniprotid, family_member=family_member, sequence=sequence)

                # session.add(eg_canon)

                base_name = record.name.split("|")
                iso_uniprotid = uniprotid.replace('-', '_')
                # family_member = base_name[2]
                iso_sequence = str(record.seq)
                iso_id = uniprotid.split('-', 1)[0]

                # print("iso uniprotid " + iso_uniprotid)
                # print("iso_sequence " + iso_sequence)
                # print("iso id " + iso_id)
                
                try:
                    eg_isoform = Isoform(id=iso_uniprotid, sequence=iso_sequence, canon_id=iso_id, precentdisordered = meta.percent_disorder(iso_sequence))
                except Exception as e:
                    eg_isoform = Isoform(id=iso_uniprotid, sequence=iso_sequence, canon_id=iso_id, precentdisordered = None)

                session.add(eg_isoform)
            else:
                # print("Uniprot Id: " + uniprotid)
                # print("Family Member: " + family_member)
                # print("Sequence: " + sequence)
                # print(meta.predict_disorder(sequence))
                # print(type(meta.predict_disorder(sequence)))
                # print(" ".join(meta.predict_disorder(sequence)))
                # print(type(" ".join(meta.predict_disorder(sequence))))
                try:
                    eg_canon = Canon(id=uniprotid, family_member=family_member, sequence=sequence, precentdisordered = meta.percent_disorder(sequence))
                except Exception as e:
                    eg_canon = Canon(id=uniprotid, family_member=family_member, sequence=sequence, precentdisordered = None)

                session.add(eg_canon)
                print(c)
                c+=1
            
                # print("Uniprot Id: " + uniprotid)
                # print("Family Member: " + family_member)
                # print("Sequence: " + sequence)

            # i+=1
            # if i > 3000:
            #     break


    session.commit()



# with Session() as session:
    
    # canon = session.query(Canon).all()
    # for canon in canon:
        # metascore = Canonmetascore(id=canon.id, score=np.ndarray.tolist(meta.predict_disorder_domains(canon.sequence).disorder)))
        # print(canon.metascore)
        # print(canon.id)
    # sequence = canon.isoforms[0].sequence
    # sequence = canon.isoforms[0].sequence
    # print(sequence)
    # print(type(np.ndarray.tolist(meta.predict_disorder_domains(sequence).disorder)))
    # metascore = Metascore(id=)
    
    # print(len(sequence))
    # print(len(meta.predict_disorder_domains(sequence).disorder))

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