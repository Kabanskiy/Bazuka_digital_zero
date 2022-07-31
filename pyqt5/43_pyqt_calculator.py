# графический интерфейс для калькулятора
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton # QtWidget - для построения графического окошка,
# QLabel - размеры окна, QPushButton - виджит, отвечающий за нажатие кнопки
import sys


class Calculator(QWidget): # импортировали и унаследовали  QtWidget  в наш инициализатор
    def __init__(self):
        super().__init__()
        self.initUI() # initUI метод, которому делегируется создание GUI



    def initUI(self): # это место, где будет происходить построение картинки, нашей GUI
        self.setGeometry(350, 350, 250, 400) # задаем параметры окна
        self.setWindowTitle('Кулькулятор') # задаем название

        # поле, которе отвечает за вывод результатов
        self.label = QLabel(self)
        self.label.setText('0')         # изначально будет висеть 0
        self.label.resize(150, 100)     # задаем размеры окна
        self.move(0,0)

        # кнопки
        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 100)
        # self.num_1.clicked.connact()

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 210)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 210)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(60, 265)

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(5, 265)

        self.umnozh = QPushButton('*', self)
        self.umnozh.resize(50, 50)
        self.umnozh.move(115, 265)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(5, 320)

        self.ravno = QPushButton('=', self)
        self.ravno.resize(50, 50)
        self.ravno.move(60, 320)

        self.delen = QPushButton('/', self)
        self.delen.resize(50, 50)
        self.delen.move(115, 320)

        self.ce = QPushButton('CE', self)
        self.ce.resize(50, 50)
        self.ce.move(170, 100)

        self.stepen = QPushButton('^', self)
        self.stepen.resize(50, 50)
        self.stepen.move(170, 155)

        self.coren = QPushButton('√', self)
        self.coren.resize(50, 50)
        self.coren.move(170, 210)

        self.prots = QPushButton('%', self)
        self.prots.resize(50, 50)
        self.prots.move(170, 265)

        self.zapyat = QPushButton(',', self)
        self.zapyat.resize(50, 50)
        self.zapyat.move(170, 320)

# Для того, чтобы тестировать все, что создаем:
if __name__=='__main__':
    app = QApplication(sys.argv) # создали экз-р класса QAppl-n, и передаем sys.argv - аргументы командной строки
    ex = Calculator()            # создали объект нашего класса
    ex.show()                    # показали объект нашего класса
    sys.exit(app.exec())         # этим мы завершаем наше приложение. И если возникнут ошибки, мы получим сообщение
