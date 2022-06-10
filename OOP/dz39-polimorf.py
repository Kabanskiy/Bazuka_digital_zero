# Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

class AK_74M:
    def automatical(self):
        print("AK-74M стреляет автоматически")

    def single(self):
        print("AK_74M не стреляет одиночными")  # на самом деле стреляет)

class Desert_eagle:
    def automatical(self):
        print("Desert eagle не стреляет автоматически")

    def single(self):
        print("Desert eagle стреляет одиночными")

def gun(shoot):
    shoot.automatical()

gun(AK_74M())
gun(Desert_eagle())
