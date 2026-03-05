#imports
from tkinter import *

root = Tk()
root.title("Black Jack Game")
root.geometry("900x500")
root.configure(background="green")

my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_frame = Label(dealer_frame, text="")
dealer_frame.pack(pady=20)

player_frame = Label(player_frame, text="")
player_frame.pack(pady=20)

#Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), bg="white", fg="black")
shuffle_button.pack(pady=20)

hit_button = Button(root, text="Hit", font=("Helvetica", 14), bg="white", fg="black")
hit_button.pack(pady=20)

#cards



#stand

#hit

#card shuffling

root.mainloop()