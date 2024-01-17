# Exercise 5: No pastrami
sandwiches_orders= ["Ham","pastrami", "Nutella", "Roast beef ","pastrami", "Egg", "Chicken", "pastrami",]
finished_sandwiches=[]
print("I'm sorry we ran out of pastrami.")
while "pastrami" in sandwiches_orders: 
    sandwiches_orders.remove("pastrami")
print("\n")
while sandwiches_orders:
    current_sandwich= sandwiches_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I finished making your {sandwich} sandwich.")
