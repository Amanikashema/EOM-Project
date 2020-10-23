from tkinter import *
root = Tk()
root.title("Ticket sales")
root.geometry("600x600")

class Easyticket:
    def __init__(self,root):
        self.label_1 = Label(root,text="Enter CellNumber:")
        self.label_1.pack()
        self.label_1.place(x=50,y=50)
        self.entry=Entry(self.label_1, textvariable="")
        self.label_2 = Label(root,text="Select Ticket Category:")
        self.label_2.pack()
        self.label_2.place(x=50,y=80)
        self.label_3= Label(root,text="Number of Tickets Bought")
        self.label_3.pack()
        self.label_3.place(x=50,y=110)








Easyticket(root)

root.mainloop()

