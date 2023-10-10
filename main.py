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

#def _MinList(lst):
 # if len(lst) > 0:
  #   _min = lst[0]

 # for i in range(1,len(lst)):
  # if lst[i] < _min:
  #   _min = lst[i]

  #return _min

#a = [1,2,3,4,5]
#print(_MinList(a))

#####################################

#3.Напишіть функцію, яка визначає кількість простих чисел у списку цілих

def is_prime(num):
  if num <= 1:
    return False

  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False

  return True

def count_primes_in_list(lst):
  count = 0

  for num in lst:
    if is_prime(num):
     count += 1
  return count
