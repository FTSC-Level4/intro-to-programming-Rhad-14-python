#Exercise 5: Changing guests lists 
guests= ["Abril","Angela", "Rence"]
name=guests[0].title()
print(f"{name}, thanks for confirming the invitation")
name=guests[1].title()
print(f"{name}, thanks for confiriming the invitation")
name=guests[2].title()
print(f"{name}, thanks for confirming the invitation")
name=guests[0].title()
print(f"\nSorry, {name} canceled the invitation")
#Abril canceled her invitation
del(guests[0])
guests.insert(0, "Hannah")
#Repeat the invitation again 
name=guests[0].title()
print(f"\n{name}, thanks for confirming the invitation")
name=guests[1].title()
print(f"{name}, thanks for confirming the invitation")
name=guests[2].title()
print(f"{name}, thanks for confirming the invitation")