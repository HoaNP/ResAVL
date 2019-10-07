#!/usr/bin/python3

list_a = [1,2,3,4]
list_b = ['a','b','c']

index = int(input("Input the index: "))

assert(index < len(list_a))
new_list = list_a[:index] + list_b+ list_a[index:]

print(list_a, list_b)
print(new_list)