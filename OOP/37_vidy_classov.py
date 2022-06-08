# Прикрепите файл с кодом, демонстрирующий работу разных видов методов класса

class Germany:

    @staticmethod
    def contactish():
        print("Контакт")

    @classmethod
    def practish(cls):
        print("Практика")

    def gud(self):
        print("Хорошо")

Germany.contactish()
Germany.practish()
G = Germany()
G.gud()