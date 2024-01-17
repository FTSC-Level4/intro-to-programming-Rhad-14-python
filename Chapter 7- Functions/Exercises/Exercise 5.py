#Exercise 5: Cities
def describe_city(city, country = "japan"):
    """Describe a city"""
    message = f"{city.title()} can be found in {country.title()}"
    print(message)
describe_city('Hiroshima')
describe_city('Beijing', 'China')
describe_city('tokyo')