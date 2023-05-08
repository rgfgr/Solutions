"""
Opgave "Tom the Turtle":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.


def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # you will need this: x-value: turtle_name.position()[0]
    # and this:           y-value: turtle_name.position()[1]
    x = turtle_name.position()[0]
    y = turtle_name.position()[1]
    return -480 < x < 480 and -480 < y < 480


def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


def squarer(length, tom):
    tom.pendown()
    for x in range(4):
        tom.forward(length)
        tom.right(90)
    tom.penup()


def square(length):
    squarer(length, turtle.Turtle())


def many_squares(amount, length, distance):
    tom = turtle.Turtle()
    tom.penup()
    while amount > 0:
        if not visible(tom):
            tom.home()
        tom.forward(length + distance)
        squarer(length, tom)
        amount -= 1


def spiral_square(length, rotation, speed):
    print(rotation)
    rotation = rotation % 360
    print(rotation)
    tom = turtle.Turtle()
    tom.speed(speed)
    while length > 0:
        print(length)
        tom.forward(length)
        tom.right(rotation)
        length -= 1
    turtle.done()


def draw_edges(amount, length, rotation, tom):
    print(rotation)
    while amount > 0:
        tom.forward(length)
        tom.right(rotation)
        amount -= 1


def draw_stars(stars=None):
    if stars is None:
        stars = [5, 7, 11]
    tom = turtle.Turtle()
    tom.penup()
    tom.backward(200)
    tom.left(90)
    tom.forward(100)
    tom.right(90)
    for star in stars:
        print(star)
        tom.right(90)
        tom.left(180 / star / 2)
        tom.pendown()
        draw_edges(star, 100, 180 - (180 / star), tom)
        tom.penup()
        tom.right(180 / star / 2)
        tom.left(90)
        tom.forward(100)


draw_stars()
