import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QListView, QTableView, QTreeView, QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon, QFont
from PyQt6.QtCore import QStringListModel, Qt


def open_article_window():
    global article_window
    article_window = QWidget()
    #article_window.setWindowIcon(QIcon("D:\\icon.png"))
    article_window.setWindowTitle("Успеваемость студентов")
    article_window.setGeometry(200, 200, 600, 400)
    layout = QVBoxLayout()


    # Обычный список (группы)
    list_view = QListView()
    list_model = QStringListModel(["Группа ИТ-101", "Группа ИТ-102", "Группа ИТ-103", "Группа ЗИТ-21"])
    list_view.setModel(list_model)

    # Раскрывающийся список (предметы)
    combo_box = QComboBox()
    combo_box.addItems(["Высшая математика", "История мировой культуры", "Физика", "Политэкономия", "Иностранный язык"])

    # Иерархический список (группы и предметы)
    tree_view = QTreeView()
    tree_model = QStandardItemModel()
    root_node = tree_model.invisibleRootItem()
    item1 = QStandardItem("Группа ИТ-101")
    item1.appendRow(QStandardItem("Высшая математик"))
    item1.appendRow(QStandardItem("Политэкономия"))
    root_node.appendRow(item1)

    item2 = QStandardItem("Группа ИТ-102")
    item2.appendRow(QStandardItem("Физика"))
    item2.appendRow(QStandardItem("История мировой культуры"))
    root_node.appendRow(item2)

    tree_view.setModel(tree_model)

    # Таблица 1 (Оценки по предметам)
    table_view1 = QTableView()
    table_model1 = QStandardItemModel(3, 4)
    table_model1.setHorizontalHeaderLabels(["Группа", "Высшая математика", "Политэкономия", "Физика"])
    table_model1.setItem(0, 0, QStandardItem("ИТ-101"))
    table_model1.setItem(0, 1, QStandardItem("4.7"))
    table_model1.setItem(0, 2, QStandardItem("4.2"))
    table_model1.setItem(0, 3, QStandardItem("4.9"))

    table_model1.setItem(1, 0, QStandardItem("ИТ-102"))
    table_model1.setItem(1, 1, QStandardItem("3.6"))
    table_model1.setItem(1, 2, QStandardItem("4.3"))
    table_model1.setItem(1, 3, QStandardItem("4.8"))

    table_view1.setModel(table_model1)

    # Таблица 2 (Средняя успеваемость)
    table_view2 = QTableView()
    table_model2 = QStandardItemModel(3, 2)
    table_model2.setHorizontalHeaderLabels(["Группа", "Средний балл"])
    table_model2.setItem(0, 0, QStandardItem("ИТ-101"))
    table_model2.setItem(0, 1, QStandardItem("4.5"))

    table_model2.setItem(1, 0, QStandardItem("ИТ-102"))
    table_model2.setItem(1, 1, QStandardItem("4.2"))

    table_model2.setItem(2, 0, QStandardItem("ИТ-103"))
    table_model2.setItem(2, 1, QStandardItem("4.0"))

    table_view2.setModel(table_model2)

    # Добавление элементов
    layout.addWidget(QLabel("Предметы:"))
    layout.addWidget(combo_box)
    layout.addWidget(QLabel("Группы:"))
    layout.addWidget(list_view)
    layout.addWidget(QLabel("Иерархический список:"))
    layout.addWidget(tree_view)
    layout.addWidget(QLabel("Оценки по предметам:"))
    layout.addWidget(table_view1)
    layout.addWidget(QLabel("Средняя успеваемость:"))
    layout.addWidget(table_view2)

    article_window.setLayout(layout)
    article_window.show()
    return article_window

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle("Руденко Максим Андреевич ЗИТ-21")
#main_window.setWindowIcon(QIcon("D:\\icon.png"))


main_window.setGeometry(100, 100, 400, 400)

central_widget = QWidget()
layout = QVBoxLayout()

label = QLabel("Лабораторная работа №4\n"
                            "Списки и таблицы.\n"
                            "Выполнил студент группы ЗИТ-21\n"
                            "Руденко Максим Андреевич")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)
label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
layout.addWidget(label)

btn_article = QPushButton("Открыть успеваемость")
btn_article.setToolTip("Нажмите, чтобы просмотреть статистику")
btn_article.clicked.connect(open_article_window)
layout.addWidget(btn_article)

central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)

main_window.show()
sys.exit(app.exec())
