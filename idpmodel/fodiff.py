# Difference in disordered scores between isoforms and canonical
# x axis - difference of scores between isoform and canonical
# y-axis - frequency

import matplotlib as plot

import numpy as np

import metapredict as meta

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Canon, Isoform

# below is for windows
# engine = create_engine("sqlite:///C:\\Users\\ryanl\\OneDrive\\Repos\\predagg\\idpmodel\\finaldata\\main.db", echo=True)
# below is for mac
engine = create_engine("sqlite:////Users/ryanlee/Desktop/Repos/predagg/idpmodel/finaldata/main.db")

# of the proteins that have isoforms:
# for x-axis, i need to find the difference of scores between isoform and canonical:
# 2 ways are brought into mind. first way, we can find the average of all the scores
# of the canonical metapredict scores and compare it with the avergae we get form isoform.
# ^ this is he wrong way, because we're not considering e.g: we get like a sin wave of scores 
# for canonical, and a zero slope line. the average of both canonical and isoform scores would
# be zero.
# So the seond way is to find the difference of each score on each reside and find the absolute value and 
# add all those values up and we will use that number as a baseline to determine how different
# the scores will be from the canonical and isoform

# *** overall disorderedness

def finddiff(canon):
    canon_sequence:str = canon.sequence
    canon_score:list = meta.predict_disorder(canon_sequence)
    canon_avg_score:float = np.average(canon_score)
    # print(canon_avg_score)

    canon_isoforms:list = canon.isoforms
    isoform_sequences:list = [isoform.sequence for isoform in canon_isoforms]
    # iso_scores:list = [meta.predict_disorder(isoform_sequence) for isoform_sequence in isoform_sequences]
    iso_scores = []
    for isoform_sequence in isoform_sequences:
        try:
            iso_scores.append(meta.predict_disorder(isoform_sequence))
        except Exception as e:
            return None
    # iso_scores:list = np.array(iso_scores)
    # print(len(iso_scores))
    iso_avg_scores:list = [np.average(scores) for scores in iso_scores]
    # print(iso_avg_scores)
    # iso_avg_scores2:list = np.mean(iso_scores, axis=1)
    # print(iso_avg_scores2)
    # print(iso_avg_scores)

    total_diff:list = np.subtract(canon_avg_score, iso_avg_scores)
    # print(total_diff)

    return total_diff

with Session(engine) as session:
    # canon = session.query(Canon).get('P04637')
    # finddiff(canon)
    canon = session.query(Canon).all()
    masterlist = []
    for cnon in canon:
        if cnon.isoforms:
            masterlist.extend(finddiff(cnon))
            # print(masterlist)
            # print(finddiff(cnon))
    with open('difflist.txt', "w") as f:
        f.write(masterlist)



    # finding overall disorderedness differences between canonical and isoform
    # returns 
    # for iso_score in iso_scores:
    #     print(np.subtract(arr1, arr2))

    # arr1 = [1, 2, 3]
    # arr2 = 1
    # print(np.subtract(arr2, arr1))