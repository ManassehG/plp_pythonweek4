# README

## Introduction

This Python script demonstrates a simple implementation of a `Person` class. The `Person` class has attributes such as `name`, `age`, and `gender`, along with a method `introduce()` to introduce the person with their attributes.

## Usage

To use this script, follow these steps:

1. Open a Python environment.
2. Copy the code provided into your Python environment.
3. Execute the code.

```python
class Person:
    name = "Manasseh"
    age = 20
    gender = "Male"
    
    def introduce(self):
        print(f'Your name is {self.name}. You are {self.age} years old and gender is {self.gender}')
        
p1 = Person()

p1.introduce()


Output
Your name is Manasseh. You are 20 years old and gender is Male

