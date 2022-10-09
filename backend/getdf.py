import requests
from pprint import pprint
import numpy as np
import json
import pandas as pd

def predict(uniprotid, predictor, prvalue):
    returnarray = []
    if predictor == "IUPred3":
        binaries = []
        URL = f"https://iupred3.elte.hu/iupred3/{uniprotid}.json"
        response = requests.get(URL)
        jsonresp = response.json()
        minscore = float(prvalue[1])*.01
        values = jsonresp['iupred2']
        returnarray.append(values)
        for num in values:
            if num >= minscore:
                binaries.append(True)
            else:
                binaries.append(False)
        returnarray.append(binaries)
        # print(str(returnarray) + "fdsf")
        return returnarray
    # add other predictors here
    pass

def get_df(uniprotid, predictors):
    # print(uniprotid)
    # print(predictors)
    URL = f"https://mobidb.org/api/download?acc={uniprotid}&format=json"
    response = requests.get(URL)
    jsonresp = response.json()
    # print(jsonresp)
    # with open("myfile.txt", "w") as f:
    #     f.write(json.dumps(jsonresp))

    proteinname = jsonresp['name']
    # print(proteinname)
    sequence = [*jsonresp['sequence']]
    # print(sequence)
    # print(sequence)
    length = jsonresp['length']
    # print(length)
    organism = jsonresp['organism']
    # print(organism)
    headers = {"Protein Name": proteinname,
        "Organism": organism,
        "UniProtID": uniprotid,
        "Sequence": pd.Series(sequence),
        "Length": length,
        }

    df = pd.DataFrame(data=headers)

    # predcol = []
    # print(df)
    # for predictor in predictors:
    #     predcol.append(predict(uniprotid, predictor, predictors[predictor]))

    for predictor in predictors:
        # print(predict(uniprotid, predictor, predictors[predictor])[0])
        # print(predict(uniprotid, predictor, predictors[predictor])[1])
        df[str(predictor)] = pd.Series(predict(uniprotid, predictor, predictors[predictor])[0])
        df[str(predictor) + " Scores with >=0." + predictors[predictor][1]] = pd.Series(predict(uniprotid, predictor, predictors[predictor])[1])

    # print(predcol)
    # df2 = df.reindex(df.columns.tolist() + list(predictors.keys()),index=1)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #     print(df)


    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 150)
    print(df)