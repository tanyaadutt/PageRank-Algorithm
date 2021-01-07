import operator
with open('web-Google.txt','r') as input_file:
    data = [x.split() for x in input_file.read().splitlines()]
    
data = data[4:]

nodes = []
from_nodes = []
text = ""
nodes_dict = {}
for line in data:
    nodes.append(int(line[0]))
    from_nodes.append(int(line[0]))
    nodes.append(int(line[1]))
    nodes_dict[int(line[0])] = []

nodes = list(set(nodes))
from_nodes = list(set(from_nodes))
s = str(max(nodes) + 1)

for line in data:
    if line[1:] == []:
        nodes_dict[int(line[0])] = [] 
    else:
        nodes_dict[int(line[0])].append(int(line[1:][0]))

for x in nodes_dict:
    if nodes_dict[x] == []:
        print(x,nodes_dict[x])

text = ""
for x in nodes_dict.keys():
    for y in nodes_dict[x]:
        text += str(str(y)+" "+str(x)+" "+str(1/len(nodes_dict[x])) +"\n")

M = open("M.txt","w")
M.write(str(s+" "+s+"\n"))
M.write(text)
M.close()

initial_pagerank = str(1/len(nodes))

pg_ = ""
for x in nodes:
    pg_ += str(str(x)+" "+initial_pagerank+"\n")
v = open("v.txt","w")
v.write(str(s+" "+str(1)+"\n"))
v.write(pg_)
v.close()

n = open("nodes.txt","w")
for x in nodes:
    n.write(str(x)+ " ")
n.close()