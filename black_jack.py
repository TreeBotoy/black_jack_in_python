#imports
from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Black Jack Game")
root.geometry("1200x800")
root.configure(background="green")

def black_jack_shuffle(player):
    if player == "dealer":
        if len(dealer_score) == 2:
            if dealer_score[0] + dealer_score[1] == 21:
                black_jack_status["dealer"] = "yes"

                messagebox.showinfo("Black Jack!", "Dealer has Black Jack! Dealer wins!") 
                hit_button.config(state = "disabled")
                stand_button.config(state = "disabled")

    if player == "player":
        if len(player_score) == 2:
            if player_score[0] + player_score[1] == 21:
                black_jack_status["player"] = "yes"

                messagebox.showinfo("Black Jack!", "Player has Black Jack! Player wins!") 
                hit_button.config(state = "disabled")
                stand_button.config(state = "disabled")

    if len(dealer_score) == 2 and len(player_score) == 2:
        if black_jack_status["dealer"] == "yes" and black_jack_status["player"] == "yes":
            messagebox.showinfo("Black Jack!", "Both dealer and player have Black Jack! It's a tie!")
            hit_button.config(state = "disabled")
            stand_button.config(state = "disabled")
        elif black_jack_status["dealer"] == "yes":
            messagebox.showinfo("Black Jack!", "Dealer has Black Jack! Dealer wins!") 
            hit_button.config(state = "disabled")
            stand_button.config(state = "disabled")
        elif black_jack_status["player"] == "yes":
            messagebox.showinfo("Black Jack!", "Player has Black Jack! Player wins!") 
            hit_button.config(state = "disabled")
            stand_button.config(state = "disabled")

#card images
def resize_cards(card):
    our_card = Image.open(card)
    our_card_resized = our_card.resize((150, 218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resized)
    return our_card_image

#card shuffling
def shuffle():
    global black_jack_status
    black_jack_status = {"dealer": "no", "player": "no"}

    hit_button.config(state = "normal")
    stand_button.config(state = "normal")
    #card deck
    dealer_label_1.config(image = "")
    dealer_label_2.config(image = "")
    dealer_label_3.config(image = "")
    dealer_label_4.config(image = "")
    dealer_label_5.config(image = "")

    player_label_1.config(image = "")
    player_label_2.config(image = "")
    player_label_3.config(image = "")
    player_label_4.config(image = "")
    player_label_5.config(image = "")

    #card faces
    card_suits = ["hearts", "diamonds", "spades", "clubs"]
    card_values = range(2, 15)

    global deck
    deck = []
    for suit in card_suits:
        for value in card_values:
            deck.append(f"{value}_of_{suit}")
    
    global player, dealer, dealer_spot, player_spot, dealer_score, player_score
    dealer = []
    player = []
    dealer_score = []
    player_score = []
    dealer_spot = 0
    player_spot = 0

    dealer_hit()
    dealer_hit()    
    player_hit()
    player_hit()

    root.title(f"Black Jack Game - Deck Shuffled! {len(deck)} cards left")

def dealer_hit():
    global dealer_spot
    if dealer_spot < 5:
        try:
            dealer_card = random.choice(deck)
            deck.remove(dealer_card)
            dealer.append(dealer_card)
            deal_card = int(dealer_card.split("_", 1)[0])
            if deal_card == 14:
                dealer_score.append(11)
            elif deal_card == 11 or deal_card == 12 or deal_card == 13:
                dealer_score.append(10)
            else:
                dealer_score.append(deal_card)

            global dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5
        
            if dealer_spot == 0:
                dealer_image_1 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{dealer_card}.png')
                dealer_label_1.config(image=dealer_image_1)
                dealer_spot += 1
            elif dealer_spot == 1:
                dealer_image_2 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{dealer_card}.png')
                dealer_label_2.config(image=dealer_image_2)
                dealer_spot += 1
            elif dealer_spot == 2:
                dealer_image_3 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{dealer_card}.png')
                dealer_label_3.config(image=dealer_image_3)
                dealer_spot += 1
            elif dealer_spot == 3:
                dealer_image_4 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{dealer_card}.png')
                dealer_label_4.config(image=dealer_image_4)
                dealer_spot += 1
            elif dealer_spot == 4:
                dealer_image_5 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{dealer_card}.png')
                dealer_label_5.config(image=dealer_image_5)
                dealer_spot += 1
    
            root.title(f"Black Jack Game - Hit! {len(deck)} cards left")

        except:
            root.title(f"Black Jack Game - card deck empty!")

        black_jack_shuffle("dealer")

def player_hit():
    global player_spot
    if player_spot < 5:
        try:
            player_card = random.choice(deck)
            deck.remove(player_card)
            player.append(player_card)
            play_card = int(player_card.split("_", 1)[0])
            if play_card == 14:
                player_score.append(11)
            elif play_card == 11 or play_card == 12 or play_card == 13:
                player_score.append(10)
            else:
                player_score.append(play_card)

            global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
        
            if player_spot == 0:
                player_image_1 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{player_card}.png')
                player_label_1.config(image=player_image_1)
                player_spot += 1
            elif player_spot == 1:
                player_image_2 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{player_card}.png')
                player_label_2.config(image=player_image_2)
                player_spot += 1
            elif player_spot == 2:
                player_image_3 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{player_card}.png')
                player_label_3.config(image=player_image_3)
                player_spot += 1
            elif player_spot == 3:
                player_image_4 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{player_card}.png')
                player_label_4.config(image=player_image_4)
                player_spot += 1
            elif player_spot == 4:
                player_image_5 = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{player_card}.png')
                player_label_5.config(image=player_image_5)
                player_spot += 1
    
            root.title(f"Black Jack Game - Hit! {len(deck)} cards left")

        except:
            root.title(f"Black Jack Game - card deck empty!")

        black_jack_shuffle("player")

def hit():
    try:
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        global dealer_image
        dealer_image = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{card}.png')
        dealer_label.config(image = dealer_image)

        card = random.choice(deck)
        deck.remove(card)
        player.append(card)
        global player_image
        player_image = resize_cards(f'D:/codes/visual/black_jack_game/Playing Cards/PNG-cards-1.3/{card}.png')
        player_label.config(image = player_image)
        

        root.title(f"Black Jack Game - Hit! {len(deck)} cards left")

    except:
        root.title(f"Black Jack Game - card deck empty!")

my_frame = Frame(root, bg="green")
my_frame.pack(pady = 20)

dealer_frame = LabelFrame(my_frame, text = "Dealer", bd = 0)
dealer_frame.pack(padx = 20, ipadx = 20)

player_frame = LabelFrame(my_frame, text = "Player", bd = 0)
player_frame.pack(ipadx = 20, pady = 10)

dealer_frame = Label(dealer_frame, text = "")
dealer_frame.pack(pady = 20)

player_frame = Label(player_frame, text = "")
player_frame.pack(pady = 20)

#dealer cards in frames
dealer_label_1 = Label(dealer_frame, text = "")
dealer_label_1.grid(row = 0, column = 0, pady = 20, padx = 20)

dealer_label_2 = Label(dealer_frame, text = "")
dealer_label_2.grid(row = 0, column = 1, pady = 20, padx = 20)

dealer_label_3 = Label(dealer_frame, text = "")
dealer_label_3.grid(row = 0, column = 2, pady = 20, padx = 20)

dealer_label_4 = Label(dealer_frame, text = "")
dealer_label_4.grid(row = 0, column = 3, pady = 20, padx = 20)

dealer_label_5 = Label(dealer_frame, text = "")
dealer_label_5.grid(row = 0, column = 4, pady = 20, padx = 20)

#player cards in frames
player_label_1 = Label(player_frame, text="")
player_label_1.grid(row = 1, column = 0, pady = 20, padx = 20)

player_label_2 = Label(player_frame, text = "")
player_label_2.grid(row = 1, column = 1, pady = 20, padx = 20)

player_label_3 = Label(player_frame, text = "")
player_label_3.grid(row = 1, column = 2, pady = 20, padx = 20)

player_label_4 = Label(player_frame, text = "")
player_label_4.grid(row = 1, column = 3, pady = 20, padx = 20)

player_label_5 = Label(player_frame, text="")
player_label_5.grid(row = 1, column = 4, pady = 20, padx = 20)

#Buttons
button_frame = Frame(root, bg="green")
button_frame.pack(pady = 20)

shuffle_button = Button(button_frame, text="Shuffle Deck", font = ("Helvetica", 14), bg = "white", fg = "black", command = shuffle)
shuffle_button.grid(row = 0, column = 0)

hit_button = Button(button_frame, text="Hit", font = ("Helvetica", 14), bg="white", fg = "black", command = player_hit)
hit_button.grid(row = 0, column = 1, padx = 10)

stand_button = Button(button_frame, text = "Stand", font = ("Helvetica", 14), bg = "white", fg = "black")
stand_button.grid(row = 0, column = 2)

shuffle()
 
root.mainloop()