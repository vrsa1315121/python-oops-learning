##### Today We will cover Inheritance Concepts 

# What is Inheritance
Inheritance allows one class to use the properties and methods of another class.
It is Parent and child relationship concepts 
Parent class ->>>> child class

# Why do we need inheritance in Python
We need inheritance in python mainly to reuse code and create a logical relationship between classes.

think of it like :
Parent Class = common things
Child Class = common things + its own special things 

Remember these 3 main Reasons 
-> Code Reusability
-> Reduce code Duplication
-> Extend / Override Behavior

# What is methods overriding
A child class provides its own implementation  of a methods thats already exists in the parent class, it is called method orveriding.

In Simple Words :
Parents has a method -> Child inherits it -> child change /redefine the methods

## Types of Inheritance
1- Single Inheritance
one parent -> one child
Animal -> Dog

simple parent and child realtionship

2- Multilevel Inheritance
Grandfather -> Parent ->child
Animal->Dog->Puppy

3- Multiple Inheritance
Multiple parents -> one child
Father ──┐
         ↓
       Child
         ↑
Mother ─┘

4- Hierarchical Inheritance
one parent -> multiple children
        Animal
       /      \
      ↓        ↓
    Dog       Cat

5- Hybrid Inheritance
Combination of two or more types of inheritance
        Animal
       /      \
      ↓        ↓
     Dog      Cat
       \      /
        ↓    ↓
        Hybrid

| Type             | Structure   |Example                 |
| ---------------- | ----------- |----------------------- |
| **Single**       | A → B       | Animal →Dog            |
| **Multilevel**   | A → B → C   | Animal → Dog →Puppy    |
| **Multiple**     | A + B → C   | Father + Mother →Child |
| **Hierarchical** | A → B, C    | Animal → Dog,Cat       |
| **Hybrid**       | Combination | Multiple +Hierarchical |


# MRO -> Method Resolution Order it supports Multiple inheritance
It tells Python
"When i call a method , in what order should i search the classes to find that method"

# super()
It is used to access functionality from a parent class,commonly to call the parent constructor or parent implementation of overridden classes.





