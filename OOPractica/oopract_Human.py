class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Заработано: {amount}. У вас {self.__money} денег')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super.__init__(SmallHouse.default_area, price)  # к дефолтному значению обращаемся через имя класса


# тесты
if __name__ == '__main__':  # значит дальше идут тесты
    Human.default_info()  # т.к. это статический метод, вызываем его через имя класса
    Vasya = Human('Василий', 31)
    Vasya.info()
    Vasya.earn_money(8000)
    Vasya.earn_money(7000)
    Vasya.info()

    # можно импортировать код в другую вкладку и будет работать с новыми вводными данными в oopract_Human2
