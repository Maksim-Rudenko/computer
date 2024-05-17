def format_text_2(text):    
    formatted_text = []
    current_line = ''
    
    words = []
    current_word = ""
    for char in text:    
        if char == ',':
            words.append(current_word + ',')
            current_word = ""    
        elif char == ' ':
            words.append(current_word)
            current_word = ""    
        else:
            current_word += char

    words.append(current_word)
       
    words = [word for word in words if word != '']    

    i = 0
    words_new = []
    while i < len(words):
        if i + 1 < len(words) and words[i + 1] == ',':
            words_new.append(words[i] + words[i + 1])
            i += 2
        else:
            words_new.append(words[i])
            i += 1

    #print(words_new)
    max_len = max(len(word) for word in words_new) * 3
    #print(max_len)

        
    for word in words_new:
        if len(current_line) + len(word) <= max_len:
            current_line += word + (' ' if (word != words[-1]) else '')
        else:
            formatted_text.append(current_line.rstrip())            
            current_line = word + (' ' if (word != words[-1]) else '')
    if current_line:
        formatted_text.append(current_line.rstrip())
    return '\n'.join(formatted_text)

text = input()
print(format_text_2(text))

#+ (1 if word != words[-1] else 0)