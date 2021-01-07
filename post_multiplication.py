with open('multiplication_result.txt','r') as input_file:
    temp_result = [x.split() for x in input_file.read().splitlines()]

with open('v.txt','r') as input_file:
    temp_v = [x.split() for x in input_file.read().splitlines()]
    shape = temp_v[0]
    temp_v = temp_v[1:]

with open('nodes.txt','r') as input_file:
    nodes = [x.split() for x in input_file.read().splitlines()]
    nodes = nodes[0]

temp_v_dict = {}
temp_result_dict = {}

for x in temp_v:
    temp_v_dict[int(x[0])] = float(x[1])

for x in temp_result:
    temp_result_dict[int(x[0])] = float(x[1])

v = {}
result = {}
for x in nodes:
    x = int(x)
    if x in temp_v_dict.keys():
        v[x] = temp_v_dict[x]
    else:
        v[x] = 0
        
for x in nodes:
    x = int(x)
    if x in temp_result_dict.keys():
        result[x] = temp_result_dict[x]
    else:
        result[x] = 0

new_v = {}
n = len(v)
beta = 0.85
change = (1-beta)*(1/n)
for x in result.keys():
    value = (result[x]*beta) + change
    new_v[x] = value


flag = 0
for x in v.keys():
    difference = v[x] - new_v[x]
    if difference > 8.5e-7:
        print("different at:",x, " difference: ", difference)
        flag = 1
        break

if flag == 1:
    wv = open('old_v.txt','w')
    for x in v.keys():
        wv.write(str(x)+" "+str(v[x])+"\n")
    wv.close()

    wv = open('v.txt','w')
    wv.write(shape[0]+" "+shape[1]+"\n" )
    for x in new_v.keys():
        wv.write(str(x)+" "+str(new_v[x])+"\n")
    wv.close()
else:
    wv = open('all_pageranks.txt','w')
    for x in new_v.keys():
        wv.write(str(x)+" "+str(new_v[x])+"\n")
    wv.close()
    
    sorted_res = {k: v for k, v in sorted(new_v.items(), key=lambda item: item[1], reverse = True)} 
    k = list(sorted_res.keys())
    k = k[:10]
    wv = open('top_ten_pageranks.txt','w')
    for i in k:
        wv.write(str(i)+" "+str(sorted_res[i])+"\n")
    wv.close()  
