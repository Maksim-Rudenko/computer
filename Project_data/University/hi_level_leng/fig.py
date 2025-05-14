import tkinter as tk
from tkinter import Toplevel, Label, Entry, Button, ttk

def open_form_window():
    form_window = Toplevel(root)
    form_window.title("Анкета")
    form_window.geometry("350x250")

    # Создаем рамку для выравнивания элементов
    frame = tk.Frame(form_window)
    frame.pack(pady=10)

    # Метка и поле для ФИО
    Label(frame, text="ФИО:", width=15, anchor="e").grid(row=0, column=0, padx=5, pady=5)
    fio_entry = Entry(frame, width=25)
    fio_entry.grid(row=0, column=1, padx=5, pady=5)

    # Метка для даты рождения
    Label(frame, text="Дата рождения:", width=15, anchor="e").grid(row=1, column=0, padx=5, pady=5)

    # Выпадающий список для дней (1-31)
    days = [str(i) for i in range(1, 32)]
    day_combobox = ttk.Combobox(frame, values=days, state="readonly", width=5)
    day_combobox.grid(row=1, column=1, padx=2, pady=5, sticky="w")
    day_combobox.set("1")

    # Выпадающий список для месяцев
    months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
              "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    month_combobox = ttk.Combobox(frame, values=months, state="readonly", width=10)
    month_combobox.grid(row=1, column=2, padx=2, pady=5, sticky="w")
    month_combobox.set("Январь")

    # Выпадающий список для годов (1900-2025)
    years = [str(i) for i in range(1900, 2026)]
    year_combobox = ttk.Combobox(frame, values=years, state="readonly", width=6)
    year_combobox.grid(row=1, column=3, padx=2, pady=5, sticky="w")
    year_combobox.set("2000")

    # Метка и поле для пола
    Label(frame, text="Пол:", width=15, anchor="e").grid(row=2, column=0, padx=5, pady=5)
    gender_options = ["Мужской", "Женский"]
    gender_combobox = ttk.Combobox(frame, values=gender_options, state="readonly", width=15)
    gender_combobox.grid(row=2, column=1, padx=5, pady=5, columnspan=3)
    gender_combobox.set(gender_options[0])

    # Функция для отправки данных
    def submit():
        print("ФИО:", fio_entry.get())
        print("Дата рождения:", day_combobox.get(), month_combobox.get(), year_combobox.get())
        print("Пол:", gender_combobox.get())
        form_window.destroy()

    # Кнопка отправки
    Button(frame, text="Отправить", command=submit).grid(row=3, columnspan=4, pady=10)

# Основное окно
root = tk.Tk()
root.title("Руденко Максим Андреевич ЗИТ-21")
root.geometry("400x300")

Label(root, text="Привет", font=("Arial", 18)).pack(pady=20)
Button(root, text="Открыть анкету", command=open_form_window).pack(pady=10)

root.mainloop()
