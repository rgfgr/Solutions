"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attack_power".
_current_health skal være en privat attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attack_power.
Eksempel: _current_health=80 og attack_power=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attack_power.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
class Character:
    name: str
    max_health: int
    _current_health: int
    attack_power: int

    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.max_health = health
        self._current_health = health
        self.attack_power = attack_power

    def __repr__(self):
        return f"Name: {self.name}, Max health: {self.max_health}, Current health: {self._current_health}, Attack power: {self.attack_power}"

    def hit(self, target: 'Character'):
        print(f"{self.name} hits {target.name} for {self.attack_power} damage")
        target.get_hit(self.attack_power)

    def get_hit(self, attack_power: int):
        self._current_health -= attack_power

    def get_healed(self, heal_power: int):
        self._current_health += heal_power


class Healer(Character):
    heal_power: int

    def __init__(self, name: str, health: int, heal_power: int):
        super().__init__(name, health, 0)
        self.heal_power = heal_power

    def __repr__(self):
        return f"{super().__repr__()}, Heal power {self.heal_power}"

    def heal(self, target: 'Character'):
        print(f"{self.name} heals {target.name} for {self.heal_power} health")
        target.get_healed(self.heal_power)


hero1 = Character("Bozeto", 100, 20)
hero2 = Character("Andananda", 110, 24)
hero3 = Healer("DoctorX", 75, 15)
for hero in [hero1, hero2, hero3]:
    print(hero)
hero1.hit(hero2)
print(hero2)
hero3.heal(hero2)
print(hero2)
