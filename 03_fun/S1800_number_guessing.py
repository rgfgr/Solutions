""" Opgave "Number guessing"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random

def check_if_invalid(input_guess: str):
    return not input_guess.isdecimal() or len(input_guess) != 4


print("Hej jeg generer et 4-cifret heltal og du skal gætte det. For hvert ciffer du gætter korrekt får du en hvid mønt, hvis cifferet er i den rigtige position er det en sort mønt")
number_to_guess = random.randint(1000, 9999)
guessed = False
guesses = 0
while not guessed:
    guesses += 1
    black = 0
    white = 0
    guess_input = input("Ind tast et 4-cifret heltal")
    if check_if_invalid(guess_input):
        print("Dette var ikke et 4-cifret heltal")
        continue
    str_to_guess = str(number_to_guess)
    if guess_input == str_to_guess:
        guessed = True
        continue
    for i in range(4):
        if guess_input[i] == str_to_guess[i]:
            black += 1
        elif guess_input[i] in str_to_guess:
            white += 1
    print(f"Du fik {black} sorte og {white} hvide mønter")
print(f"Du vandt på {guesses} gæt")
