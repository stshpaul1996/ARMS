# Input: [“baseball”, “b,bas,ba,all,base,seb,ball”] 

# Output: base,ball 

# Split the first input based on the longest possibility match in second input 


ip = ['baseball','b,bas,ba,all,base,seb,ball']

compare_list = ip[1].split(",")
base = ip[0]
output_list = []
for i in range(len(base)):
    if base[:i] in compare_list:
        output_list.append(base[:i])
max_str = len(output_list[-1])
output = base[:max_str] + "," + base[max_str:]
print(output)