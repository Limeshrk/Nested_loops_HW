persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

def who_eats_what(persons, restaurants):
  for name in persons:
    for restaurant in restaurants:
      print(f"{name} eats {restaurant}")

who_eats_what(persons, restaurants)