def clean_apartment(N, M, x, y, grid):
    visited = [[0] * M for _ in range(N)]  # Массив для отслеживания очищенных клеток
    total_time = 0
    cleaned_cells = 0

    def dfs(i, j):
        nonlocal total_time, cleaned_cells
        # Проверка границ и условий
        if i < 0 or i >= N or j < 0 or j >= M:
            return
        if grid[i][j] == 1 or visited[i][j] == 1:
            return
        
        # Помечаем клетку как посещенную
        visited[i][j] = 1
        cleaned_cells += 1
        total_time += y  # Время на очистку

        # Перемещение к соседним клеткам
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            total_time += x  # Время на перемещение
            dfs(i + di, j + dj)

    # Начинаем с первой клетки (0, 0)
    dfs(0, 0)

    return total_time, cleaned_cells

# Пример использования
if __name__ == "__main__":
    # Ввод данных
    N, M, x, y = map(int, input().split())
    grid = []    
    for _ in range(M):
        row = list(map(int, input().split()))
        grid.append(row)

    total_time, cleaned_cells = clean_apartment(N, M, x, y, grid)
    print(f"Общее время: {total_time} секунд")
    print(f"Количество очищенных клеток: {cleaned_cells}")