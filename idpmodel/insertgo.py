# at this point, it has become too much data to store into memory
# talk about computation limitations
# not storage limitations

from sqlalchemy import create_engine
from models import Canon, Base, Isoform, Annotation
from sqlalchemy.orm import sessionmaker
import json
import orjson
# import metapredict as meta
# import sys
# import numpy as np
# from Bio import SeqIO
# np.set_printoptions(threshold=sys.maxsize)

# testing db
engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\test2k.db", echo=False)
# below is for windows
# engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\main.db", echo=True)
# below is for mac
# engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/main.db", echo=True)


Session = sessionmaker(bind=engine)
# session = Session()
Base.metadata.create_all(engine)

with Session() as session:
    with open("C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\main.json") as handle:
        data = orjson.loads(handle)
        print(data['results'][0]['primaryAccession'])


    session.commit()