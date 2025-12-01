import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, messagebox, ttk, IntVar, Checkbutton, Scale
from math import log, sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkcalendar import DateEntry


# Функция для открытия окна с анкетой
def open_form_window():
    form_window = Toplevel(root)
    form_window.title("Анкета")
    form_window.geometry("350x250+400+200")

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

    # Круговая шкала с ползунком
    Label(form_window, text="Уровень удовлетворенности:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    satisfaction_scale = Scale(form_window, from_=0, to=100, orient="horizontal")
    satisfaction_scale.grid(row=3, column=1, padx=5, pady=5)

    # Флажок (Checkbox)
    agreement_var = IntVar()
    check_btn = Checkbutton(form_window, text="Согласен на обработку данных", variable=agreement_var)
    check_btn.grid(row=4, columnspan=2, pady=5)

    def submit():
        print("ФИО:", fio_entry.get()) # Получаем ФИО
        print("Дата рождения:", dob_entry.get())  # Получаем выбранную дату
        print("Пол:", gender_combobox.get())  # Получаем выбранный пол
        print("Уровень удовлетворенности:", satisfaction_scale.get()) # Получаем уровень удовлетворенности
        print("Согласие на обработку:", "Да" if agreement_var.get() else "Нет") # Получаем согласие на обработку данных
        form_window.destroy()

    Button(form_window, text="Отправить", command=submit).grid(row=5, columnspan=2, pady=10)

# Функция для окна с вычислением функции
def open_function_window():
    func_window = Toplevel(root)
    func_window.title("Вычисление значения функции")
    func_window.geometry("500x400+400+200")

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
                        
            if x <= -4:
                y = -3
            elif x <= -3:
                y = 2 * x + 8
            elif x <= 3:
                y = sqrt(9 - pow(x, 2))
            elif x <= 8:
                y = 0.6 * (x - 3)
            else:
                y = 3   

            y_label.config(text=f"Значение Y: {y:.2f}")

            ax.clear()            
            x_vals = [i for i in range(int(x) - 20, int(x) + 20)]
            y_vals = []  # Создаем пустой список для значений y

            for x_value in x_vals:
                if x_value <= -4:
                    y_value = -3
                elif x_value <= -3:
                    y_value = 2 * x_value + 8
                elif x_value <= 3:
                    y_value = sqrt(9 - pow(x_value, 2))
                elif x_value <= 8:
                    y_value = 0.6 * (x_value - 3)
                else:
                    y_value = 3   

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
    ring_window.title("Нахождение точки в заданном секторе")
    ring_window.geometry("500x400+400+200")

    Label(ring_window, text="Введите X:").pack(pady=5)
    x_entry = Entry(ring_window)
    x_entry.pack()

    Label(ring_window, text="Введите Y:").pack(pady=5)
    y_entry = Entry(ring_window)
    y_entry.pack()

    Label(ring_window, text="Введите R1 (первый радиус полукруга):").pack(pady=5)
    r1_entry = Entry(ring_window)
    r1_entry.pack()

    Label(ring_window, text="Введите R2 (второй радиус окружности):").pack(pady=5)
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

            if r1 <= 0 or r2 <= 0:
                raise ValueError("Введите корректные радиусы!")
            
            if (((x - r1) ** 2 + y ** 2 <= r1 ** 2) and (y >= 0) and (x >= 0)) or (((x + r2) ** 2 + (y + r2) ** 2 >= r2 ** 2) and (abs(y) <= r2) and (abs(x) <= r2) and (x < 0) and (y < 0)):
                result_label.config(text="Точка ВНУТРИ сектора")
                color = "green"
            else:
                result_label.config(text="Точка ВНЕ сектора")
                color = "red"

            ax.clear()

            lim = r1 * 2 if r1 > r2 else r2 * 2 # Установим лимит по отображению осей

            ax.set_xlim(-lim, lim)
            ax.set_ylim(-lim, lim)

            circle_left_full = plt.Circle((-r2, -r2), r2, color="blue", fill=False)            
            circle_right_half = mpatches.Arc((r1, 0), 2*r1, 2*r1, angle=0, theta1=0, theta2=180, color="black", linewidth=2)
            ax.add_patch(circle_left_full)
            ax.add_patch(circle_right_half)
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
root.title("Ефименко Милана Викторовна ЗИТ-21")
root.geometry("500x350+400+200")

Label(root, text="Ефименко Милана Викторовна ЗИТ-21\n Лабораторная работа 3", font=("Arial", 18)).pack(pady=20)

def on_enter(e, btn, text):
    btn.config(text=text)

def on_leave(e, btn, original_text):
    btn.config(text=original_text)

btn1 = Button(root, text="Открыть анкету", command=open_form_window)
btn1.pack(pady=10)
btn1.bind("<Enter>", lambda e: on_enter(e, btn1, "Заполнить анкету"))
btn1.bind("<Leave>", lambda e: on_leave(e, btn1, "Открыть анкету"))

btn2 = Button(root, text="Открыть окно расчета функции", command=open_function_window)
btn2.pack(pady=10)
btn2.bind("<Enter>", lambda e: on_enter(e, btn2, "Ввести X, рассчитать Y"))
btn2.bind("<Leave>", lambda e: on_leave(e, btn2, "Открыть окно расчета функции"))

btn3 = Button(root, text="Проверить положение точки", command=open_ring_window)
btn3.pack(pady=10)
btn3.bind("<Enter>", lambda e: on_enter(e, btn3, "Введите координаты точки"))
btn3.bind("<Leave>", lambda e: on_leave(e, btn3, "Проверить положение точки"))

# Добавляем кнопку завершения программы в главное окно
btn_exit = Button(root, text="Завершить программу", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()