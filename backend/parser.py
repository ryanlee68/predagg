def fromseq(seq):
    return seq

def identifier(json):
    if json['uniprotid']:
        return json['uniprotid']
    elif json['sequence']:
        return fromseq(json['sequence'])
    else:
        return None