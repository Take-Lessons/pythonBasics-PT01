print("Hello World")
# This is a statement that when the file is run in the terminal using python, py, or python3 main.py it will print what is in the ()

# int - whole numbers only

number01 = 100
print('Print number01:', number01)

# Float - allows for numbers with decimals

number02 = 43.5
print("printing number02:", number02)

# complex - similar to algebra 3x + y =12
x = 5
number03 = 15+x
print('printing number03:', number03)

name01 = 'Rosa'
class01 = 'Python Fundamentals'
print("name01:", name01)
print(name01, 'is taking a class called', class01)
print(f'{name01} is taking a class called {class01}')
print(name01+ ' ' + 'is taking a class called '+ class01)


# Tuple - collection of information or data that can not change
tuple01 = (1,2,3,4,5,56)
print('tuple01:', tuple01)

# list - collection of information or data that can be added to updated and removed from
list01 = [2,4,5,6,7,7,8]
print('list01:', list01)
print('3 item in list:', list01[2])
# all lists/tuples start with a index of 0 meaning the 1st item in the list/tuple is at position 0

# dictionary -  collect of data in key / value pairs

dict01 = {
    'class': 'Python Fundamentals',
    'location': 'Online',
    'duration': '30 min',
    'students': 3
}
print('whole dict:', dict01)
print('number of students:', dict01['students'])
print(dict01['class'], 'is being held', dict01['location'], 'and is', dict01['duration'], 'and currently has', dict01['students'])
