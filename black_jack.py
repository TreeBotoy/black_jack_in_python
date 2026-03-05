#imports
from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Black Jack Game")
root.geometry("1200x800")
root.configure(background="green")

#card images
def resize_cards(card):
    our_card = Image.open(card)
    our_card_resized = our_card.resize((150, 218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resized)
    return our_card_image

#card shuffling
def shuffle():
    card_suits = ["hearts", "diamonds", "spades", "clubs"]
    card_values = range(2, 15)

    global deck
    deck = []
    for suit in card_suits:
        for value in card_values:
            deck.append(f"{value}_of_{suit}")
    
    global player, dealer
    dealer = []
    player = []

    card=random.choice(deck)
    deck.remove(card)
    dealer.append(card)

    global dealer_image
    dealer_image = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{card}.png')
    dealer_label.config(image=dealer_image)

    card=random.choice(deck)
    deck.remove(card)
    player.append(card)

    global player_image
    player_image = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{card}.png')
    player_label.config(image=player_image)

    player_label.config(text=card)

    root.title(f"Black Jack Game - Deck Shuffled! {len(deck)} cards left")

def hit():
    try:
        card=random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        global dealer_image
        dealer_image = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{card}.png')
        dealer_label.config(image=dealer_image)

        card=random.choice(deck)
        deck.remove(card)
        player.append(card)
        global player_image
        player_image = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{card}.png')
        player_label.config(image=player_image)
        

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
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), bg="white", fg="black", command=shuffle)
shuffle_button.grid(row=0, column=0)

hit_button = Button(button_frame, text="Hit", font=("Helvetica", 14), bg="white", fg="black", command=hit)
hit_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand", font=("Helvetica", 14), bg="white", fg="black")
stand_button.grid(row=0, column=2)

shuffle()
 
root.mainloop()