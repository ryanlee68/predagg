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
                binaries.append(1)
            else:
                binaries.append(0)
        returnarray.append(binaries)
        return returnarray
    pass

def get_df(uniprotid, predictors):
    print(uniprotid)
    print(predictors)
    URL = f"https://mobidb.org/api/download?acc={uniprotid}&format=json"
    response = requests.get(URL)
    jsonresp = response.json()
    # print(jsonresp)
    # with open("myfile.txt", "w") as f:
    #     f.write(json.dumps(jsonresp))

    proteinname = jsonresp['name']
    print(proteinname)
    sequence = jsonresp['sequence']
    print(sequence)
    length = jsonresp['length']
    print(length)

    headers = {"Protein Name": [proteinname],
        "UniProtID": [uniprotid],
        "Sequence": [sequence],
        "Length": length,
        }

    df = pd.DataFrame(data=headers)

    predcol = []
    for predictor in predictors:
        predcol.append(predict(uniprotid, predictor, predictors[predictor]))

    df2 = df.reindex(df.columns.tolist() + list(predictors.keys()),index=1)
    print(df)