# Python-Flask-Udemy

Udemy courses on Python and Flask: [Basic](https://www.udemy.com/course/rest-api-flask-and-python/) and [Advance](https://www.udemy.com/course/advanced-rest-apis-flask-python/)

<h3 id='summary'>Summary</h3>

- [Python Refresher](#python-refresher)
    - [Variables](#variables)
        - [Numbers](#numbers)
        - [Strings](#strings)
        - [List, Tuples and Sets](#list-tuples-sets)
        - [Booleans](#booleans)
    - [User Input](#user-input)
    - [The 'in' Keyword](#in-keyword)
    - [Loops](#loops)
    - [List Comprehension](#list-comprehension)
    - [Dictionaries](#dictionaries)
        - [Dictionaries Comprehension](#dictionaries-comprehension)
    - [Destructuring Tuples](#destructuring-tuples)
    - [Functions](#functions)
        - [Lambda Functions](#lambda-functions)
        - [Unpacking/Destructuring Arguments](#unpacking-arguments)
        - [Unpacking/Destructuring Keyword Arguments](#unpacking-keyword-arguments)
    - [Object Oriented Programming](#object-oriented)
        - [Magic Methods: '\_\_str\_\_' and '\_\_repr\_\_'](#magic-methods)
        - [@classmethod and @staticmethod](#oo-methods)
        - [Class Inheritance](#class-inheritance)
        - [Class Composition](#composition)
    - [Type Hinting](#type-hinting)
    - [Imports in Python](#imports)
    - [Errors](#errors)
    - []()
    - []()
    - []()
    - []()
    - []()


<h2 id='python-refresher'>Python Refresher</h2>

<h3 id='variables'>Variables</h3>

<h5 id='numbers'>Numbers</h5>

[Summary](#summary)

Python has integers (15) and floats (9.99).

<h5 id='strings'>Strings</h5>

[Summary](#summary)

Regular strings, you can use ```'``` or ```"```. 

You can add (+) 2 strings together, or multiply (*) by a number:

```python
a = 'ok'
b = 'test'
print(a + b)                            # 'oktest'
print(a * 2)                            # 'okok'
```

After python v3.6 we have the string interpolation to embed variables to strings. We use the letter `f` in front of it.

```python
name = 'Bob'
print(f'Hello, {name}')
```

We can use templating to embed the variable afterwards.

```python
name = 'Bob'
greeting = 'Hello, {}'
with_name = greeting.format(name)       # add name as the variable to be used
print(with_name)
```

<h5 id='lists-tuples-sets'>Lists, Tuples and Sets</h5>

[Summary](#summary)

List ordered collection and possible to modify afterwards. `['Bob', 'Anne']`

Tuple ordered collection and cannot be modified after it was created. `('Bob', 'Anne')`

Set collection that has no order and has no duplicates. `{'Bob', 'Anne'}`

Methods:

- append() - add element to the end
- add() - used for SETS because it has no order. Adds element.
- remove() - remove element
- difference() - returns a set with the difference between two sets.
- union() - unites 2 sets and return a set will all the items.
- intersection() - return the items that 2 sets has that are the same.

``` python
friends = {'Bob', 'Anne', 'Rolf'}
abroad = {'Bob', 'Rolf', 'Lara'}
local_friends = friends.difference(abroad)
# local_friends = {'Anne'}
local_friends_opposite = abroad.difference(friends)
# local_friends = set()
other_friends = {'Maria', 'Jose'}
all_friends = friends.union(other_friends)
# all_friends = {'Bob', 'Anne', 'Rolf', 'Maria', 'Jose'}
friends_study_science = {'Ellen', 'Renato', 'Bob', 'Rolf'}
abroad_study_science = abroad.intersection(friends_study_science)
```

<h5 id='booleans'>Booleans</h5>

[Summary](#summary)

True or False.

Some of the comparisons available:
- ==
- !=
- \>
- <
- \>=
- <=

The `is` keyword checks if two elements are **the same**, so be careful with memory allocations. Even if two lists has the same items, it doesn't mean they are equal with the keyword is, since they are allocated in different places in memory.

<h3 id='user-input'>User Input</h3>

[Summary](#summary)

```python
name = input('Enter your name: ')
size = input('Enter the size of your house: ')
```

Note: Input method always gives back a string. If you are expecting a number to do some math, you need to convert it to a number. You can use: `int(size)` or `float(size)`.

```python
size = input('Enter the size of your house in square feet: ')
square_feet = int(size)
floating = float(size)
print(square_feet, floating)
square_meters = square_feet / 10.8
print(f'{square_feet} square feet is {square_meters} square meters.')
print(f'{square_feet} square feet is {square_meters:.2f} square meters.')
# note: the `:.2f` will force the number to 2 decimals.
```

<h3 id='in-keyword'>The 'in' Keyword</h3>

[Summary](#summary)

We use the `in` keyword to check if we have the item in a sets, lists, tuples or dictionaries.

```python
colors = {'blue', 'red', 'white', 'black'}
user_color = input('Enter a color that you think is in the game: ').lower()
if user_color in colors:
    print('You are right!')
else:
    print("Sorry, you're wrong")
```

<h3 id='loops'>Loops</h3>

[Summary](#summary)

- while
- for / in

```python
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# you can also use the sum method
total = sum(grades)
```

<h3 id='list-comprehension'>List Comprehension</h3>

[Summary](#summary)

```python
numbers = [1,2,3]
doubled = []

for num in numbers:
    doubled.append(num * 2)

# instead of doing that, we can use list comprehensions:
doubled = [ num * 2 for num in numbers]

# we can also change the `num` word for an `x` to have a smaller code, although I don't think it gets very clear and readable
doubled = [ x * 2 for x in numbers]

# Another Example:
friends = ['Suzy', 'Ellie', 'Sarah', 'Anna', 'Sayuri']
friends_starts_s = []

for friend in friends:
    if friend.startswith('S'):
        friends_starts_s.append(friend)

# using list comprehension
friends_starts_s = [friend for friend in friends if friend.startswith('S')]

# using the `x`
friends_starts_s = [x for x in friends if x.startswith('S')]
```

<h3 id='dictionaries'>Dictionaries</h3>

[Summary](#summary)

Key-value pairs.

Methods:
- items() - returns the key and the value
- values() - return the values back
```python
student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

for student, attendance in student_attendance.items():
    print(f'{student} has {attendance}% of attendance')

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
```

<h5 id='dictionaries-comprehension'>Dictionaries Comprehension</h5>

[Summary](#summary)

```python
users = [
    (0, 'Bob', '1234567'),
    (1, 'Rolf', 'mypassword'),
    (2, 'Jose', 'extralongpassword1234567'),
    (3, 'Lara', 'lara1234'),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)                         # {'Bob': (0, 'Bob', '1234567'), 'Rolf': (1, 'Rolf', 'mypassword'), 'Jose': (2, 'Jose', 'extralongpassword1234567'), 'Lara': (3, 'Lara', 'lara1234')}

username_input = input('Enter your username: ')
password_input = input('Enter your password: ')

_, username, password = username_mapping[username_input]

if password_input == password:
    print('Your details are correct!')
else:
    print('Your details are incorrect.')
```

<h3 id='destructuring-tuples'>Destructuring Tuples</h3>

[Summary](#summary)

```python
x, y = 5, 11                        # x = 5, y = 11

# or
t = 5, 11
x, y = t
```

The underscore as a variable was decided by the Python community to be a variable that we don't care, that is meant to be ignored.

```python
person = ('Jose', 30, 'artist')
name, _, profession = person

print(name, profession)
```

The `*` will get as much values as it can leaving values for the other destructured variables.

```python
head, *tail = [1, 2, 3, 4, 5]
print(head)                     # [1]
print(tail)                     # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]
print(head)                     # [2, 3, 4, 5]
print(tail)                     # [1]
```

<h3 id='functions'>Functions</h3>

[Summary](#summary)

Important note about scope, if you redefine (look example below) a global variable inside a function, the function will create a new variable with the same name within the function scope. It will not understand that you are redefining the global one.

```python
friends = ['Ella', 'Ellie']

def add_friend_wrong():
    friend_name = input('Enter your friend name: ')
    friends = friends + [friend_name]                   # it will give an error of UnboundLocalError: local variable 'friends' referenced before assignment

def add_friend():
    friend_name = input('Enter your friend name: ')
    f = friends + [friend_name]
    print(f) 

add_friend()
```

Positional and Keyword Arguments:
- positional arguments - are the ones added and read according to its position.
- keyword arguments - are the ones added with the keyword for them in front of them.

*Note*: If you have both types, the positional arguments always needs to come first, in other words, in front of the keyword arguments.

*Note 2*: you can have a default parameter (always at the end) if you want.

```python
def say_hello(name, surname='Doe'):
    print(f'Hello, {name} {surname}.')

say_hello(surname='Filly', name='Phil')                 # Keyword Arguments ==> Hello, Phil Filly.
say_hello('Filly', 'Phil')                              # Positional Arguments ==> Hello, Filly Phil.
say_hello('Filly', surname='Phil')                               # Positional and Keyword Arguments ==> Hello, Filly Phil.
say_hello('Phil')                               # Positional Argument + Default Parameter ==> Hello, Phil Doe.
```

<h5 id='lambda-functions'>Lambda Functions</h5>

[Summary](#summary)

Exclusively used to operate on inputs and return outputs, they are not really used to do actions.



```python
def add(x, y):
    return x + y

# transform into Lambda
add = lambda x, y: x + y

print(add(5, 7))

# you can also call it right away, like an IIFE
print((lambda x, y: x + y)(5, 7))


# Another Example
def double(x):
    return x * 2

sequence = [1, 3, 5, 7]
doubled = [double(x) for x in sequence]
doubled_inline = [(lambda x: x * 2)(y) for y in sequence]
print(doubled)
print(doubled_inline)

# same thing - you can use map, it will go through each number in the sequence and apply double on it, it will then return a map object. So if you want to return a list, you need to transform it.
# NOTE: it is a little bit slower than list comprehension
doubled_same = list(map(double, sequence))

print(doubled_same)
```

<h5 id='unpacking-arguments'>Unpacking/Destructuring Arguments</h5>

[Summary](#summary)

```python
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

multiply(1,3,5)

def add(x,y):
    return x + y

nums = [3, 5]
add(*nums)              # it will destructure the nums when calling add, so 3 will be x and 5 will be y

# Another way
nums = {'x': 15, 'y': 25}
add(x=nums['x'], y=nums['y'])
# instead of doing like that, we can use `**` if our keywords are the same as the properties (ex. x and x)
add(**nums)

# Going back to the mulpiply example and using with another function
def apply(*args, operator):
    if operator == '*':
        return multiply(*args)                  # we need to add the `*` to destructure, otherwise we will send a tuple and the multiply function will create a tuple with the tuple
    elif operator == '+':
        return sum(args)
    else:
        return 'No valid operator provided to apply()'

print(apply(1, 3, 6, 9, operator='*'))             # we need to use the keyword argument for operator, otherwise the `*args` from the function will get everything as the args and the operator will be missing.
```

<h5 id='unpacking-keyword-arguments'>Unpacking/Destructuring Keyword Arguments</h5>

[Summary](#summary)

It collects all the arguments and puts them into a dictionary

```python
def named(**kwargs):
    print(kwargs)

named(name='Bob', age=25)               # {'name': 'Bob', 'age': 25}

# Another option
def named1(name, age):
    print(name, age)

details = {'name': 'Bob', 'age': 25}

named1(**details)           # Bob 25
named(**details)            # {'name': 'Bob', 'age': 25}

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')

print_nicely(name='Bob', age=25)            
# {'name': 'Bob', 'age': 25}
# name: Bob
# age: 25
```

We can use args and kwargs together. One important thing to notice is that `args` needs to come first!

```python
def both(*args, **kwargs):
    print(args)                     # (1, 3, 5)
    print(kwargs)                   # {'name': 'Bob', 'age': 25}

both(1, 3, 5, name='Bob', age=25)
```


<h3 id='object-oriented'>Object Oriented Programming</h3>

[Summary](#summary)

```python
# create the Student class
class Student:
    # all objects has the self ('this'), but they can have other properties, like name or grades
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

# create a new student
student1 = Student('Matt', (90, 90, 80, 75, 80))
student2 = Student('Rob', (40, 50, 60, 75, 60))
print(student1.name)
print(student2.grades)
print(Student.average(student1))     #same as below
print(student1.average())
```

<h5 id='magic-methods'>Magic Methods: '__str__' and '__repr__'</h5>

[Summary](#summary)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Person('Bob', 35)
print(bob)                  # prints a string representation of the instance: <__main__.Person object at 0x10a62bd90>

# modify to print what we want
class Person_modified:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # what to print when we print the string representation of the instance
    def __str__(self):
        return f'I am {self.name}, and I have {self.age} years.'
    
    # this method goal is to be unambiguous and it should return a string that allows us to recreate the object very easily
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

bob_modified = Person_modified('Bob', 35)
print(bob_modified)                 # I am Bob, and I have 35 years.
# in order to print the __repr__ method, you can call it or comment the __str__ and just print the instance:
print(bob_modified.__repr__())          # <Person('Bob', 35)>
```

<h5 id='oo-methods'>@classmethod and @staticmethod</h5>

[Summary](#summary)

```python
class ClassTest:
    def instance_method(self):
        print(f'Called instance_method of {self}')
    
    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')
    
    @staticmethod
    def static_method():
        print('Called static_method')

test = ClassTest()
# instance method because it is called on the instance - it will receive 'self', which is the instance and you can use it in the return
test.instance_method()
# class method because it is called on the class - it will receive 'cls', which is the class and you can use it in the return => Very used as factory
ClassTest.class_method()
# static method is called without 'passing' the object/instance to it, it is really just a function that you pasted inside the class, it doesn't have any info of the class or the instance
ClassTest.static_method()

# Another Example
class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'
    
    # factory => create a new instance within the class using the class ==> since cls is the class, you can use Book or cls, but it is best practices to use cls, also because of inheritance
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, Book.TYPES[1], page_weight + 100)

book = Book.hardcover('Harry Potter', 1500)
light = Book.hardcover('Python', 600)

print(book)
print(light)
```

<h5 id='class-inheritance'>Class Inheritance</h5>

[Summary](#summary)

```python
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        # the '!r' calls the repr method on self.name, so it adds the quotes automatically
        return f'Device {self.name!r} ({self.connected_by})'
    
    def disconnect(self):
        self.connected = False
        print('Disconnected.')

# create a Printer class who inherits from Device, so you have access to all the methods from the Device class and can also add new methods specific to the Printer class
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # get the parent class with super() and then call the __init__ method of it passing the variables => this way you don't have to copy everything again
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining.)'
    
    def print(self, pages):
        if not self.connected:
            print('Your printer is not connected!')
            return
        print(f'Printing {pages} pages')
        self.remaining_pages -= pages

headphones = Device('Headphones', 'Bluetooth')
print(headphones)

printer = Printer('Printer', 'USB', 500)
printer.print(20)
print(printer)

printer.disconnect()
printer.print(30)
```

<h5 id='composition'>Class Composition</h5>

[Summary](#summary)

It is a counterpart of inheritance to build classes that uses other classes.
Used the most. Allows classes to be simpler and reduces the complexity of your code overall.

```python
class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity
    
    def __str__(self):
        # python ternary operator: 'true' if 'condition' else 'false'
        end = 's.' if self.quantity > 1 else '.'
        return f'Bookshelf with {self.quantity} book{end}'

shelf = Bookshelf(300)

# with inheritance ==> not the best way, you are saying that books are also bookshelves, which is not technically true. Also, you are completely overriding the __str__ method from Bookshelf and you are not using the Bookshelf anywhere.
class Book_inheritance(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name
    
    def __str__(self):
        return f'Book {self.name}'

book = Book_inheritance('Harry Potter', 120)
print(book)

# with composition ==> better to use in this case, since with this you mean: a bookshelf has many books. But a book is not a bookshelf.
class Bookshelf_composition:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        # python ternary operator: 'true' if 'condition' else 'false'
        end = 's.' if len(self.books) > 1 else '.'
        return f'Bookshelf with {len(self.books)} book{end}'

class Book_composition:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'Book {self.name}'

book = Book_composition('Harry Potter')
book1 = Book_composition('Harry Potter II')
shelf1 = Bookshelf_composition(book, book1)
print(shelf1)
```

In sum, Inheritance means a book is a bookshelf, while Composition means that a bookshelf has many books.

<h3 id='type-hinting'>Type Hinting</h3>

[Summary](#summary)

Is a 'newer' feature (python v3.5+) that gives you the option to add types.

```python
from typing import List         # Tuple, Set, etc.

# sequence is a type of List (or list, but the best practices is use List and import it from typing)
# this function returns a float
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

list_avg(123)               # TypeError: 'int' object is not iterable
list_avg([1,2,3])           # 2.0

# Another Example
class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'
    
    @classmethod
    # this is how you say it will return the class Book from within the class Book. If it was another class, you don't need the quotes
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, Book.TYPES[1], page_weight + 100)

class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books
    
    def __str__(self) -> str :
        return f'Bookshelf with {len(self.books)} books.'
```

<h3 id='imports'>Imports in Python</h3>

[Summary](#summary)

```python
# from (file we want from) import (what we want to import)
from mymodule import divide

# you can also just import the file if you have a default export there
import mymodule
```

With python v2 you need to add a `__init__.py` file on the folder in order to be able to import from that folder.

Relative Imports are the ones that import from the same folder.

```python
from topfolder.innerfolder import myfunction
from topfolder.innerfolder import *
```

<h3 id='errors'>Errors</h3>

[Summary](#summary)

- ZeroDivisionError
- TypeError
- ValueError
- RuntimeError

```python
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be a 0.')
    return dividend / divisor

grades = []

# try/except/else block
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as err:
    print(err)
    print('There are no grades yet in your list.')
except ValueError as verr:
    print(verr)
    print('The grades needs to be a list.')
# run code if there are no errors
else:
    print(f'The average grade is {average}')
# run code always, with or without errors
finally:
    print('I always print')
```