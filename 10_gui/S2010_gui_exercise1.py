"""
Opgave "GUI step 1":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import tkinter as tk

main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

frame_1 = tk.LabelFrame(main_window, text="Container")
frame_1.grid(row=0, column=0, padx=8, pady=4, sticky=tk.N)

frame_2 = tk.Frame(frame_1)
frame_2.grid(row=0, column=0, padx=25, pady=10)

label = tk.Label(frame_2, text="Id")
label.grid(row=0, column=0, padx=10, pady=2)

entry = tk.Entry(frame_2, width=4)
entry.grid(row=1, column=0, padx=10, pady=2)

button = tk.Button(frame_1, text="Create")
button.grid(row=1, column=0, padx=25, pady=10)

if __name__ == "__main__":
    main_window.mainloop()
