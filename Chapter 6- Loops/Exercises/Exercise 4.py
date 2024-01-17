# Exercise 4: Deli 
sandwiches_orders= ["Ham", "Nutella", "Roast beef ",  "Egg", "Chicken",]
finished_sandwiches=[]
while sandwiches_orders:
    current_sandwich= sandwiches_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I finished making {sandwich} sandwich.")
