rivers= {"Rio de la plata": "South America",
         "Yellow river": "China",
         "Amazon river": "South America",
         "Ob river": "Russia",
         "Yenisei river": "Russia"}
for river, country in rivers.items():
    print(f"The {river.title()} can be found in {country.title()}.")
print("\n All the rivers in the following are in this data set")
for river in rivers.keys():
    print(f"- {river.title()}")
print("\n All the countries in the following are  in this set")
for country in rivers.values():
    print(f"- {country.title()}")
