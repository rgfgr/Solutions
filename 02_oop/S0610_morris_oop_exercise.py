"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0
        self.action = "none"

    def __repr__(self):
        return f"Sleepiness: {self.sleepiness}, Thirst: {self.thirst}, Hunger: {self.hunger}, Whisky: {self.whisky}, Gold: {self.gold}, Action: {self.action}"

    def alive(self):
        return self.sleepiness <= 100 and self.thirst <= 100 and self.hunger <= 100

    def _valid(self):
        return self.sleepiness >= 0 and self.thirst >= 0 and self.hunger >= 0 and self.whisky >= 0 and self.gold >= 0

    def can_buy_whisky(self):
        return self.gold >= 1 and self.whisky < 10

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        self.action = "sleep"

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5
        self.action = "mine"

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2
        self.action = "eat"

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1
        self.action = "buy_whisky"

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1
        self.action = "drink"

    def play(self, turns):
        turn = 0
        while self.alive() and self._valid() and turn < turns:
            turn += 1
            if self.sleepiness >= 100:
                self.sleep()
            elif self.hunger >= 95:
                self.eat()
            elif self.whisky > 0 and self.thirst >= 85:
                self.drink()
            elif self.can_buy_whisky() and self.thirst >= 90:
                self.buy_whisky()
            else:
                self.mine()

            print(f"Turn: {turn}, Stats: {self}")

        self.action = "done" if self.alive() else "dead"

        print(self)


morris = Miner()

morris.play(1000)

print(morris.gold)