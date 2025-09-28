nums=[7,7]
k = 1

hashmap = {}
return_list = []
for values in nums:
    if values not in hashmap:
        hashmap[values] = 1
    else:
        hashmap[values] += 1
hashmap = sorted(hashmap.items(), key=lambda values:values[1], reverse=True)

for i in range(len(hashmap)): 
    if i < k:
        return_list.append(hashmap[i][0])
    else:
        print(return_list)

print(return_list)

            


        