# use another proteome for testing purposes
# meta has a average function already

import matplotlib as plot

import numpy as np

import metapredict as meta

import pandas as pd

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Canon, Isoform

# below is for windows
engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\acttest.db", echo=False)
# below is for mac
# engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/test.db")

# maindf = pd.DataFrame({'uniprotid':[], 'canonavgmeta':[], 'isoavgmeta':[], 'avgdifferences':[]})

df = pd.read_sql_query(
    sql = sqlalchemy.select([Canon.id,
                     Canon.family_member,
                     Canon.precentdisordered]),
    con = engine
)
id = []
isolistdisordered = []
with Session(engine) as session:
    isoformlistquery = session.query(Isoform).all()
    for isoform in isoformlistquery:
        id.append(isoform.canon_id)
        isolistdisordered.append(isoform.precentdisordered)
    id.append('O60260')
    isolistdisordered.append(79.69)
    isodf = pd.DataFrame({'id': id, 'isolistdisordered': isolistdisordered})
newdf = pd.merge(df, isodf, on="id")
newdf['difference'] = newdf['precentdisordered'] - newdf['isolistdisordered']
print("Type:", type(newdf))
print()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 2)
print(newdf)
newdf.hist()

# with Session(engine) as session:
#     canonlist = session.query(Canon).all()
#     df = pd.read_sql_query(canonlist, engine)
#     # df.to_csv(index=False)
#     print(df.info())
#     # print(df)
#     df.to_csv("C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\test.csv", index=False)
    # # i = False
    # for canon in canonlist:
    #     maindf['uniprotid'] = canon.id
    #     maindf['canonavgmeta'] = 
