import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk  # Для работы с изображениями

# Основное окно приложения
root = tk.Tk()
root.title("Ефименко Милана Викторовна ЗИТ-21")  # Заголовок окна
root.geometry("400x400+500+600")  # Размер 400x400, положение 500x600

# Надпись "Привет"
label = tk.Label(root, text="Ефименко Милана Викторовна ЗИТ-21\n Лабораторная работа 2", font=("Arial", 20))
label.pack(pady=20)

# Функция для модального окна (параллелограмм с изображением)
def open_parallelogram():
    win = Toplevel(root)
    win.title("Ефименко Милана Викторовна")
    win.geometry("400x300+400+300")
    win.attributes('-alpha', 0.4)  # Устанавливаем прозрачность 40%

    # Загружаем изображение из папки с программой
    image_path = r'E:\Сухого\city.jpeg'  # Задний фон     Сюда нужно указать путь к картинке какой-то
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((400, 300))  # Изменяем размер под окно
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Создаём холст и добавляем фоновое изображение
    canvas = tk.Canvas(win, width=400, height=300)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.pack()

    # Рисуем параллелограмм поверх изображения
    points = [150, 50, 350, 50, 250, 200, 50, 200]  # Координаты вершин
    canvas.create_polygon(points, fill="white", outline="red")

    # Сохраняем ссылку на изображение (чтобы не удалилось)
    win.bg_photo = bg_photo

# Функция для второго модального окна (изменение состояния)
def open_state_window():
    state_win = Toplevel(root)
    state_win.title("Ефименко Милана Викторовна")
    state_win.geometry("400x300+400+300")

    label = tk.Label(state_win, text="Нажми кнопку для изменения состояния", font=("Arial", 12))
    label.pack(pady=20)

    def toggle_state():
        if state_win.attributes('-fullscreen'):
            state_win.attributes('-fullscreen', False)
        else:
            state_win.attributes('-fullscreen', True)

    btn_toggle = tk.Button(state_win, text="Изменить состояние окна", command=toggle_state)
    btn_toggle.pack()

# Кнопки
btn1 = tk.Button(root, text="Открыть параллелограмм", command=open_parallelogram)
btn1.pack(pady=10)
btn1.bind("<Enter>", lambda e: btn1.config(text="Открытие параллелограмма"))  # Подсказка при наведении
btn1.bind("<Leave>", lambda e: btn1.config(text="Открыть параллелограмм"))  # Возвращение текста

btn2 = tk.Button(root, text="Изменение состояния окна", command=open_state_window)
btn2.pack(pady=10)
btn2.bind("<Enter>", lambda e: btn2.config(text="Открыте окна изменения"))  # Подсказка при наведении
btn2.bind("<Leave>", lambda e: btn2.config(text="Изменение состояния окна"))  # Возвращение текста

# Запуск главного окна
root.mainloop()
