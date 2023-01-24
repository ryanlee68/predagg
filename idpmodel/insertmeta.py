import matplotlib as plot

import numpy as np

import metapredict as meta

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Canon, Isoform

# below is for windows
engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\test.db", echo=False)
# below is for mac
# engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/main.db")

with Session(engine) as session:
    canonlist = session.query(Canon).all()
    i = False
    for canon in canonlist:
        if canon.metascore:
            for isoform in canon.isoforms:
                if isoform.metascore:
                    pass
                else:
                    i = True
                    break
