from tkinter import *

# Initializing GUI
root = Tk()

# Basic properties of GUI
root.title("Card Deck")
root.iconphoto(False, PhotoImage(file = "blackjack_logo.png"))
root.geometry("900x500")
root.configure(background = "green")

# Creates Main Frame
main_frame = Frame(root, bg = "green")
main_frame.pack(pady = 20)

# Creates Frames For Cards
dealer_frame = LabelFrame(main_frame, text = "Dealer", bd = 0, bg = "white", fg = "black")
dealer_frame.grid(row = 0, column = 0, padx = 20, ipadx = 20)

player_frame = LabelFrame(main_frame, text = "Player", bd = 0, bg = "white", fg = "black")
player_frame.grid(row = 0, column = 1, ipadx = 20)

# Put Cards In Frames
dealer_label = Label(dealer_frame, text = "", bg = "white")
dealer_label.pack(pady = 20)

player_label = Label(player_frame, text = "", bg = "white")
player_label.pack(pady = 20)

# Create a couple buttons
shuffle_button = Button(root, text = "Shuffle Deck", font = ("Times New Roman", 14, "bold"), bd = 0, relief = "flat", bg = "green")
shuffle_button.pack(pady = 20)

card_button = Button(root, text = "Get Cards", font = ("Times New Roman", 14, "bold"), bd = 0, relief = "flat", bg = "green")
card_button.pack(pady = 20)



root.mainloop()