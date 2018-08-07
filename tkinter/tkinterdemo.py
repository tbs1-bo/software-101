import tkinter

class GUI:
    def __init__(self):
        self.counter = 0

        root = tkinter.Tk()
        root.title("TKinter Demo")

        # add menu
        menubar = tkinter.Menu(root)
        root.config(menu=menubar)
        # adding Tools-menu to menubar
        tools_menu = tkinter.Menu(menubar)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Next", command=self.click)

        # add image in a label
        bild = tkinter.PhotoImage(file="ball.gif")  # only GIF or PGM/PPM
        lbl = tkinter.Label(root, image=bild)
        lbl.grid(row=0, column=0)

        # add button, invoking method 'click' when clicked.
        btn = tkinter.Button(root, text="next", command=self.click)
        btn.grid(row=1, column=0)

        # add label with counter value
        self.lbl = tkinter.Label(root, text="Label für Counter")
        self.lbl.grid(row=1, column=1)

        # add entry field
        self.ent = tkinter.Entry(root)
        self.ent.grid(row=1, column=2)

        # entering main event loop
        root.mainloop()

    def click(self):
        # update label
        self.lbl.configure(text="Counter " + str(self.counter))

        # clear the entry field and inter counter value at beginning
        self.ent.delete(0, tkinter.END)        
        self.ent.insert(0, self.counter)

        self.counter += 1

if __name__ == "__main__":
    GUI()
