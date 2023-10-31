import random
import json

card_data = []

# Initialize cards
def initCards():
    global card_data
    try:
        with open("carddb.json", "r") as file:
            card_data = json.load(file)
    except FileNotFoundError:
        card_data = []  # Initialize an empty list if the file is not found

# Call initCards() to load the card data from carddb.json
initCards()

# Define the getCard function
def getCard(id):
    for card in card_data:
        if card["id"] == id:
            return card
        
# Generate a random card
def generateRandomCard():
    return random.choice(card_data)

# Number of cards
def countCards():
    return len(card_data)

# Test Card Model
if __name__ == "__main__":
    # Most liked and most jeered cards are not applicable for cards, so you can remove those parts

    # Random card
    print("Random card:")
    random_card = generateRandomCard()
    print(random_card)

    # Count of Cards
    print("Cards Count: " + str(countCards()))
