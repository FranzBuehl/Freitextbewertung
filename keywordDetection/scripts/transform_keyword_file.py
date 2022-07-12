import json

# Opening JSON file
file = open("../assets/keywords_raw.json", encoding="utf-8")

# returns JSON object as
# a dictionary
data = json.load(file)
out = {}

def add_cases(keywords):
    """ Adds regex for lower and upper case at the beginning of every word
    Example:
        keywords = "This is an Example
        returns "[Tt]his [Ii]s [Aa]n [Ee]xample
    """
    workerString = keywords
    addedChars = 0
    for index in range(len(workerString)-1):
        char = workerString[index]
        wordStart = keywords[index+addedChars]
        upper = wordStart.upper()
        lower = wordStart.lower()
        if index == 0:
            keywords = "["+upper+lower+"]"+keywords[1:]
            addedChars += 4
        elif char in ["/", ",", " "]:
            keywords = keywords[0:index+addedChars]+"["+upper+lower+"]"+keywords[index+addedChars+1:]
            addedChars += 3
        index += 1
    return keywords

# Arbeitsanalyse & Arbeitsgestaltung
for competence in data:
   for gameParameter in data[competence]:
        name = competence + "/" + gameParameter
        keywords = data[competence][gameParameter]
        keywords = add_cases(keywords)
        pattern = 'r' +'"' + keywords.replace("*", "(\w+)?").replace("/", "|").replace(",", "|")+ '"'
        out[name] = pattern

with open("../assets/keywords.json", "w", encoding="utf-8") as file:
    json.dump(out, file, ensure_ascii=False, indent=4)

# Closing file
file.close()


