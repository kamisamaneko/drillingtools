import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()




# from tkinter import *
# import tkinter.messagebox
#
# # def doNothing():
# #     print("Ok OK Nothing to do")
#
# root = Tk()
#
# canvas = Canvas(root, width=200, height=100)
# canvas.pack()
#
# blackline = canvas.create_line(0,0,200,50)
# redline = canvas.create_line(0,100,200,50, fill='blue')
#
# #canvas.delete(ALL)
#
#
# root.mainloop()

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
# two = Label(root, text="Two", bg="green", fg="white")
# two.pack(fill=X)
# three = Label(root, text="blue", bg="green", fg="white")
# three.pack(side=LEFT, fill=Y)

# label_1 = Label(root, text="Name")
# label_2  = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1, sticky=E)
#
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# c = Checkbutton(root, text="Keep Me Logged In")
# c.grid(columnspan=2)

# def printname(event):
#     print("Hello my name is Bucky")
#
# button_1 = Button(root, text="Print Name")
# button_1.bind("<Button-1>", printname)
# button_1.pack()

# def leftClick(event):
#     print("Left")
#
# def middleClick(event):
#     print("Midle")
# def rightClick(event):
#     print("Right")
#
# frame = Frame(root, width=1800, height=250)
# frame.bind("<Button-1>",leftClick)
# frame.bind("<Button-2>",middleClick)
# frame.bind("<Button-3>",rightClick)
# frame.pack()


# class BuckyButton:
#
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         self.printButton = Button(frame, text="Print Message", command= self.printMessage)
#         self.printButton.pack(side=LEFT)
#         self.quitButton = Button(frame, text="Quit", command= frame.quit)
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self):
#         print("yuhuuu its working")
#
#
# root = Tk()
# b=BuckyButton(root)

#### Main Menu####
# menu = Menu(root)
# root.config(menu=menu)
#
# submenu = Menu(menu)
# menu.add_cascade(label="File", menu=submenu)
# submenu.add_command(label="New Project", command=doNothing)
# submenu.add_command(label="Now", command=doNothing)
# submenu.add_separator()
# submenu.add_command(label="Exit", command=menu.quit)
#
# editmenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editmenu)
# editmenu.add_command(label="Lalalal", command=doNothing)
# editmenu.add_command(label="hehhee", command=doNothing)
# editmenu.add_separator()
# #### Tool Bar ####
#
# toolbar = Frame(root, bg="blue")
# insertButt = Button(toolbar, text="Insert Image", command=doNothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
# printButt = Button(toolbar, text="Print", command=doNothing)
# printButt.pack(side=LEFT, padx=2, pady=2)
#
# toolbar.pack(side=TOP, fill=X)
#
# #############Status Bar###############
#
# status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)

# tkinter.messagebox.showinfo("window title", "Monkey Monkey")
#
# answer = tkinter.messagebox.askquestion("question 1", 'Do you like')
#
# if answer == 'yes':
#     print('8====D-')
