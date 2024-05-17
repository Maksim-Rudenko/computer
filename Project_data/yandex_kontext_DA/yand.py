"""
В одном городе проходят выборы нового мэра, всего есть два кандидата: Андрей и Борис. Город этот небольшой и в нем есть 
N
N районов.

Для каждого района известно, сколько человек поддерживает Андрея и Бориса. Борис очень сильно желает победить, поэтому он собирается произнести в некоторых районах речь. Если в 
i
i-м районе Борис произносит речь, то все жители этого района голосуют за Бориса. В противном случае, жители, которые поддерживают Андрея, голосуют за него, а остальные избиратели расстраиваются и не голосуют.

В выборах побеждает кандидат, набравший строго большее число голосов, чем его соперник.

Само собой, Борис очень занятой человек, поэтому хочет посетить минимальное число районов для победы на выборах. Вы, как его помощник, должны вычислить это количество.
"""
def custom_key(person):
    return person[0]


def min_districts_to_win(districts):
    districts.sort(key=custom_key, reverse=True)    
    districts.sort(key=lambda x: x[0] + x[1], reverse=True)
        
    andrei_votes = sum(district[0] for district in districts)
     
    result = 0

    boris_votes = 0

    for i in range(len(districts)):
        boris_votes += sum(districts[i])
        andrei_votes -= districts[i][0]
        result += 1
        if boris_votes > andrei_votes:           
            break             

    return result

num_regions = int(input())

districts = []

for i in range(num_regions):
    input_str = input()
    a, b = input_str.split()    
    districts.append((int(a), int(b)))

print(min_districts_to_win(districts))

