# графический интерфейс для калькулятора
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton  # QtWidget - для построения графического окошка,
# QLabel - размеры окна, QPushButton - виджит, отвечающий за нажатие кнопки
import sys


class Calculator(QWidget):  # импортировали и унаследовали  QtWidget  в наш инициализатор
    def __init__(self):
        super().__init__()
        self.initUI()  # initUI метод, которому делегируется создание GUI
        self.my_input = []  # создаем пустой массив
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):  # это место, где будет происходить построение картинки, нашей GUI
        self.setGeometry(350, 350, 250, 400)  # задаем параметры окна
        self.setWindowTitle('Кулькулятор')  # задаем название

        # поле, которе отвечает за вывод результатов
        self.label = QLabel(self)
        self.label.setText('0')  # изначально будет висеть 0
        self.label.resize(150, 100)  # задаем размеры окна
        self.move(0, 0)

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

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.zapyat.clicked.connect(self.zapyat_1)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.umnozh.clicked.connect(self.umnozh_1)
        self.stepen.clicked.connect(self.stepen_1)
        self.coren.clicked.connect(self.coren_1)
        self.prots.clicked.connect(self.prots_1)
        self.ravno.clicked.connect(self.ravno_1)
        self.ce.clicked.connect(self.ce_1)

    def enterValue(self):  # функция, отвечающая за ввод
        if self.label.text() == '0':
            self.label.setText('')  # эта функция добавляет текст в наш лейбл
        self.label.setText(self.label.text() + self.my_input)  # если не ноль, оно выводится и остается

    def one(self):
        self.my_input = '1'
        self.enterValue()  # здесь enterValue вызывается, смотрит выше на label.text()=='0':, если не 0, то остается

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def zapyat_1(self):
        self.my_input = ','
        self.enterValue()

    # знаки

    def plus_1(self):  # 1 чтобы не было конфликта
        self.operation = '+'
        self.operand_1 = float(
            self.label.text())  # записали все, что было в label и привели все к типу float, чтобы считать
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def umnozh_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def delen_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def stepen_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def coren_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def prots_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ravno_1(self):
        self.operand_2 = float(self.label.text())  # забирает весь текст, который записан в нашем label
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        if self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        if self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        if self.operation == '/':
            if self.operand_2 == '0':
                self.rezult == 'Error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        if self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2
        if self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)
        if self.operation == '%':
            self.rezult = self.operand_1 % self.operand_2  # надо пофиксить
        self.label.setText(str(self.rezult))  # обязательно указываем str

    def ce_1(self):
        self.label.setText('')


# Для того, чтобы тестировать все, что создаем:
if __name__ == '__main__':
    app = QApplication(sys.argv)  # создали экз-р класса QAppl-n, и передаем sys.argv - аргументы командной строки
    ex = Calculator()  # создали объект нашего класса
    ex.show()  # показали объект нашего класса
    sys.exit(app.exec())  # этим мы завершаем наше приложение. И если возникнут ошибки, мы получим сообщение
