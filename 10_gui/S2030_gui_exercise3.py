"""Opgave "GUI step 3":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2030.png

Genbrug din kode fra "GUI step 2".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                treeview and scrollbar
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).


Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import tkinter as tk
from tkinter import ttk

# region Variables
button_padx = 10
button_pady = 5

entry_n_label_padx = 3
entry_n_label_pady = 5

label_padx = 5
label_pady = 5

entry_padx = 5
entry_pady = 5

row_height = 24
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#773333"
# endregion

def clear_entry_boxes():
    print("Clearing entry boxes")
    id_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    weather_entry.delete(0, tk.END)
    print("Entry boxes cleared")


main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("500x500")

label_frame = tk.LabelFrame(main_window, text="Container")
label_frame.grid(row=0, column=0, padx=8, pady=4, sticky=tk.N)

# region Treeview stuff

treeview_frame = tk.Frame(label_frame)
treeview_frame.grid(row=0, column=0, padx=10, pady=5)
style = ttk.Style()
scrollbar = tk.Scrollbar(treeview_frame)
treeview = ttk.Treeview(treeview_frame, yscrollcommand=scrollbar.set, selectmode="browse")

# region Style stuff
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=row_height, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])
# endregion

# region Scrollbar stuff
scrollbar.grid(row=0, column=1, padx=0, pady=0, sticky='ns')
scrollbar.configure(command=treeview.yview)
# endregion

# region Treeview stuff
treeview.grid(row=0, column=0, padx=0, pady=0)
treeview['columns'] = ("Id", "Weight", "Destination")
treeview.column("#0", width=0, stretch=tk.NO)
treeview.column("Id", anchor=tk.E, width=40)
treeview.column("Weight", anchor=tk.W, width=80)
treeview.column("Destination", anchor=tk.W, width=220)

treeview.heading("#0", text="", anchor=tk.W)
treeview.heading("Id", text="Id", anchor=tk.CENTER)
treeview.heading("Weight", text="Weight", anchor=tk.CENTER)
treeview.heading("Destination", text="Destination", anchor=tk.CENTER)
# endregion

# endregion

# region Entry and label stuff
entry_n_label_frame = tk.Frame(label_frame)
entry_n_label_frame.grid(row=1, column=0, padx=15, pady=10)

id_frame = tk.Frame(entry_n_label_frame)
weight_frame = tk.Frame(entry_n_label_frame)
destination_frame = tk.Frame(entry_n_label_frame)
weather_frame = tk.Frame(entry_n_label_frame)

id_frame.grid(row=0, column=0, padx=entry_n_label_padx, pady=entry_n_label_pady)
weight_frame.grid(row=0, column=1, padx=entry_n_label_padx, pady=entry_n_label_pady)
destination_frame.grid(row=0, column=2, padx=entry_n_label_padx, pady=entry_n_label_pady)
weather_frame.grid(row=0, column=3, padx=entry_n_label_padx, pady=entry_n_label_pady)

# region Label stuff
id_label = tk.Label(id_frame, text="Id")
weight_label = tk.Label(weight_frame, text="Weight")
destination_label = tk.Label(destination_frame, text="Destination")
weather_label = tk.Label(weather_frame, text="Weather")

id_label.grid(row=0, column=0, padx=label_padx, pady=label_pady)
weight_label.grid(row=0, column=0, padx=label_padx, pady=label_pady)
destination_label.grid(row=0, column=0, padx=label_padx, pady=label_pady)
weather_label.grid(row=0, column=0, padx=label_padx, pady=label_pady)
# endregion

# region Entry stuff
id_entry = tk.Entry(id_frame, width=5)
weight_entry = tk.Entry(weight_frame, width=10)
destination_entry = tk.Entry(destination_frame)
weather_entry = tk.Entry(weather_frame, width=15)

id_entry.grid(row=1, column=0, padx=label_padx, pady=label_pady)
weight_entry.grid(row=1, column=0, padx=label_padx, pady=label_pady)
destination_entry.grid(row=1, column=0, padx=label_padx, pady=label_pady)
weather_entry.grid(row=1, column=0, padx=label_padx, pady=label_pady)
# endregion

# endregion

# region Button stuff
button_frame = tk.Frame(label_frame)
button_frame.grid(row=2, column=0, padx=30, pady=5)

create_button = tk.Button(button_frame, text="Create")
update_button = tk.Button(button_frame, text="Update")
delete_button = tk.Button(button_frame, text="Delete")
clear_button = tk.Button(button_frame, text="Clear Entry Boxes", command=clear_entry_boxes)

create_button.grid(row=0, column=0, padx=button_padx, pady=button_pady)
update_button.grid(row=0, column=1, padx=button_padx, pady=button_pady)
delete_button.grid(row=0, column=2, padx=button_padx, pady=button_pady)
clear_button.grid(row=0, column=3, padx=button_padx, pady=button_pady)
# endregion

if __name__ == "__main__":
    main_window.mainloop()
