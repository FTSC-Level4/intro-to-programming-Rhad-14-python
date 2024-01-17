#Exercise 2: Movie Tickets
words= "\n Type your age please"
words += "\n Press enter then type quit if your done"
while True:
    age= input(words)
    if age == "quit":
        break
    age = int(age)
    if age < 3: 
        print("Your ticket cost nothing")
    elif age < 13: 
        print("Your ticket cost $10")
    else: 
        print("Your tickest cost $15")