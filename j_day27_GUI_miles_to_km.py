from tkinter import *


def convert():
    converted = float(user_input.get()) * 1.609
    converted_number.config(text=converted)


window = Tk()
window.title("My First GUI Program")
window.config(padx=20, pady=20)


user_input = Entry(width=10)
user_input.grid(column=1, row=0)


miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

equal_label = Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

converted_number = Label(text="0", font=("Arial", 12))
converted_number.grid(column=1, row=1)
converted_number.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)






window.mainloop()