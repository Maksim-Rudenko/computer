from collections import defaultdict

method = int(input('Выберите необходимое задание:\n' \
                   '1. Отсортировать массив по невозрастанию методом обменов рядом стоящих элементов с фиксированным числом просмотров\n' \
                   '2. Отсортировать массив по невозрастанию методом обменов рядом стоящих элементов с минимально необходимым (переменным) числом просмотров\n' \
                   '3. Отсортировать массив по неубыванию методом включения с выбором включаемого элемента\n' \
                   '4. Отсортировать массив по невозрастанию методом извлечения максимального элемента\n' \
                   '5. Получить упорядоченный по неубыванию массив методом слияния двух упорядоченных по неубыванию массивов\n' \
                   '6. Отсортировать массив по невозрастанию методом распределения по массиву ключей, упорядоченному по невозрастанию\n' \
                   '7. В матрице МхN переставить столбцы таким образом, чтобы получилась последовательность C1 >= C2 >=...>= CN\n' \
                   'Выбор (номер): '))

match method:
    case 1:
        def exchange_sort(arr, num_passes):
            """Сортирует массив по невозрастанию методом обменов с фиксированным числом проходов справа налево."""
            n = len(arr)
            for _ in range(num_passes):  # Выполняем фиксированное количество проходов
                for j in range(n - 1, 0, -1):  # Двигаемся справа налево
                    if arr[j] > arr[j - 1]:  # Обмен элементов, если они нарушают порядок
                        arr[j], arr[j - 1] = arr[j - 1], arr[j]

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        # Ввод количества проходов
        num_passes = int(input("Введите количество проходов сортировки: "))

        print("Исходный массив:", numbers)

        exchange_sort(numbers, num_passes)
        print("Массив после сортировки:", numbers)

    case 2:
        def optimized_exchange_sort(arr):
            """Сортировка массива по невозрастанию методом обменов с переменным числом проходов слева направо."""
            n = len(arr)
            swapped = True  # Флаг, показывающий, были ли перестановки

            while swapped:  # Продолжаем, пока есть обмены
                swapped = False
                for i in range(n - 1):
                    if arr[i] < arr[i + 1]:  # Обмен, если элементы не упорядочены
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True  # Запоминаем, что был обмен

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        optimized_exchange_sort(numbers)
        print("Отсортированный массив:", numbers)

    case 3:
        def insertion_sort_left_to_right(arr):
            """Сортировка массива по неубыванию методом включения слева направо."""
            n = len(arr)
            for i in range(1, n):  # Начинаем со второго элемента
                key = arr[i]  # Запоминаем включаемый элемент
                j = i - 1

                # Перемещаем элементы, чтобы вставить key на нужное место
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1

                arr[j + 1] = key  # Вставляем key на правильную позицию

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        insertion_sort_left_to_right(numbers)
        print("Отсортированный массив:", numbers)

    case 4:
        def selection_sort_desc(arr):
            """Сортировка массива по невозрастанию методом извлечения максимального элемента слева направо."""
            n = len(arr)
            for i in range(n):
                max_index = i  # Предполагаем, что первый элемент текущего подмассива максимальный
                for j in range(i + 1, n):  # Ищем максимальный элемент слева направо
                    if arr[j] > arr[max_index]:
                        max_index = j
                arr[i], arr[max_index] = arr[max_index], arr[i]  # Меняем местами найденный максимум и текущий элемент

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        selection_sort_desc(numbers)
        print("Отсортированный массив:", numbers)

    case 5:
        def merge_sorted_arrays(arr1, arr2):
            """Слияние двух упорядоченных по неубыванию массивов в один."""
            merged = []
            i, j = 0, 0

            # Объединяем два массива, сравнивая элементы
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1

            # Добавляем оставшиеся элементы из первого массива (если есть)
            while i < len(arr1):
                merged.append(arr1[i])
                i += 1

            # Добавляем оставшиеся элементы из второго массива (если есть)
            while j < len(arr2):
                merged.append(arr2[j])
                j += 1

            return merged

        # Ввод массивов от пользователя
        arr1 = list(map(int, input("Введите первый упорядоченный массив через пробел: ").split()))
        arr2 = list(map(int, input("Введите второй упорядоченный массив через пробел: ").split()))

        print("Первый массив:", arr1)
        print("Второй массив:", arr2)

        merged_array = merge_sorted_arrays(arr1, arr2)
        print("Объединённый массив:", merged_array)

    case 6:
        def distribution_sort_desc(arr):
            """Сортировка массива по невозрастанию методом распределения по массиву ключей."""
            if not arr:
                return arr

            # Создаем словарь для хранения элементов по их ключам
            key_dict = defaultdict(list)

            # Заполняем словарь: группируем элементы по значению ключа
            for num in arr:
                key_dict[num].append(num)

            # Сортируем ключи методом выбора
            keys = list(key_dict.keys())
            for i in range(len(keys)):
                max_index = i
                for j in range(i + 1, len(keys)):
                    if keys[j] > keys[max_index]:  # Выбираем максимальный ключ
                        max_index = j
                keys[i], keys[max_index] = keys[max_index], keys[i]  # Перемещаем максимальный ключ в начало

            # Собираем элементы обратно в отсортированный массив
            sorted_arr = []
            for key in keys:
                sorted_arr.extend(key_dict[key])  # Добавляем элементы из групп

            return sorted_arr

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        sorted_numbers = distribution_sort_desc(numbers)
        print("Отсортированный массив:", sorted_numbers)

    case 7:
        def sort_columns_by_abs_sum(matrix):
            """Переставляет столбцы матрицы по невозрастанию суммы абсолютных значений элементов."""
            rows, cols = len(matrix), len(matrix[0])

            # Вычисляем сумму абсолютных значений для каждого столбца
            column_sums = [(j, sum(abs(matrix[i][j]) for i in range(rows))) for j in range(cols)]

            # Сортируем индексы столбцов по убыванию сумм            
            for i in range(len(column_sums)):
                max_index = i
                for j in range(i + 1, len(column_sums)):
                    if column_sums[j][1] > column_sums[max_index][1]:
                        max_index = j
                column_sums[i], column_sums[max_index] = column_sums[max_index], column_sums[i]

            # Переставляем столбцы по отсортированному порядку
            sorted_matrix = [[matrix[i][j] for j, _ in column_sums] for i in range(rows)]
    
            return sorted_matrix

        # Ввод матрицы от пользователя
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))

        matrix = []
        print("Введите элементы матрицы построчно:")
        for _ in range(rows):
            row = list(map(int, input().split()))
            matrix.append(row)

        print("Исходная матрица:")
        for row in matrix:
            print(row)

        sorted_matrix = sort_columns_by_abs_sum(matrix)

        print("Матрица после сортировки столбцов:")
        for row in sorted_matrix:
            print(row)
