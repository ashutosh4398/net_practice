data = {
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"],
                    },
                    "GlossSee": "markup",
                }
            },
            "scores": [1, 2, 3],
        },
    }
}


def flatten(data, source=""):
    if isinstance(data, dict):
        temp = {}
        for k, v in data.items():
            new_source = (source + "_" + k) if source else k
            if isinstance(v, (dict, list)):
                resp = flatten(v, new_source)
                if isinstance(resp, dict):
                    temp.update(resp)
                else:
                    temp[new_source] = resp
            else:
                temp[new_source] = v
        return temp
    elif isinstance(data, list):
        temp = {}
        for i, each in enumerate(data):
            temp[source + "_" + str(i)] = each
        return temp
    return data


x = flatten(data)
