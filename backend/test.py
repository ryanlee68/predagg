from iupred3 import iupred3_lib as ip3

seq = ip3.iupred('MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD')

print(len(seq[0]))


# csrftoken=3wxnuG7ZZTOASsNKz4Neo1CKfvPyye5Ovmv5pqmfrVVEXeCS2a7vuF3LLZPVk55f; expires=Thu, 26-Oct-2023 20:19:52 GMT; Max-Age=31449600; Path=/
# import metapredict as meta

# sequence = "MDLWQLLLTLALAGSSDAFSGSEATAAILSRAPWSLQSVNPGLKTNSSKEPKFTKCRSPERETFSCHWTDEVHHGTKNLGPIQLFYTRRNTQEWTQEWKECPDYVSAGENSCYFNSSFTSIWIPYCIKLTSNGGTVDEKCFSVDEIVQPDPPIALNWTLLNVSLTGIHADIQVRWEAPRNADIQKGWMVLEYELQYKEVNETKWKMMDPILTTSVPVYSLKVDKEYEVRVRSKQRNSGNYGEFSEVLYVTLPQMSQFTCEEDFYFPWLLIIIFGIFGLTVMLFVFLFSKQQRIKMLILPPVPVPKIKGIDPDLLKEGKLEEVNTILAIHDSYKPEFHSDDSWVEFIELDIDEPDEKTEESDTDRLLSSDHEKSHSNLGVKDGDSGRTSCCEPDILETDFNANDIHEGTSEVAQPQRLKGEADLLCLDQKNQNNSPYHDACPATQQPSVIQAEKNKPQPLPTEGAESTHQAAHIQLSNPSSLSNIDFYAQVSDITPAGSVVLSPGQKNKAGMSQCDMHPEMVSLCQENFLMDNAYFCEADAKKCIPVAPHIKVESHIQPSLNQEDIYITTESLTTAAGRPGTGEHVPGSEMPVPDYTSIHIVQSPQGLILNATALPLPDKEFLSSCGYVSTDQLNKIMP"

# results = meta.predict_disorder_domains(sequence)
# Available dot variables are:
#   .sequence
#   .disorder
#   .disordered_domain_boundaries
#   .folded_domain_boundaries
#   .disordered_domains
#   .folded_domains
# print(results.disorder[1])
# print(results.disordered_domain_boundaries)
# print(results.disordered_domains)

# import requests
# from pprint import pprint
# import numpy as np
# import json
# import pandas as pd

# uniprotid = 'P04637'
# predictors = {
    
# }

# URL = f"https://mobidb.org/api/download?acc={uniprotid}&format=json"
# response = requests.get(URL)
# jsonresp = response.json()
# # print(jsonresp)
# with open("myfile.txt", "w") as f:
#     f.write(json.dumps(jsonresp))

# proteinname = jsonresp['name']
# print(proteinname)
# sequence = jsonresp['sequence']
# print(sequence)
# length = jsonresp['length']
# print(length)

# headers = {"Protein Name": [proteinname],
#     "UniProtID": [uniprotid],
#     "Sequence": [sequence],
#     "Length": length,
#     }

# df = pd.DataFrame(data=headers)
# df2 = df.reindex(df.columns.tolist() + list(predictors.keys()),index=1)
# print(df)

# # open("instagram.ico", "wb").write(response.content)