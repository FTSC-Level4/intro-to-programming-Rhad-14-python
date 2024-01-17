# Exercise 1: Pizza toppings
prompt="\n What other toppings do you like in your pizza?"
prompt= "\n Press enter then type quit if you are done:"
while True: 
    topping=input(prompt)
    if topping !="quit": 
        print(f"{topping} is added to ypur pizza")
    else:
        break