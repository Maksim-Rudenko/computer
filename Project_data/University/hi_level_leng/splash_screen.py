import tkinter as tk
import time


class SplashScreen:
    """Класс заставки перед запуском основного приложения."""

    def __init__(self, root):
        self.root = root
        self.splash = tk.Toplevel(root)
        self.splash.title("Запуск приложения")
        self.splash.geometry("300x150")

        self.label = tk.Label(self.splash, text="Запуск приложения...", font=("Arial", 12))
        self.label.pack(expand=True)

        self.splash.update()
        self.run_loading_animation()

    def run_loading_animation(self):
        """Метод для имитации процесса загрузки."""
        for i in range(1, 101, 10):
            self.label.config(text=f"Руденко Максим Андреевич ЗИТ-21\n Лабораторная работа 1\nЗагрузка... {i}%")
            self.splash.update()
            time.sleep(0.3)

        self.splash.destroy()  # Закрываем заставку
