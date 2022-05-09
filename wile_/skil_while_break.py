number = int(input('input number: '))
summa = 0
while number != 0:
  new_num = number % 10
  print(new_num)
  if new_num ==5:
    print('gap')
    break
  summa += new_num
  number //= 10
print('Sum: ', summa)