def min_districts_for_victory(districts, n):
    """
    Возвращает минимальное количество районов, которые должен посетить Борис, чтобы победить на выборах.

    Args:
        districts (list): Список из кортежей (поддержка Андрея, поддержка Бориса) для каждого района.
        n (int): Общее количество районов.

    Returns:
        int: Минимальное количество районов для победы.
    """

    # Отсортировать районы по убыванию поддержки Бориса
    districts.sort(key=lambda x: x[1], reverse=True)

    # Инициализировать счетчик поддержки
    boris_support = 0
    andrey_support = 0

    # Перебирать районы
    for district in districts:
        # Если Борис посещает район, то все жители голосуют за него
        if district[1] > 0:
            boris_support += district[0] + district[1]
        # Иначе голосуют за Андрея или не голосуют
        else:
            andrey_support += district[0]

    # Если Борис уже победил, то возвращаем 0
    if boris_support > andrey_support:
        return 0

    # Иначе увеличиваем поддержку Бориса, пока он не победит
    visited_districts = 0
    while boris_support <= andrey_support:
        visited_districts += 1
        boris_support += districts[visited_districts - 1][1]

    # Возвращаем количество посещенных районов
    return visited_districts

num_regions = int(input())

districts = []

for i in range(num_regions):
    input_str = input()
    a, b = input_str.split()    
    districts.append((int(a), int(b)))

print(min_districts_for_victory(districts, num_regions))