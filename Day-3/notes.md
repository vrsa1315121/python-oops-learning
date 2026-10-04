################# Polymorphism ###############
What is Polymorphism

Polymorphsim is an OOPS concepts where the same interface or method can have different implementation or behaviours
depending on the objects.

Polymorphism
│
├── Method Overriding
├── Duck Typing
├── Operator Overloading
└── Method Overloading

Python does not support traditional method overloading like Java/C++.

Instead, Python commonly uses:

default arguments
*args
**kwargs

Method Overriding:
When a child class provides its own implemenation of a methods that already exist in the parent class ,it is called method overriding.

Duck Typing:
"If it walks like a duck and quacks like a duck, treat it like a duck."

| Operator | Dunder method   |
| -------- | --------------- |
| `+`      | `__add__()`     |
| `-`      | `__sub__()`     |
| `*`      | `__mul__()`     |
| `/`      | `__truediv__()` |
| `==`     | `__eq__()`      |
| `<`      | `__lt__()`      |
| `>`      | `__gt__()`      |
| `len()`  | `__len__()`     |
| `str()`  | `__str__()`     |


Python does not support traditional method overloading based on different parameter lists. We can achieve similar behavior using default arguments or *args

Polymorphsim  + Inheritance
Inheritance
     ↓
Child gets parent method
     ↓
Child overrides method
     ↓
Polymorphism
