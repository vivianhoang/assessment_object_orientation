"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    a) Abstraction - we don't need to know any info a method uses internally,
                     as it hides the complexity of the code.

    b) Encapsulation - we can have all the code in one object so it has everything
                       in one place.

    c) Polymorphism - we can have the flexibility of types without conditionals,
                      more specificially we can redefine methods from classes

2. What is a class?
   A class is a type of string or file which can be used as a template for creating
   objects where we can provide our initial values.

3. What is an instance attribute?
   An instance attribute is where a subclass has a declared attribute that may
   or may not be unique compared to the superclass.

4. What is a method?
   A method is a function that is within a class.

5. What is an instance in object orientation?
   An instance in object orientation is the instantiation of an attribute within
   the class. It is an object in memory.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute is shared by all instances, whereas an isntance attribute
   is unique to that instance.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Students(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Questions(object):
    def __init__(self, questions, correct_answer):
        self.questions = questions
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        self.answer = raw_input(self.questions)
        if self.answer == self.correct_answer:
            return True
        else:
            return False


class Exam(Questions):
    def __init__(self, name):
        self.name = name
        self.questions = []

    def QA(self, questions, correct_answer):
        return super(Exam, self).__init__(questions, correct_answer)

    def administer(self):
        score = 0
        return super(Exam, self).ask_and_evaluate()
