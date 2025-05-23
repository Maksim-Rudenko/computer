import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox, ttk
from math import log, sqrt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkcalendar import DateEntry


# Функция для открытия окна с анкетой
def open_form_window():
    form_window = Toplevel(root)
    form_window.title("Анкета")
    form_window.geometry("350x250")

    Label(form_window, text="ФИО:").grid(row=0, column=0, padx=5, pady=5)
    fio_entry = Entry(form_window)
    fio_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(form_window, text="Дата рождения:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    dob_entry = DateEntry(form_window, width=17, selectmode="day", year=2000, month=1, day=1)
    dob_entry.grid(row=1, column=1, padx=5, pady=5)

    Label(form_window, text="Пол:").grid(row=2, column=0, padx=5, pady=5)

    # Выпадающий список для выбора пола
    gender_options = ["Мужской", "Женский"]
    gender_combobox = ttk.Combobox(form_window, values=gender_options, state="readonly")
    gender_combobox.grid(row=2, column=1, padx=5, pady=5)
    gender_combobox.set(gender_options[0])  # Устанавливаем значение по умолчанию

    def submit():
        print("ФИО:", fio_entry.get())
        print("Дата рождения:", dob_entry.get())  # Получаем выбранную дату
        print("Пол:", gender_combobox.get())  # Получаем выбранный пол
        form_window.destroy()

    Button(form_window, text="Отправить", command=submit).grid(row=3, columnspan=2, pady=10)

# Функция для окна с вычислением функции
def open_function_window():
    func_window = Toplevel(root)
    func_window.title("Вычисление функции")
    func_window.geometry("500x400")

    Label(func_window, text="Введите X:").pack(pady=5)
    x_entry = Entry(func_window)
    x_entry.pack()

    y_label = Label(func_window, text="Значение Y:")
    y_label.pack(pady=5)

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=func_window)
    canvas.get_tk_widget().pack()

    def calculate():
        try:
            x = float(x_entry.get())
                        
            if x < -4:
                y = (-2)
            elif x < 0:
                y = (x / 4)
            elif x < 2:
                y = (x ** 2)
            else:
                y = (-0.5 * x + 5)     

            y_label.config(text=f"Значение Y: {y:.2f}")

            ax.clear()            
            x_vals = [i for i in range(int(x) - 20, int(x) + 20)]
            y_vals = []  # Создаем пустой список для значений y

            for x_value in x_vals:
                if x_value < -4:
                    y_value = -2
                elif x_value < 0:
                    y_value = x_value / 4
                elif x_value < 2:
                    y_value = x_value ** 2
                else:
                    y_value = -0.5 * x_value + 5

                y_vals.append(y_value)  # Добавляем y в массив
            
            ax.plot(x_vals, y_vals)
            ax.scatter(x, y, color="red", label="Введённый X")
            ax.legend()
            ax.grid()

            canvas.draw()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное значение X!")

    def clear():
        x_entry.delete(0, tk.END)
        y_label.config(text="Значение Y:")
        ax.clear()
        canvas.draw()

    Button(func_window, text="Решить", command=calculate).pack(pady=5)
    Button(func_window, text="Очистить", command=clear).pack(pady=5)
    Button(func_window, text="Выход", command=func_window.destroy).pack(pady=5)

# Функция для окна проверки попадания точки в кольцо
def open_ring_window():
    ring_window = Toplevel(root)
    ring_window.title("Проверка точки в кольце")
    ring_window.geometry("500x400")

    Label(ring_window, text="Введите X:").pack(pady=5)
    x_entry = Entry(ring_window)
    x_entry.pack()

    Label(ring_window, text="Введите Y:").pack(pady=5)
    y_entry = Entry(ring_window)
    y_entry.pack()

    Label(ring_window, text="Введите R1 (меньший радиус):").pack(pady=5)
    r1_entry = Entry(ring_window)
    r1_entry.pack()

    Label(ring_window, text="Введите R2 (больший радиус):").pack(pady=5)
    r2_entry = Entry(ring_window)
    r2_entry.pack()

    result_label = Label(ring_window, text="Результат:")
    result_label.pack(pady=5)

    # Кнопки перед графиком
    btn_frame = tk.Frame(ring_window)
    btn_frame.pack(pady=10)

    Button(btn_frame, text="Определить", command=lambda: check_point()).pack(side=tk.LEFT, padx=5)
    Button(btn_frame, text="Очистить", command=lambda: clear()).pack(side=tk.LEFT, padx=5)
    Button(btn_frame, text="Выход", command=ring_window.destroy).pack(side=tk.LEFT, padx=5)

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=ring_window)
    canvas.get_tk_widget().pack()

    def check_point():
        try:
            x = float(x_entry.get())
            y = float(y_entry.get())
            r1 = float(r1_entry.get())
            r2 = float(r2_entry.get())

            if r1 <= 0 or r2 <= 0 or r1 >= r2:
                raise ValueError("Введите корректные радиусы!")

            dist = sqrt(x**2 + y**2)

            if r1 < dist < r2 and ((x >= 0 and y >= 0) or (x <= 0 and y <= 0)):
                result_label.config(text="Точка ВНУТРИ сектора")
                color = "green"
            else:
                result_label.config(text="Точка ВНЕ сектора")
                color = "red"

            ax.clear()
            ax.set_xlim(-r2 - 1, r2 + 1)
            ax.set_ylim(-r2 - 1, r2 + 1)

            circle_outer = plt.Circle((0, 0), r2, color="blue", fill=False)
            circle_inner = plt.Circle((0, 0), r1, color="black", fill=False)
            ax.add_patch(circle_outer)
            ax.add_patch(circle_inner)
            ax.scatter(x, y, color=color, label="Точка")
            ax.legend()
            ax.grid()

            canvas.draw()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные значения!")

    def clear():
        x_entry.delete(0, tk.END)
        y_entry.delete(0, tk.END)
        r1_entry.delete(0, tk.END)
        r2_entry.delete(0, tk.END)
        result_label.config(text="Результат:")
        ax.clear()
        canvas.draw()

# Основное окно
root = tk.Tk()
root.title("Руденко Максим Андреевич ЗИТ-21")
root.geometry("400x300")

Label(root, text="Руденко Максим Андреевич ЗИТ-21\n Лабораторная работа 3", font=("Arial", 18)).pack(pady=20)

def on_enter(e, btn, text):
    btn.config(text=text)

def on_leave(e, btn, original_text):
    btn.config(text=original_text)

btn1 = Button(root, text="Открыть анкету", command=open_form_window)
btn1.pack(pady=10)
btn1.bind("<Enter>", lambda e: on_enter(e, btn1, "Заполните анкету"))
btn1.bind("<Leave>", lambda e: on_leave(e, btn1, "Открыть анкету"))

btn2 = Button(root, text="Открыть окно вычислений", command=open_function_window)
btn2.pack(pady=10)
btn2.bind("<Enter>", lambda e: on_enter(e, btn2, "Ввести X, рассчитать Y"))
btn2.bind("<Leave>", lambda e: on_leave(e, btn2, "Открыть окно вычислений"))

btn3 = Button(root, text="Проверить точку", command=open_ring_window)
btn3.pack(pady=10)
btn3.bind("<Enter>", lambda e: on_enter(e, btn3, "Введите координаты точки"))
btn3.bind("<Leave>", lambda e: on_leave(e, btn3, "Проверить точку"))

# Добавляем кнопку завершения программы в главное окно
btn_exit = Button(root, text="Завершить программу", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()