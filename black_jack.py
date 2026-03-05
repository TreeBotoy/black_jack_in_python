#imports
from tkinter import *
import random

root = Tk()
root.title("Black Jack Game")
root.geometry("900x500")
root.configure(background="green")

#card shuffling
def shuffle():
    card_suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_values = range(2, 15)

    global deck
    deck = []
    for suit in card_suits:
        for value in card_values:
            deck.append(f"{value} of {suit}")
    
    global player, dealer
    dealer = []
    player = []

    card=random.choice(deck)
    deck.remove(card)
    dealer.append(card)
    dealer_label.config(text=card)

    card=random.choice(deck)
    deck.remove(card)
    player.append(card)
    player_label.config(text=card)

    root.title(f"Black Jack Game - Deck Shuffled! {len(deck)} cards left")

def hit():
    try:
        card=random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        dealer_label.config(text=card)

        card=random.choice(deck)
        deck.remove(card)
        player.append(card)
        player_label.config(text=card)

        root.title(f"Black Jack Game - Hit! {len(deck)} cards left")

    except:
        root.title(f"Black Jack Game - card deck empty!")

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

dealer_label = Label(dealer_frame, text="")
dealer_label.pack(pady=20)

player_label = Label(player_frame, text="")
player_label.pack(pady=20)

#Buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), bg="white", fg="black", command=shuffle)
shuffle_button.pack(pady=20)

hit_button = Button(root, text="Hit", font=("Helvetica", 14), bg="white", fg="black", command=hit)
hit_button.pack(pady=20)

shuffle()

#cards



root.mainloop()