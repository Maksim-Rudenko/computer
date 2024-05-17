num_people = int(input())

dolg = []

for i in range(num_people):
    input_str = input()
    a, b = input_str.split()    
    dolg.append((int(a), int(b)))

sum_dolg_for_whom = {str(i + 1): 0 for i in range(num_people)}
sum_dolg_for_me = {str(i + 1): 0 for i in range(num_people)}


for i in range(num_people):
    if str(dolg[i][0]) not in sum_dolg_for_me:
        sum_dolg_for_me[str(dolg[i][0])] = dolg[i][1]
    else:
        sum_dolg_for_me[str(dolg[i][0])] += dolg[i][1]
    
    sum_dolg_for_whom[str(i + 1)] = dolg[i][1]

result = 0

for i in range(num_people):
    result += max(0, sum_dolg_for_me[str(i + 1)] - sum_dolg_for_whom[str(i + 1)])
print(result)

