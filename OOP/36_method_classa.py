#
# class Batya():
#     @staticmethod # декоратор
#     def staticmethod():
#         print('static method called')
#
# class son_Batya(Batya):
#     pass
#
# my_obj = Batya()
# my_obj.staticmethod()
# my_obj2 = son_Batya()
# my_obj2.staticmethod()

class Person():
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False
print(Person.is_adult(19))