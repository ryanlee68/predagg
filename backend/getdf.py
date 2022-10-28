import requests
from pprint import pprint
import numpy as np
import json
import pandas as pd
import metapredict as meta
from iupred3 import iupred3_lib as ip3
# from symbol import pass_stmt

def binaries(array, minscore):
    binarray = []
    for i in array:
        if i >= minscore:
            binarray.append(True)
        else:
            binarray.append(False)
    return binarray

def predict_uniprot(uniprotid, sequence, predictor, prvalue=None):
    returnarray = []
    minscore = float(prvalue[1])*.01
    if predictor == "IUPred3":
        URL = f"https://iupred3.elte.hu/iupred3/{uniprotid}.json"
        response = requests.get(URL)
        jsonresp = response.json()
        values = jsonresp['iupred2']
        returnarray.append(values)
        returnarray.append(binaries(values, minscore))
        # print(str(returnarray) + "fdsf")
    elif predictor == "Metapredict":
        metaArray = meta.predict_disorder_domains(sequence).disorder
        returnarray.append(metaArray)
        returnarray.append(binaries(metaArray, minscore))
        # print(str(returnarray) + "fdsf")

def predict_seq(sequence, predictor, prvalue=None):
    # returnarrya is an array that contains two arrays:
    # the first array contains the prediction confidence values for each residue
    # the second array contains binary true/false values based on the minscore that the user provided
    returnarray = []
    minscore = float(prvalue[1])*.01
    if predictor == "IUPred3":
        iupredresp = ip3.iupred(sequence)[0]
        returnarray.append(iupredresp)
        returnarray.append(binaries(iupredresp, minscore))
    if predictor == 'Metapredict':
        metaArray = meta.predict_disorder_domains(sequence).disorder
        returnarray.append(metaArray)
        returnarray.append(binaries(metaArray, minscore))

    return returnarray

    # add other predictors here
    pass

def get_df(user_predictors, uniprotid=None, sequence=None):
    strSequence = ''
    if uniprotid:

        # print(uniprotid)
        print("User Predictors: "+str(user_predictors))
        URL = f"https://mobidb.org/api/download?acc={uniprotid}&format=json"
        response = requests.get(URL)
        jsonresp = response.json()
        # print(jsonresp)
        # with open("myfile.txt", "w") as f:
        #     f.write(json.dumps(jsonresp))

        proteinname = jsonresp['name']
        # print(proteinname)
        # strSequence is used as a parameter for metapredict
        strSequence = jsonresp['sequence']
        sequenceCol = [*strSequence]
        # print(sequence)
        # print(sequence)
        length = jsonresp['length']
        # print(length)
        organism = jsonresp['organism']
        # print(organism)
    else:
        proteinname = 'Unknonwn'
        organism = 'Unknown'
        uniprotid = 'Unknown'
        print(sequence)
        length = len(sequence)
        sequenceCol = [*sequence]
    headers = {"Protein Name": proteinname,
        "Organism": organism,
        "UniProtID": uniprotid,
        "Length": length,
        "Sequence": pd.Series(sequenceCol),
        }

    df = pd.DataFrame(data=headers)

    # predcol = []
    # print(df)
    # for predictor in predictors:
    #     predcol.append(predict(uniprotid, predictor, predictors[predictor]))

    for predictor in user_predictors:
        print(predictor)
        # print(predict(uniprotid, predictor, predictors[predictor])[0])
        # print(predict(uniprotid, predictor, predictors[predictor])[1])
        print(uniprotid)
        if uniprotid != 'Unknown':
            print('uniprotid is invoked')
            predictor_results = predict_uniprot(uniprotid, strSequence, predictor, prvalue=user_predictors[predictor])
        else:
            predictor_results = predict_seq(sequence, predictor, prvalue=user_predictors[predictor])
        df[str(predictor)] = pd.Series(predictor_results[0])
        df[str(predictor) + " Scores with >=0." + user_predictors[predictor][1]] = pd.Series(predictor_results[1])

    # print(predcol)
    # df2 = df.reindex(df.columns.tolist() + list(predictors.keys()),index=1)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(df)


    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 150)
    print(df)