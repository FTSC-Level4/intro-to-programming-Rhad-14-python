#Exercise 3: Glossary 2
Keywords= {"for": "this keyword creates loops",
           "del": "is used for deleting things in python",
           "true": "its an boolean expression that is used to evaluate",
           "false": "its also a boolean expression but the opposite of True",
           "if": "this keyword is uses if there is a condition",
           "int": "int is a whole number",
           "float": "float is a decimal number",
           "complex": "is made up of two values: the real and imaginary parts of a complex number",
           "str": "everyword is a character"}
for word, definition in Keywords.items():
    print(f"{word.title()}: {definition}")