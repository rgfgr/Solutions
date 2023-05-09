"""
Opgave "Animals"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop- og rpg1-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random


class Animal:
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"Name: {self.name}, Sound: {self.sound}, Height: {self.height}, Weight: {self.weight}, Legs: {self.legs}, Female: {self.female}"

    def make_noise(self):
        print(self.sound)


class Dog(Animal):
    def __init__(self, name: str, height: float, weight: float, female: bool, tail_length: float, hunts_sheep: bool):
        super().__init__(name, "woof", height, weight, 4, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return f"{super().__repr__()}, Tail length: {self.tail_length}, Hunts sheep: {self.hunts_sheep}"

    def wag_tail(self):
        print(f"Hunden {self.name} vifter med sin {self.tail_length:.2f} cm lange hale")


def mate(mother: 'Dog', father: 'Dog', name: str) -> 'Dog':
    if not isinstance(mother, Dog) or not isinstance(father, Dog):
        raise ValueError("Both mother and father must be of type Dog")

    if not mother.female:
        raise ValueError("Mother must be female")

    if father.female:
        raise ValueError("Father must not be female")

    height_ratio = random.random()
    weight_ratio = random.random()
    tail_ratio = random.random()

    height = mother.height * height_ratio + father.height * (1 - height_ratio)
    weight = mother.weight * weight_ratio + father.weight * (1 - weight_ratio)
    tail = mother.tail_length * tail_ratio + father.tail_length * (1 - tail_ratio)
    female = random.random() < 0.5
    hunts = random.random() < 0.5

    return Dog(name, height, weight, female, tail, hunts)


test = Animal("no", "yes", 9, 9, 9, True)
print(test)
test.make_noise()

dog = Dog("Snoopy", 10, 10, False, 32, True)
print(dog)
dog.make_noise()
dog.wag_tail()

mom = Dog("Mom", 25, 10, True, 40, False)
dad = Dog("Dad", 10, 25, False, 20, True)
child = mate(mom, dad, "Child")

for animal in [dog, mom, dad, child]:
    print(animal)
    print(type(animal))
    animal.make_noise()
    animal.wag_tail()
