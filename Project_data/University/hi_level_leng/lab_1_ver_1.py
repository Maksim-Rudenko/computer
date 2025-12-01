import tkinter as tk
import time

# Функция загрузки
def splash_screen():
    splash = tk.Tk()
    splash.title("Запуск приложения")
    splash.geometry("300x150")
    
    label = tk.Label(splash, text="Ефименко Милана Владимировна ЗИТ-21\n Лабораторная работа 1\nЗапуск приложения...", font=("Arial", 12))
    label.pack(expand=True)

    splash.update()
    
    # Симуляция процесса загрузки
    for i in range(1, 101, 10):
        label.config(text=f"Ефименко Милана Викторовна ЗИТ-21\n Лабораторная работа 1\nЗагрузка... {i}%")
        splash.update()
        time.sleep(0.3)  # Задержка для имитации загрузки

    splash.destroy()  # Закрываем заставку после загрузки

# Основное окно
def main_window():
    root = tk.Tk()
    root.title("Ефименко Милана Викторовна")
    root.geometry("400x200")

    label = tk.Label(root, text="Окно загружено", font=("Arial", 16))
    label.pack(expand=True)

    root.mainloop()

# Запуск приложения
splash_screen()  # Показываем заставку
main_window()  # Открываем основное окно