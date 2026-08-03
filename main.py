from tkinter import *

def button_clicked():
    # print(text_input.get())
    miles = int(text_input.get())
    # print(miles)
    km = str(round(miles * 1.60934, 1))
    # print(km)
    km_answer.config(text=km)

window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(500, 300)
window.config(padx=20, pady=20)

#Labels
miles_label = Label(window, text="Miles")
miles_label.grid(column=2, row=0)
inter_label = Label(window, text="is equal to")
inter_label.grid(column=0, row=1)
km_label = Label(window, text="Km")
km_label.grid(column=2, row=1)
km_answer = Label(window, text="0")
km_answer.grid(column=1, row=1)

#Button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

#Entry
text_input = Entry(width=10)
text_input.insert(END, "0")
text_input.grid(column=1, row=0)



window.mainloop()
