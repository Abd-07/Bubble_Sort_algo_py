import random

array = []

for i in range(10):
    array.append(random.randint(0,9))

print(array)

for left in range(len(array)):
    for right in range( len(array) - 1):
        if array[left] > array[right]:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

print(array)

'''character = 'a'
print(ord(character))'''

'''names= ["andray", "Michael", "Ivan", "dgo"]

for i in range(len(names)):
    names[i].upper()

names.sort()
print(names)'''

