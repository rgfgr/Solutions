"""Opgave "Number pyramid"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
Funktionen har en parameter, der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række og også deres sum.

I hovedprogrammet kalder du funktionen med fx 7 som argument.

Tilføj en mere generel funktion pyramid2.
Denne funktion har som andet parameter en liste med tallene i
pyramidens øverste række.

I hovedprogrammet kalder du pyramid2 med 1, 2, 3, ..., 10 som det første argument
og en liste med tal efter eget valg som det andet argument.
Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne S1620_pyramid_help.py og starte derfra

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
def pyramid(lines):
    pyramid2(lines, [1, 1])


def pyramid2(lines, numbers):
    if lines > 500:
        pyramid_iterative(lines, numbers)
    else:
        pyramid_recursive(lines, numbers)


def pyramid_iterative(lines, numbers):
    numbers2 = [i for i in numbers]
    for line in range(lines):
        print("row " + str(line+1), end=": ")
        print(numbers2)
        index_shift = 0
        for n in range(len(numbers)-1):
            if numbers[n] + numbers[n + 1] == line + 2:
                numbers2.insert(n + index_shift + 1, line + 2)
                index_shift += 1
        numbers = [i for i in numbers2]


def pyramid_recursive(lines, numbers):
    if lines == 0:
        return numbers
    numbers = pyramid_recursive(lines - 1, numbers)
    numbers2 = [i for i in numbers]
    print("row " + str(lines), end=": ")
    print(numbers2)
    index_shift = 0
    for n in range(len(numbers) - 1):
        if numbers[n] + numbers[n + 1] == lines + 1:
            numbers2.insert(n + index_shift + 1, lines + 1)
            index_shift += 1
    return numbers2


pyramid2(10, range(10))
pyramid2(499, [1, 1, 1])
