# at this point, it has become too much data to store into memory
# talk about computation limitations
# not storage limitations

from sqlalchemy import create_engine
from models import Canon, Base, Isoform, Annotation
from sqlalchemy.orm import sessionmaker
import json
import orjson
import requests
import pandas as pd
# import metapredict as meta
# import sys
# import numpy as np
# from Bio import SeqIO
# np.set_printoptions(threshold=sys.maxsize)

# testing db
engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\4-4-2023-test2k.db", echo=False)
# below is for windows
# engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\main.db", echo=True)
# below is for mac
# engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/main.db", echo=True)


Session = sessionmaker(bind=engine)
# session = Session()
Base.metadata.create_all(engine)

gaffile = 'C:\\Users\\ryanl\\Downloads\\humangoa\\goa_human.gaf'

df = pd.read_csv(gaffile)
print(df)

with Session() as session:
    canon = session.query(Canon).all()
    for canon in canon:
        productid = 'A0A024RBG1'
        requestURL = f"https://www.ebi.ac.uk/QuickGO/services/annotation/search?page=1&limit=25&geneProductId={productid}"

        r = requests.get(requestURL)

        GoId = ''
        Reference = ''
        EvidenceCode = ''
        GoAspect = ''

        try:
            responseBody = r.json()
            GoId = responseBody['results'][0]['goId']
            Reference = responseBody['results'][0]['reference']
            EvidenceCode = responseBody['results'][0]['evidenceCode']
            GoAspect = responseBody['results'][0]['goAspect']
        except Exception as e:
            print(e)

        print()

    session.commit()