import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk  # Для работы с изображениями

# Основное окно приложения
root = tk.Tk()
root.title("Руденко Максим Андреевич ЗИТ-21")  # Заголовок окна
root.geometry("400x400+500+600")  # Размер 400x400, положение 500x600

# Надпись "Привет"
label = tk.Label(root, text="Привет", font=("Arial", 20))
label.pack(pady=20)

# Функция для модального окна (параллелограмм с изображением)
def open_parallelogram():
    win = Toplevel(root)
    win.title("Параллелограмм")
    win.geometry("400x300+550+650")
    win.attributes('-alpha', 0.4)  # Устанавливаем прозрачность 40%

    # Загружаем изображение из папки с программой
    image_path = r'E:\Сухого\city.jpeg'  # Задний фон
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((400, 300))  # Изменяем размер под окно
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Создаём холст и добавляем фоновое изображение
    canvas = tk.Canvas(win, width=400, height=300)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.pack()

    # Рисуем параллелограмм поверх изображения
    points = [50, 50, 350, 50, 300, 250, 0, 250]  # Координаты вершин
    canvas.create_polygon(points, fill="blue", outline="black")

    # Сохраняем ссылку на изображение (чтобы не удалилось)
    win.bg_photo = bg_photo

# Функция для второго модального окна (изменение состояния)
def open_state_window():
    state_win = Toplevel(root)
    state_win.title("Изменение состояния окна")
    state_win.geometry("300x200+550+650")

    label = tk.Label(state_win, text="Нажми кнопку для изменения состояния!", font=("Arial", 12))
    label.pack(pady=20)

    def toggle_state():
        if state_win.attributes('-fullscreen'):
            state_win.attributes('-fullscreen', False)
        else:
            state_win.attributes('-fullscreen', True)

    btn_toggle = tk.Button(state_win, text="Изменить состояние", command=toggle_state)
    btn_toggle.pack()

# Кнопки
btn1 = tk.Button(root, text="Открыть параллелограмм", command=open_parallelogram)
btn1.pack(pady=10)
btn1.bind("<Enter>", lambda e: btn1.config(text="Нажми для окна"))  # Подсказка при наведении
btn1.bind("<Leave>", lambda e: btn1.config(text="Открыть параллелограмм"))  # Возвращение текста

btn2 = tk.Button(root, text="Изменение состояния окна", command=open_state_window)
btn2.pack(pady=10)
btn2.bind("<Enter>", lambda e: btn2.config(text="Нажми для изменения"))  # Подсказка при наведении
btn2.bind("<Leave>", lambda e: btn2.config(text="Изменение состояния окна"))  # Возвращение текста

# Запуск главного окна
root.mainloop()
