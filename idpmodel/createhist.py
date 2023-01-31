# use another proteome for testing purposes
# meta has a average function already

import matplotlib as plot

import numpy as np

import metapredict as meta

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Canon, Isoform

# below is for windows
# engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\test.db", echo=False)
# below is for mac
engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/test.db")

maindf = pd.DataFrame({'uniprotid':[], 'canonavgmeta':[], 'isoavgmeta':[], 'avgdifferences':[]})

with Session(engine) as session:
    canonlist = session.query(Canon).all()
    i = False
    for canon in canonlist:
        if canon.metascore:
            pass
        for isoform in canon.isoforms:
            if isoform.metascore:
                pass
            else:
                i = True
                break
        if i:
            i = False
            pass
        else:
            isotot = np.array([])
            for isoform in canon.isoforms:
                temp = np.array(map(float, isoform.metascore.split(" ")))
                isotot.append(temp)
            df2 = {'uniprotid':canon.id, 'canonavgmeta':[eval(i) for i in canon.metascore.split(" ")], 'isoavgmeta':[], 'avgdifferences':[]}
            maindf.append(df2, ignore_index=True)
            # maindf['uniprotid'] = canon.id
            # print([eval(i) for i in canon.metascore.split(" ")])
            # maindf['canonavgmeta'] = [eval(i) for i in canon.metascore.split(" ")]
print(maindf)
