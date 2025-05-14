import tkinter as tk
from splash_screen import SplashScreen

class MainApplication:
    """Основной класс приложения."""
    def __init__(self, root):
        self.root = root
        self.root.title("Руденко Максим Андреевич")
        self.root.geometry("400x200")

        label = tk.Label(self.root, text="Добро пожаловать!", font=("Arial", 16))
        label.pack(expand=True)

    def run(self):
        """Запуск главного окна приложения."""
        self.root.mainloop()


# Точка запуска приложения
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно перед загрузкой

    SplashScreen(root)  # Запускаем заставку
    root.deiconify()  # Отображаем основное окно после заставки

    app = MainApplication(root)
    app.run()
