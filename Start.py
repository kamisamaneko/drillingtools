import tkinter as tk

window = tk.Tk()
window.title("Driling Trajectory and Survey Builder")
window.geometry("400x400")

# LABEL
title = tk.Label(text="Hello World, Welcome to CS50")
title.grid(column=0, row=0)

#BUTTON
button1 = tk.Button(text="Click Me", bg="red")
button1.grid(column=0, row=1)

#ENTRY Field 1
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

text_field = tk.Text(master=window, height= 10 , width=30)
text_field.grid(column=0, row=2)




window.mainloop()