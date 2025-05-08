from collections import defaultdict

task_num = int(input('Задания:\n' \
                   '1. Сортировка массива по невозрастанию методом обменов слева направо с фиксированным числом проходов.\n' \
                   '2. Сортировка массива по невозрастанию методом обменов справа налево с минимальным числом проходов.\n' \
                   '3. Сортировка массива по неубыванию методом включения справа налево.\n' \
                   '4. Сортировка массива по невозрастанию методом извлечения минимального элемента, поиск слева направо.\n' \
                   '5. Слияние двух массивов, первый из которых упорядочен по невозрастанию, а второй — по неубыванию.\n' \
                   '6. Сортировка массива по неубыванию методом распределения по массиву ключей, упорядоченному по невозрастанию.\n' \
                   '7. Переставить строки матрицы по возрастанию количества отрицательных элементов.\n' \
                   'Выберите номер задания, которое необходимо решить: '))

match task_num:
    case 1:
        def exchange_sort_fixed_passes(arr, num_passes):
            """Сортировка массива по невозрастанию методом обменов слева направо с фиксированным числом проходов."""
            n = len(arr)
            for _ in range(num_passes):  # Выполняем фиксированное количество проходов
                for i in range(n - 1):  # Двигаемся слева направо
                    if arr[i] < arr[i + 1]:  # Обмен, если нарушен порядок
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        # Ввод количества проходов
        num_passes = int(input("Введите количество проходов сортировки: "))

        print("Исходный массив:", numbers)

        exchange_sort_fixed_passes(numbers, num_passes)
        print("Массив после сортировки:", numbers)

    case 2:
        def exchange_sort_variable_passes(arr):
            """Сортировка массива по невозрастанию методом обменов справа налево с минимальным числом проходов."""
            n = len(arr)
            swapped = True  # Флаг для отслеживания изменений

            while swapped:  # Продолжаем сортировку, пока есть перестановки
                swapped = False
                for i in range(n - 1, 0, -1):  # Двигаемся справа налево
                    if arr[i] > arr[i - 1]:  # Меняем элементы местами, если нарушен порядок
                        arr[i], arr[i - 1] = arr[i - 1], arr[i]
                        swapped = True  # Запоминаем, что был обмен

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        exchange_sort_variable_passes(numbers)
        print("Отсортированный массив:", numbers)

    case 3:
        def insertion_sort_right_to_left(arr):
            """Сортировка массива по неубыванию методом включения справа налево."""
            n = len(arr)
            for i in range(n - 2, -1, -1):  # Двигаемся справа налево
                key = arr[i]  # Запоминаем включаемый элемент
                j = i + 1

                # Перемещаем элементы, чтобы вставить key на нужное место
                while j < n and arr[j] < key:
                    arr[j - 1] = arr[j]
                    j += 1
        
                arr[j - 1] = key  # Вставляем key на правильную позицию

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        insertion_sort_right_to_left(numbers)
        print("Отсортированный массив:", numbers)

    case 4:
        def selection_sort_desc_min(arr):
            """Сортировка массива по невозрастанию методом извлечения минимального элемента, поиск слева направо."""
            n = len(arr)
            for i in range(n - 1):
                min_index = i  # Считаем текущий элемент минимальным
                for j in range(i + 1, n):  # Ищем минимальный элемент слева направо
                    if arr[j] < arr[min_index]:
                        min_index = j
                arr[min_index], arr[n - i - 1] = arr[n - i - 1], arr[min_index]  # Меняем минимальный элемент с последним неотсортированным

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        selection_sort_desc_min(numbers)
        print("Отсортированный массив:", numbers)

    case 5:
        def merge_descending(arr1, arr2):
            """Слияние двух массивов, первый из которых упорядочен по невозрастанию, а второй — по неубыванию."""
            merged = []
            i, j = 0, len(arr2) - 1  # Двигаемся в первом массиве слева направо, во втором — справа налево

            while i < len(arr1) and j >= 0:
                if arr1[i] >= arr2[j]:
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j -= 1

            # Добавляем оставшиеся элементы (если что-то осталось)
            while i < len(arr1):
                merged.append(arr1[i])
                i += 1

            while j >= 0:
                merged.append(arr2[j])
                j -= 1

            return merged

        # Ввод массивов от пользователя
        arr1 = list(map(int, input("Введите первый массив (упорядоченный по невозрастанию) через пробел: ").split()))
        arr2 = list(map(int, input("Введите второй массив (упорядоченный по неубыванию) через пробел: ").split()))

        print("Первый массив:", arr1)
        print("Второй массив:", arr2)

        merged_array = merge_descending(arr1, arr2)
        print("Объединённый массив (по невозрастанию):", merged_array)

    case 6:
        def distribution_sort_ascending(arr):
            """Сортировка массива по неубыванию методом распределения по массиву ключей, упорядоченному по невозрастанию."""
            if not arr:
                return arr

            # Создаем словарь для хранения элементов по их ключам
            key_dict = defaultdict(list)

            # Заполняем словарь: группируем элементы по значению ключа
            for num in arr:
                key_dict[num].append(num)

            # Сортируем ключи по невозрастанию
            sorted_keys = sorted(key_dict.keys(), reverse=True)

            # Собираем элементы обратно в отсортированный массив (по неубыванию)
            sorted_arr = []
            for key in reversed(sorted_keys):  # Переворачиваем ключи, чтобы получить неубывающий порядок
                sorted_arr.extend(key_dict[key])  # Добавляем элементы из групп

            return sorted_arr

        # Ввод массива от пользователя
        numbers = list(map(int, input("Введите числа через пробел: ").split()))

        print("Исходный массив:", numbers)

        sorted_numbers = distribution_sort_ascending(numbers)
        print("Отсортированный массив (по неубыванию):", sorted_numbers)

    case 7:
        def sort_rows_by_negative_count(matrix):
            """Переставляет строки матрицы по возрастанию количества отрицательных элементов с помощью сортировки вручную."""
            # Вычисляем количество отрицательных элементов в каждой строке
            row_counts = [(row, sum(1 for num in row if num < 0)) for row in matrix]

            # Реализация сортировки (методом выбора)
            n = len(row_counts)
            for i in range(n):
                min_index = i
                for j in range(i + 1, n):
                    if row_counts[j][1] < row_counts[min_index][1]:
                        min_index = j
                row_counts[i], row_counts[min_index] = row_counts[min_index], row_counts[i]

            # Возвращаем отсортированную матрицу
            sorted_matrix = [row for row, _ in row_counts]
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

        sorted_matrix = sort_rows_by_negative_count(matrix)

        print("Матрица после сортировки строк:")
        for row in sorted_matrix:
            print(row)
