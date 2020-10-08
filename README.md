<h1>Python-Flask-Udemy</h1>

Udemy courses on Python and Flask: [Basic](https://www.udemy.com/course/rest-api-flask-and-python/) and [Advance](https://www.udemy.com/course/advanced-rest-apis-flask-python/)

<h3 id='summary'>Summary</h3>

- [Python Refresher](#python-refresher)
  - [Variables](#variables)
      - [Numbers](#numbers)
      - [Strings](#strings)
      - [Lists, Tuples and Sets](#lists-tuples-and-sets)
      - [Booleans](#booleans)
  - [User Input](#user-input)
  - [The 'in' Keyword](#the-in-keyword)
  - [Loops](#loops)
  - [List Comprehension](#list-comprehension)
  - [Dictionaries](#dictionaries)
      - [Dictionaries Comprehension](#dictionaries-comprehension)
  - [Destructuring Tuples](#destructuring-tuples)
  - [Functions](#functions)
      - [Lambda Functions](#lambda-functions)
      - [Unpacking/Destructuring Arguments](#unpackingdestructuring-arguments)
      - [Unpacking/Destructuring Keyword Arguments](#unpackingdestructuring-keyword-arguments)
  - [Object Oriented Programming](#object-oriented-programming)
      - [Magic Methods: '__str__' and '__repr__'](#magic-methods-str-and-repr)
      - [@classmethod and @staticmethod](#classmethod-and-staticmethod)
      - [Class Inheritance](#class-inheritance)
      - [Class Composition](#class-composition)
  - [Type Hinting](#type-hinting)
  - [Imports in Python](#imports-in-python)
  - [Errors](#errors)
      - [Custom Error Classes](#custom-error-classes)
  - [Decorators](#decorators)
  - [Mutability](#mutability)
  - [Transforming Folders into Modules](#transforming-folders-into-modules)
  - [Deploying to Heroku](#deploying-to-heroku)
      - [Add PostgreSQL to the App in Heroku](#add-postgresql-to-the-app-in-heroku)
  - [Deploy Flask App to your Own Server (DigitalOcean)](#deploy-flask-app-to-your-own-server-digitalocean)
  - [L10n (Localization) and i18n (Internationalization)](#l10n-localization-and-i18n-internationalization)
  - [Flask-Babel](#flask-babel)
  - [Werkzeug and wsgi](#werkzeug-and-wsgi)
  - [Database Migrations](#database-migrations)


## Python Refresher

### Variables

##### Numbers

[Summary](#summary)

Python has integers (15) and floats (9.99).

##### Strings

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

##### Lists, Tuples and Sets

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

##### Booleans

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

### User Input

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

### The 'in' Keyword

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

### Loops

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

### List Comprehension

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

### Dictionaries

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

##### Dictionaries Comprehension

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

### Destructuring Tuples

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

### Functions

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

##### Lambda Functions

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

##### Unpacking/Destructuring Arguments

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

##### Unpacking/Destructuring Keyword Arguments

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


### Object Oriented Programming

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

##### Magic Methods: '__str__' and '__repr__'

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

##### @classmethod and @staticmethod

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

##### Class Inheritance

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

##### Class Composition

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

### Type Hinting

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

### Imports in Python

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

### Errors

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

##### Custom Error Classes

[Summary](#summary)

```python
# you need to inherit from ValueError class so you have all the methods that you need and also to be able to be raised
class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return (
            f'<Book {self.name}, read{self.pages_read} pages out of {self.page_count}>'
        )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f'You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages.')
        self.pages_read += pages
        print(f'You have now read {self.pages_read} pages out of {self.page_count}.')

python101 = Book('Python 101', 50)
python101.read(35)
python101.read(10)
python101.read(30)
```

### Decorators

[Summary](#summary)

```python
user = {'username': 'jose', 'access_level': 'guest'}

# unprotected route
def get_admin_password():
    return '1234'

# create decorator to protect the route
def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

# With The '@' syntax
def make_secure1(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

# just add the '@' and the decorator function name to secure this route and then call it
@make_secure1
def get_admin_password1():
    return '1234'

print(get_admin_password1())

# it will return the name as 'secure_function' and any documentation from get_admin_password1 would be lost and replaced with the secure_function
print(get_admin_password1.__name__)

# in order to fix this, we need to import functools and add the decorator before the secure_function
import functools

def make_secure2(func):         # decorator
    @functools.wraps(func)          #it will protect the name and documentation of the 'func', in this case, the get_admin_password
    def secure_function():          # function that will replace the other one
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

@make_secure2
def get_admin_password2():
    return '1234'

print(get_admin_password2.__name__)
```

```python
# Decorators with Arguments => in order to pass arguments to the decorating function and still be able to use for several different functions, we should always add '*args, **kwargs' to the function that is the replacement:
def make_secure3(func):   
    @functools.wraps(func)          
    def secure_function(*args, **kwargs):  
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permissions for {user['username']}'
    return secure_function

@make_secure3
def get_admin_password3(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'

print(get_admin_password3('billing'))

# Decorators with Parameters => in order to pass parameters to the decorator itself, you need to create another decorator for the decorator, in other words, another level.
def factory(access_level):
    def decorator(func):   
        @functools.wraps(func)          
        def secure_function(*args, **kwargs):  
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No {access_level} permissions for {user['username']}'
        return secure_function
    return decorator

@factory('admin')
def get_admin_password4():
        return 'admin: 1244'

@factory('user')
def get_dashboard_password4():
        return 'user: user_password'

print(get_admin_password4())
```

### Mutability

[Summary](#summary)

Most things in python are mutable, except for:
- Tuples
- Strings
- Integers
- Booleans

Every time you redefine the above you will be redefining, not changing the actual value. Ex.
```python
a = 50
b = a

print(id(a) == id(b))       # true

a = 55

print(id(a) == id(b))       # false
print (a)                   # 55
print (b)                   # 50
```

**Note**: never pass mutable default parameters because the class or function is analysed in the beginning and it will make the parameter to save the reference to the mutable object. Then, you will have a problem if you run it again, since the reference will still be the same. Ex.
```python
from typing import List

class Student:
                                            # this is BAD
    def __init__(self, name: str, grades: List[int] = []):
        self.name = name
        self.grades = grades
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student('Bob')
matt = Student('Matt')
bob.take_exam(90)
print(bob.grades)                   # [90]
print(matt.grades)                  # [90]

# to FIX it
from typing import List, Optional

class Student:
                                            # this is BAD
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student('Bob')
matt = Student('Matt')
bob.take_exam(90)
print(bob.grades)                   # [90]
print(matt.grades)                  # []
```

### Transforming Folders into Modules

[Summary](#summary)

Inside the folder, create a file called: `__init__.py`

Note: `Models` is our internal representation of the entity and `Resources` is our external representation of our entity.

### Deploying to Heroku

[Summary](#summary)

1. Create `runtime.txt` in the root folder of your project and add the version of python `python-3.7.5`.
2. Create `requirements.txt` in the root folder of your project and add the libraries you are using. Also add `uwsgi`.
   ```
    Flask
    Flask-RESTful
    Flask-JWT
    Flask-SQLAlchemy
    uwsgi
   ```
3. Create `uwsgi.ini` in the root folder of your project and add the configs:
   ```
    [uwsgi]
    http-socket = :$(PORT)              // it will read the port from heroku
    master = true                       // we will be using the master process
    die-on-term = true                  // to liberate resources
    module = app:app                    // module is app.py and the variable is app
    memory-report = true
   ```
4. Create `Procfile` to declare the type of dyno and config:
   ```
    web: uwsgi uwsgi.ini                // type of dyno is web and we are going to run uwsgi with the config os uwsgi.ini
   ```
5. Separate the db from the app file creating the file `run.py` and cut from the app and paste the db there:
    ```python
    from app import app
    from db import db

    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all
    ```
6. Now, on the uwsgi change the module config:
   ```
    module= run:app                     // module is run.py and the variable is app
   ```

##### Add PostgreSQL to the App in Heroku

[Summary](#summary)

1. Add `Heroku Postgres` as an add-on.
2. In config vars you will have the `DATABASE_URL` created automatically by Heroku Postgres.
3. In you app.py, you will have to change the `DATABASE_URI` config to use the heroku variable if on heroku
   ```python
    import os

        ...
    
    app.config['SQLALCHEMY_DATABASE_USI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
        ...
   ```
4. In the `requirements.txt` add the `psycopg2` library. It is a very popular library used to interact with postgres.

### Deploy Flask App to your Own Server (DigitalOcean)

[Summary](#summary)

In `DigitalOcean` droplets are servers that you own. So, whenever we want to deploy a new server, you need to click `create droplet`.

There, you will have to choose the image, usually `Ubuntu - 16.04`. Choose the size you want, you don't need block storage, and choose a datacenter region (choose the one closest to your users).

Select your additional options, add your SSH keys (if you add you will always have to connect from that same computer), choose your hostname and tag and create.

Click more and access console, add password you received by email.

(...continue)

### L10n (Localization) and i18n (Internationalization)

[Summary](#summary)

The numbers come from the amount of characters that are between the L and the n and the i and the n.

**Localization** means 'what would the product look like if you were native to this market?'
    - You would have to adapt graphics
    - modify content (translation, changing layout, images, colors)
    - Convert to local units and currencies
    - Use local format for dates, addresses, phones, etc.

**Internationalization** is teh proces of planning and implementing a product so it can be localized.
- Implementing a feature that lets us add new languages - the act of translating is not **internationalization**, adding the feature is.
- Making sure your app support dates to be formatted in different ways to suit different markets
- Having the capability to adhere to local legal regulations (e.g. GDPR)
- Cookie legal regulations

**Locale** are the localities. Ex. the 'English' language is not all the same everywhere. We have different locales:
- British English: en-gb
- American English: en-us

Note: some markets can have multiple languages. Ex. Canada has en-ca (english) and fr-ca (french).

**Translation** is the process of re-writing string form one locale into another. Normally done by professional translators or native speakers.

In many software-only products (ex. libs), normally the usage of American English is enough

In user-facing application, you'll normally want to make they feel more welcome translating the strings.

**NOTE**: **Caching** means temporarily storing a piece of data that is being used multiple times, so it doesn't need to be regenerated or retrieved many times.

### Flask-Babel

[Summary](#summary)

Library that helps with internationalization of an app. It supports date formatting with timezone and `gettext` translations.

It can also look into your jinja template and check what else needs to be localized.

### Werkzeug and wsgi

[Summary](#summary)

User makes request to your server (let's assume `nginx`)
And `nginx` talks with your app's server
When we run locally, we do app.run(), and that starts the Flask's built-in server (provided by Werkzeug).
When we run on a production deployment, Flask's guilt-ind server is usually not fast enough, so normally we use `uWSGI` or `gunicorn`.
So, `nginx` talks with `uWSGI` and `uWSGI` talks with the app.

Flask's Built-in server uses `Werkzeug`. `Werkzeug` provides a `WSGI middleware` and a whole bunch of other functionality. The `WSGI middleware` is a development server (which is not the fastest).

`WSGI` is not a program. Is a protocol which dictates how applications forward requests to other applications and receive responses.

`uwsgi` is another protocol, but is faster, and `uWSGI` is a program that uses `uwsgi` protocol, and is also optimized for production.

`WSGI` stands for Web Server Gateway Interface (PEP-333 and PEP-3333) and if you want to be compliant with it you need your application to have 2 parts:
- gateway - receives data
- application - uses data, including forwarding
  

Flask apps are WSGI apps, they have a gateway to receive data and then they use it (ex. in resources)

Werkzeug's development server is alo a WSGI app. It receives data and forwards it to the Flask app.

`WSGI Middleware` are WSGI applications that take data and forward it somewhere.

Werkzeug is a WSGI utility library, and it provides a WSGI middleware. It is a python app that is a WSGI app, but it's not the end of the WSGI chain. Instead of using the data and returning a response, it forwards the data to the next layer. You can have many chained middlewares, like routing, load balancing, post-processing, caching, etc. Werkzeug does a lot of this for us, so often we don't need any more middlewares.

### Database Migrations

[Summary](#summary)

In order to deal with db migrations, you have to `pipenv install Flask_Migrate`. This will also install `Alembic`.

Then, on the app.py:

```python
from flask_migrate import Migrate

...

# after loading dotenv and adding the configs
migrate = Migrate(app, db)
```

1. Then, on your virtual environment in the terminal: `flask db init`

2. Then run `flask db migrate -m "<message>"` to pre-create the tables.
   
3. Now change the constant name on the version file in 2 places:
   ```
    def upgrade():
        # ### commands auto generated by Alembic - please adjust! ###
        op.add_column('users', sa.Column('email', sa.String(length=80), nullable=False))
        op.create_unique_constraint(<HERE>, 'users', ['email'])     <----- HERE
        # ### end Alembic commands ###


    def downgrade():
        # ### commands auto generated by Alembic - please adjust! ###
        op.drop_constraint(<HERE>, 'users', type_='unique')         <----- HERE
        op.drop_column('users', 'email')
        # ### end Alembic commands ###
    ```


4. Then run `flask db upgrade` to create the tables on postgres.

5. Whenever you have to run a migration again, just return from number 2.
   
6. If you want to know what version you are, you can run `SELECT * FROM alembic_version` on your postgres.
   
7. If you want to downgrade to a previous version, you need to run `flask db downgrade`. NOTE: if you did not named the constants (#3), you will have to get the name that postgres created on the db configs.

##### Problems while migrating

[Summary](#summary)

Some problems that can happen:
- Not being at the latest version => `flask db upgrade`
- Column deleted on the db directly, instead of using migrations to do it.
- If you ever want to delete all and restart, just delete all the versions and drop the db, then run everything again.

**NOTE**: migrations are not backup! Always backup your dbs!

## Flask Apps Contexts

[Summary](#summary)

There are mainly 3 contexts within a Flask app:
1. Configuration Context - where we configure our app. Change everything here, because the app is not running. We are not supposed to change the app's configuration when we start running the app.
2. App Context - app is ready, when we start running the app, we will enter the app context.
3. Request Context - when we receive the first request, we enter the request context

```python
from flask import Flask

app = Flask (__name__)

# Configuration Context
    ## Add Configurations
app.config['FOO'] = 'bar' 
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DB_URI'] = 'mysql:///...'        # libraries have the prefix

    ## Register Routes
@app.route('/')
def function():
    ...

app.add_url_rule('/', function)         # another way to register routes

    ## Init Libraries

from flask_admin import Admin
Admin.init_app(app)

    ## Register Blueprints
app.register_blueprints(...)

    ## Add Hooks - to inject dependencies
@app.before_request(...)
@app.error_handler(...)

    ## Call other Factories
views.init_app(app)

# App Context
    ## Test the app
app.test_client

    ## Debug

    ## Import global objects from Flask (request, session, g)
        ### `request` brings all our requests
        ### `session` brings all our sessions
        ### `g` helps us to save state - AVOID using it! Don't use global on your program! But, if it really is necessary, please do it very well and controlled. It might create `data race` problems, for example.
from flask import current_app, g

    ## Some Hooks execution
        ### for example the `before_request` one.

# Request Context
    ## Use global objects from Flask (request, session, g)
from flask import request

request.args
request.form
```