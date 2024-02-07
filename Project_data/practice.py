'''sentence = 'I like to Have this message have? on my computer'

tags_list = ['like', 'want', 'have', 'do']

def get_tags(sentence):
    result = []
    for word in sentence.split(' '):
        if word.lower() in tags_list:
            result.append(word)

    return result
print(get_tags(sentence))'''