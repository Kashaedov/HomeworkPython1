# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number =  int (input('Введите номер дня недели: '))
if number > 7 or number <= 0:
  print ("Введено некорректное число")
elif number == 6 or number ==  7:
    print ('Это выходной')
else:
    print ('Это будний день')
