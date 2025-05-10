#from PyQt6 import QtCore, QtWidgets
'''import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget(flags=QtCore.Qt.WindowType.Dialog)
window.setWindowTitle("Программное закрытие окна ")
window.resize(300, 70)
button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150, 30)
button.move(75, 20)
button.clicked.connect(window.close)
window.show()
sys.exit(app.exec())
'''

from PyQt6 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
# На уровне программы задаем синий цвет текста у надписей, вложенных в группы,
# и курсивное начертание текста кнопок
app.setStyleSheet(
            "QGroupBox QLabel {color: blue;} QPushButton {font-style: italic}")
window = QtWidgets.QWidget()
window.setWindowTitle("Таблицы стилей")
# На уровне окна задаем зеленый цвет текста у надписи с именем first и
# красный цвет текста у надписи, на которую наведен курсор мыши
window.setStyleSheet("QLabel#first {color: green;} QLabel:hover {color: red;}")
window.resize(200, 150)
# Создаем три надписи
lbl1 = QtWidgets.QLabel("Зеленый текст")
# Даем первой надписи имя first
lbl1.setObjectName("first")
lbl2 = QtWidgets.QLabel("Полужирный текст")
# У второй надписи указываем полужирный шрифт
lbl2.setStyleSheet("font-weight: bold")
lbl3 = QtWidgets.QLabel("Синий текст")
# Создаем кнопку
btn = QtWidgets.QPushButton("Курсивный текст")
# Создаем группу
box = QtWidgets.QGroupBox("Группа")
# Создаем контейнер, помещаем в него третью надпись и вставляем в группу
bbox = QtWidgets.QVBoxLayout()
bbox.addWidget(lbl3)
box.setLayout(bbox)
# Создаем еще один контейнер, помещаем в него две первые надписи, группу,
# кнопку и вставляем в окно
mainbox = QtWidgets.QVBoxLayout()
mainbox.addWidget(lbl1)
mainbox.addWidget(lbl2)
mainbox.addWidget(box)
mainbox.addWidget(btn)
window.setLayout(mainbox)
window.show()
sys.exit(app.exec())
