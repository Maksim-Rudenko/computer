len_text = int(input())
text = input()
text_list = list(text)
res = []

for i in range(len_text):
    text_list_copy = text_list.copy()
    check_list = []
    check_list.append(text_list_copy[i])
    

    for command in ['L', 'R', 'F']:
        result = 0
        position = 1   
        if command not in check_list:
            text_list_copy[i] = command
            check_list.append(text_list_copy[i]) 

            #print(text_list_copy)            

            for letter in text_list_copy:    
                if letter == 'L':
                    position = -1
                if letter == 'R':
                    position = 1
                if letter == 'F':
                    result += position
            res.append(result)
            #print(result)
            

print(len(set(res)))