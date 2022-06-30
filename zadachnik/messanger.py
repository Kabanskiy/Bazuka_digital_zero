# Совместно со скиллбокс
#Структура одного сообщения.
chat_msg_1 = {
  'text': 'Всем бонжорно',
  'sender': 'Джян',
  'date': '31.01.22 21:00'
  }

chat_msg_2 = {
  'text': 'Всем дороу',
  'sender': 'Вася',
  'date': '31.01.22 22:00'
  }
#Список сообщения.
messages_list = ["Привет", "хуе мое", "бараньи яйца"]

# функция которая умеет выводить одно сообщение
def print_message(message):
  print(f "[{chat_msg_1 ['sender']}]: {chat_msg_1 ['text']} / {chat_msg_1['date']}")
  print("-"*20)

# print_message(chat_msg_1)
# print_message(chat_msg_2)

# Пройдем по всем элементам списка.
for n in messages_list:
  print_message(n)
