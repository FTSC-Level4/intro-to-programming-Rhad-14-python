#Exercise 5: Pets
#empty lists of pets
pets=[]
# pets and their owner
pet={
    "animal type": "cat",
    "name": "Whiskers",
    "owner": "Abril",
    "weight": 20,
    "eats": "curtains"
}
pets.append(pet)
pet={
    "animal type": "rabbit",
    "name": "Oreo",
    "owner": "Angela", 
    "weight": 6, 
    "eats": "grass"
}
pets.append(pet)
pet= {
    "animal type": "dog",
    "name": "Hanabi",
    "owner": "Tyler",
    "weight": 20, 
    "eats": "slippers"
}
# The information about each pets 
for pet in pets:
    print(f"\n The information about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}:{value}")
