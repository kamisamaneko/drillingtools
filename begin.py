import tkinter as tk
from tkinter import *
from tkinter import font  as tkfont # python 3

def clear():
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_3.delete(0,END)
    Entry_4.delete(0,END)
    Entry_5.delete(0,END)
    Entry_6.delete(0,END)
    Entry_7.delete(0,END)
    Entry_8.delete(0,END)
    Entry_9.delete(0,END)
    Entry_10.delete(0,END)
    Entry_11.delete(0,END)
    Entry_12.delete(0,END)
    Entry_13.delete(0,END)

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

        Button_Traj = tk.Button(text="Trajectory")
        Button_Survey = tk.Button(text="Survey")
        Button_Check = tk.Button(text="Check Point")
        Button_Cluster = tk.Button(text="Cluster")
        Button_Section = tk.Button(text="Section")
        Button_Built = tk.Button(text="Built")
        Button_Clear = tk.Button(text="Clear", command=clear)
        Button_Traj.grid(column=0, row=0)
        Button_Survey.grid(column=1, row=0)
        Button_Check.grid(column=2, row=0)
        Button_Cluster.grid(column=3, row=0)
        Button_Section.grid(column =0, row = 17)
        Button_Built.grid(column=2, row=17)
        Button_Clear.grid(column=3, row=17)

        Label_1 = tk.Label(text="Cluster = ")
        Label_1.grid(column=0, row = 1)

        Label_2 = tk.Label(text="Well API = ")
        Label_2.grid(column=0, row = 2)

        Label_3 = tk.Label(text="Starting Point")
        Label_3.grid(column=0, row = 3)

        Label_4 = tk.Label(text="Xo = ")
        Label_4.grid(column=0, row = 4)

        Label_5 = tk.Label(text="Yo = ")
        Label_5.grid(column=0, row =5 )

        Label_6 = tk.Label(text="Zo = ")
        Label_6.grid(column=0, row = 6)

        Label_7 = tk.Label(text="Target Point ")
        Label_7.grid(column=0, row =7 )

        Label_8 = tk.Label(text="Xt = ")
        Label_8.grid(column=0, row = 8)

        Label_9 = tk.Label(text="Yt = ")
        Label_9.grid(column=0, row = 9)

        Label_10 = tk.Label(text="Zt = ")
        Label_10.grid(column=0, row =10 )

        Label_11 = tk.Label(text="KOP = ")
        Label_11.grid(column=0, row = 11)

        Label_12 = tk.Label(text="Tolerance = ")
        Label_12.grid(column=0, row =12 )

        Label_13 = tk.Label(text="Calculation")
        Label_13.grid(column=0, row = 13)

        Label_14 = tk.Label(text="Methond = ")
        Label_14.grid(column=0, row =14 )

        Label_15 = tk.Label(text="Data Point = ")
        Label_15.grid(column=0, row =15 )

        Label_16 = tk.Label(text="Number Section = ")
        Label_16.grid(column=0, row =16 )

        Entry_1=tk.Entry()
        Entry_1.grid(column = 1, row = 1)

        Entry_2=tk.Entry()
        Entry_2.grid(column = 1, row = 2)

        Entry_3=tk.Entry()
        Entry_3.grid(column = 1, row = 4)

        Entry_4=tk.Entry()
        Entry_4.grid(column = 1, row = 5)

        Entry_5=tk.Entry()
        Entry_5.grid(column = 1, row = 6)

        Entry_6=tk.Entry()
        Entry_6.grid(column = 1, row = 8)

        Entry_7=tk.Entry()
        Entry_7.grid(column = 1, row = 9)

        Entry_8=tk.Entry()
        Entry_8.grid(column = 1, row = 10)

        Entry_9=tk.Entry()
        Entry_9.grid(column = 1, row =11)

        Entry_10=tk.Entry()
        Entry_10.grid(column = 1, row = 12)

        Entry_11=tk.Entry()
        Entry_11.grid(column = 1, row = 14)

        Entry_12=tk.Entry()
        Entry_12.grid(column = 1, row = 15)

        Entry_13=tk.Entry()
        Entry_13.grid(column = 1, row = 16)


        variable1 = StringVar(window1)
        variable1.set("ft")
        listbox = OptionMenu(window1,variable1,"ft","m")
        listbox.grid(column = 2, row=11)

        variable2 = StringVar(window1)
        variable2.set("ft")
        listbox = OptionMenu(window1,variable2,"ft","m")
        listbox.grid(column = 2, row=12)

        variable3 = StringVar(window1)
        variable3.set("ft")
        listbox = OptionMenu(window1,variable3,"ft","m")
        listbox.grid(column = 2, row=11)


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

# window1 = tk.Tk()
# # window1.geometry("640x480")
#
# #Top Menu
# Button_Traj = tk.Button(text="Trajectory")
# Button_Survey = tk.Button(text="Survey")
# Button_Check = tk.Button(text="Check Point")
# Button_Cluster = tk.Button(text="Cluster")
# Button_Section = tk.Button(text="Section")
# Button_Built = tk.Button(text="Built")
# Button_Clear = tk.Button(text="Clear", command=clear)
# Button_Traj.grid(column=0, row=0)
# Button_Survey.grid(column=1, row=0)
# Button_Check.grid(column=2, row=0)
# Button_Cluster.grid(column=3, row=0)
# Button_Section.grid(column =0, row = 17)
# Button_Built.grid(column=2, row=17)
# Button_Clear.grid(column=3, row=17)
#
# Label_1 = tk.Label(text="Cluster = ")
# Label_1.grid(column=0, row = 1)
#
# Label_2 = tk.Label(text="Well API = ")
# Label_2.grid(column=0, row = 2)
#
# Label_3 = tk.Label(text="Starting Point")
# Label_3.grid(column=0, row = 3)
#
# Label_4 = tk.Label(text="Xo = ")
# Label_4.grid(column=0, row = 4)
#
# Label_5 = tk.Label(text="Yo = ")
# Label_5.grid(column=0, row =5 )
#
# Label_6 = tk.Label(text="Zo = ")
# Label_6.grid(column=0, row = 6)
#
# Label_7 = tk.Label(text="Target Point ")
# Label_7.grid(column=0, row =7 )
#
# Label_8 = tk.Label(text="Xt = ")
# Label_8.grid(column=0, row = 8)
#
# Label_9 = tk.Label(text="Yt = ")
# Label_9.grid(column=0, row = 9)
#
# Label_10 = tk.Label(text="Zt = ")
# Label_10.grid(column=0, row =10 )
#
# Label_11 = tk.Label(text="KOP = ")
# Label_11.grid(column=0, row = 11)
#
# Label_12 = tk.Label(text="Tolerance = ")
# Label_12.grid(column=0, row =12 )
#
# Label_13 = tk.Label(text="Calculation")
# Label_13.grid(column=0, row = 13)
#
# Label_14 = tk.Label(text="Methond = ")
# Label_14.grid(column=0, row =14 )
#
# Label_15 = tk.Label(text="Data Point = ")
# Label_15.grid(column=0, row =15 )
#
# Label_16 = tk.Label(text="Number Section = ")
# Label_16.grid(column=0, row =16 )
#
# Entry_1=tk.Entry()
# Entry_1.grid(column = 1, row = 1)
#
# Entry_2=tk.Entry()
# Entry_2.grid(column = 1, row = 2)
#
# Entry_3=tk.Entry()
# Entry_3.grid(column = 1, row = 4)
#
# Entry_4=tk.Entry()
# Entry_4.grid(column = 1, row = 5)
#
# Entry_5=tk.Entry()
# Entry_5.grid(column = 1, row = 6)
#
# Entry_6=tk.Entry()
# Entry_6.grid(column = 1, row = 8)
#
# Entry_7=tk.Entry()
# Entry_7.grid(column = 1, row = 9)
#
# Entry_8=tk.Entry()
# Entry_8.grid(column = 1, row = 10)
#
# Entry_9=tk.Entry()
# Entry_9.grid(column = 1, row =11)
#
# Entry_10=tk.Entry()
# Entry_10.grid(column = 1, row = 12)
#
# Entry_11=tk.Entry()
# Entry_11.grid(column = 1, row = 14)
#
# Entry_12=tk.Entry()
# Entry_12.grid(column = 1, row = 15)
#
# Entry_13=tk.Entry()
# Entry_13.grid(column = 1, row = 16)
#
#
# variable1 = StringVar(window1)
# variable1.set("ft")
# listbox = OptionMenu(window1,variable1,"ft","m")
# listbox.grid(column = 2, row=11)
#
# variable2 = StringVar(window1)
# variable2.set("ft")
# listbox = OptionMenu(window1,variable2,"ft","m")
# listbox.grid(column = 2, row=12)
#
# variable3 = StringVar(window1)
# variable3.set("ft")
# listbox = OptionMenu(window1,variable3,"ft","m")
# listbox.grid(column = 2, row=11)
#
# window1.mainloop()
# menuframe = Frame(window1, width=640, height=100)
# Button_Traj = tk.Button(text="Trajectory")
# Button_Survey = tk.Button(text="Survey")
# Button_Check = tk.Button(text="Check Point")
# Button_Cluster = tk.Button(text="Cluster")
# menuframe.bind(Button_Traj)
# menuframe.bind(Button_Survey)
# menuframe.bind(Button_Check)
# menuframe.bind(Button_Cluster)
# menuframe.grid(column=0, row=0)

# Button_Traj.grid(column=0, row=0, width="10")
# Button_Survey.grid(column=1, row=0)
# Button_Check.grid(column=2, row=0)
# Button_Cluster.grid(column=3, row=0)

# frame = Frame(root, width=1800, height=250)
# frame.bind("<Button-1>",leftClick)
# frame.bind("<Button-2>",middleClick)
# frame.bind("<Button-3>",rightClick)
# frame.pack()


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