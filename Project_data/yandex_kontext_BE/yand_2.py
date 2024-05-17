input_str = input()
N, Q = input_str.split()
N = int(N)
Q = int(Q)

dictionary = []

for i in range(N):
    dictionary.append(input())

dict_find_keys = []
dict_find_place = []

for i in range(Q):
    input_str = input()
    k, p = input_str.split()
    k = int(k)
    dict_find_keys.append(p)
    dict_find_place.append(k)


for word in dictionary:
    for key in 













for key in range(len(dict_find_keys)):
    i = 0
    j = 0
    for word in dictionary:
        i += 1
        if word.startswith(dict_find_keys[key]):
            j += 1        
            if j == dict_find_place[key]:
                print(i)
    if j < dict_find_place[key]:
        print(-1)



#print(dictionary)
#print(dict_find)