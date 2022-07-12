import json

# Opening JSON file
file = open('../assets/generated_output.jsonl', encoding='utf-8')

# returns JSON object as
# a dictionary
data = json.load(file)

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

with open('../assets/generated_data-fixed.jsonl', 'w', encoding='utf-8') as file:
    json.dump(out, file, ensure_ascii=False, indent=4)

# Closing file
file.close()

