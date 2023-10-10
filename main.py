#print("Hello teacher")
#print("Homework Banul")

#1.Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.

def multiply(b):
    multiplication = 1
    for elements in b:
        if elements != 0:
            multiplication *= elements
    return multiplication

a = [1,2,3,4,5]
print(multiply(a))
