import random
import tkinter as tk

window = tk.Tk()
window.title("Greetings _____")
window.geometry("400x400")

#function

def phrase_generator():

    phrases = ["Hello", "What's up", "Aloha", "Hafa Adai"]
    name = str(entry1.get())
    return phrases[random.randint(0,3)] + name

def phrase_display():
    greeting = phrase_generator()

    # create text field
    greeting_display = tk.Text(master=window, height=10, width = 30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)


#Label
label1 = tk.Label(text="welcome dude")
label1.grid(column = 0, row = 0)

#label2
label2 = tk.Label(text="what is your name")
label2.grid(column = 0, row =1)

#Entry Fields
entry1 = tk.Entry()
entry1.grid(column = 1, row=1)

#Button 1
button1 = tk.Button(text="click me", command=phrase_display)
button1.grid(column=0, row=2)





window.mainloop()