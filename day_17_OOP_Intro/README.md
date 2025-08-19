# Day 17: Intro to OOP - Classes & Objects 🧠

Welcome to Day 17\! Today, we're shifting our thinking to a new programming paradigm: **Object-Oriented Programming (OOP)**. Instead of just writing functions and scripts, OOP allows us to model our code around real-world concepts or "objects." This makes our programs more structured, reusable, and easier to maintain.


### The Core Concepts of OOP

OOP is built on four pillars, which we will explore over the next few days. Today, we'll focus on the two most fundamental concepts: **Classes** and **Objects**.

#### 1\. Classes: The Blueprint

A **Class** is a blueprint or a template for creating objects. It defines the properties (data) and behaviors (functions) that all objects of that type will have.

  * **Analogy:** A Class is like the blueprint for a car. It defines that all cars have a color, a model, and an engine, and that they all have the ability to drive and brake.
  * **Example:**
    ```python
    # The 'Car' class is the blueprint.
    class Car:
        pass # The 'pass' keyword means we're intentionally leaving the class empty for now.
    ```

#### 2\. Objects: The Instance

An **Object** is a specific, tangible instance of a class. You can create many objects from a single class blueprint, each with its own unique data.

  * **Analogy:** An Object is a specific car built from the blueprint. It's a real, physical car that has a unique color (red), a specific model (Mustang), and a real engine.
  * **Example:**
    ```python
    # 'my_car' and 'your_car' are objects (instances) of the Car class.
    my_car = Car()
    your_car = Car()
    ```


### Anatomy of a Class: Attributes & Methods

Classes contain two main components that define the nature of the objects they create.

#### 1\. Attributes (Data)

**Attributes** are the variables that belong to an object. They store the data or state of the object. They are defined inside the `__init__` method.

  * **Analogy:** For a `Car` object, the attributes would be `self.make`, `self.model`, and `self.year`.
  * **Example:**
    ```python
    class Car:
        # The __init__ method is a special method called the constructor.
        # It's automatically called when an object is created.
        def __init__(self, make, model):
            self.make = make   # 'make' is an attribute of the object
            self.model = model # 'model' is an attribute of the object
    ```

#### 2\. Methods (Behaviors)

**Methods** are the functions that belong to an object. They define what the object can do. A method always takes `self` as its first parameter, which refers to the specific object the method is being called on.

  * **Analogy:** For a `Car` object, the methods could be `start_engine()`, `drive()`, or `honk()`.
  * **Example:**
    ```python
    class Car:
        def __init__(self, make, model):
            self.make = make
            self.model = model
            
        # This is a method that describes the car's behavior.
        def display_info(self):
            print(f"This is a {self.make} {self.model}.")
    ```

### Putting it All Together: The `__init__` Method (The Constructor)

The `__init__` method is the heart of a class. It's automatically called whenever you create a new object from that class. Its purpose is to **initialize** the object's attributes with the values you pass in.

  * `self`: The first parameter of every method (including `__init__`) is `self`. It's a reference to the specific object that is being created or is calling the method.
  * **Full Code Example:**
    ```python
    class Dog:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed
            self.is_hungry = True

        def speak(self):
            print(f"{self.name} says Woof!")

    # Creating objects automatically calls __init__
    my_dog = Dog("Buddy", "Golden Retriever")
    my_dog.speak()
    ```

### 📝 Practice Exercises

1.  **Create a `Car` Class:**
      * Define a class named `Car`.
      * In the `__init__` method, give it attributes for `make`, `model`, and `year`.
      * Create a method called `display_info` that prints the car's `make`, `model`, and `year` in a single sentence.
2.  **Create `Car` Objects:**
      * Instantiate two different `Car` objects with unique attributes.
      * Call the `display_info` method on both objects.
3.  **Create a `Student` Class:**
      * Define a class named `Student` with attributes for `name`, `age`, and `grade`.
      * Add a method called `is_passing` that returns `True` if the student's `grade` is 70 or higher, and `False` otherwise.

### ✨ Best Practices & Professional Notes

  * **Use Classes for Complex Data:** While dictionaries are great for simple key-value pairs, classes are better when you need to store data *and* define the behaviors that apply to that data.
  * **Encapsulation:** OOP promotes **encapsulation**, which means bundling the data (attributes) and methods that operate on the data into a single unit (the object). This is a core tenet of writing clean, maintainable code.
  * **Naming Conventions:** Class names should always be in `PascalCase` (e.g., `MyClass`), while method and attribute names should be in `snake_case` (e.g., `my_method`).

### 🏃 How to Run This Code

1.  Open your terminal or command prompt.
2.  Navigate to the `Day_17_OOP_Intro` directory.
    ```bash
    cd path/to/your/fluffy-python/Day_17_OOP_Intro
    ```
3.  Run the script using:
    ```bash
    python oop_intro.py
    # Or if you installed python3:
    # python3 oop_intro.py
    ```

### ➡️ What's Next?

Tomorrow, on Day 18, we'll continue our OOP journey by exploring **Inheritance**, which allows classes to inherit properties from other classes.
