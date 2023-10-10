#print("Hello teacher")
#print("Homework Banul")

#1.Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.

#def multiply(b):
  #  multiplication = 1
   # for elements in b:
     #   if elements != 0:
     #       multiplication *= elements
   # return multiplication

#a = [1,2,3,4,5]
#print(multiply(a))

##############################
#2.Напишіть функцію для знаходження мінімуму у списку цілих

def _MinList(lst):
  if len(lst) > 0:
     _min = lst[0]

  for i in range(1,len(lst)):
   if lst[i] < _min:
     _min = lst[i]

  return _min

a = [1,2,3,4,5]
print(_MinList(a))