zoo = ("panther", "bobcat", "tiger", "panda", "meerkat",
       "flamingo", "elephant", "giraff", "lion", "gazelle")
print(zoo.index("meerkat"))

animal_to_find = "lion"
if animal_to_find in zoo:
    print(f"You can find a {animal_to_find} in the zoo.")

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal,
 sixth_animal, seventh_animal, eigth_animal, ninth_animal, tenth_animal) = zoo
print(first_animal)
print(second_animal)
print(third_animal)
print(fourth_animal)
print(fifth_animal)
print(sixth_animal)
print(seventh_animal)
print(eigth_animal)
print(ninth_animal)
print(tenth_animal)

ZooList = list(zoo)
print(ZooList)

NewAnimals = ["turtle", "goat", "gibbon"]
ZooList.extend(NewAnimals)
print(ZooList)

zoo = tuple(ZooList)
print(zoo)
