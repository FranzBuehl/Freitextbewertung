import json

# Opening JSON file
f = open('output/train/output.jsonl')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
count = 0
out = data
for i in data:
    c = i[1]
    i[1]=i[0]
    i[0]=c
    count2=0
    print(i)
    for ent in i[1]['entities']:
       # print(ent)
        x = ent[0]
        ent[0] = ent[2]#data2[count]['entities'][count2]['start-index']
        ent[2] = ent[1]
        ent[1] = x #data2[count]['entities'][count2]['end-index']
        print(ent)
        #count2 +=1

    out[count]= i

    count += 1

with open('output2/train/output-fixed.jsonl', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=4)

# Closing file
f.close()

