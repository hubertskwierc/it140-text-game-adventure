# Hugh Skwierc - KC Munchkin Adventure
# TextBasedGame.py - Project Two Final Submission

# Show the game instructions
def show_instructions():
    print("""
KC Munchkin Maze Adventure
Collect 6 items to win the game, but beware of Blinky!
Move commands: go North, go South, go East, go West
To pick up an item: get [item name]
Type 'exit' to leave the maze.
""")

# Show where the player is, what they have, and what they see
def show_status(current_room, inventory, rooms):
    print("\n--------------------------")
    print("You are in the", current_room)
    if 'item' in rooms[current_room]:
        print("You see a", rooms[current_room]['item'])
    print("Inventory:", inventory)
    directions = [d for d in rooms[current_room] if d != 'item']
    print("You can go:", ', '.join(directions))
    print("--------------------------")

# Show a message when the game ends
def end_game(message):
    print(message)
    print("Thanks for playing!")

# Move the player to a new room if direction is allowed
def get_new_state(direction, current_room, rooms):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("BUMP! Munchkin can’t go that way.")
        return current_room

# The main part of the game
def main():
    rooms = {
        'Start Chamber': {'North': 'Blue Zone'},
        'Blue Zone': {'South': 'Start Chamber', 'East': 'Power Pod', 'item': 'Cherry'},
        'Power Pod': {'West': 'Blue Zone', 'North': 'Warp Tunnel', 'item': 'Banana'},
        'Warp Tunnel': {'South': 'Power Pod', 'East': 'Dot Depot', 'item': 'Orange Pellet'},
        'Dot Depot': {'West': 'Warp Tunnel', 'North': 'Maze Junction', 'item': 'Super Pellet'},
        'Maze Junction': {'South': 'Dot Depot', 'East': 'Ghost Alley', 'item': 'Blue Pellet'},
        'Ghost Alley': {'West': 'Maze Junction', 'North': 'Ghost Lair', 'item': 'Energy Pellet'},
        'Ghost Lair': {'South': 'Ghost Alley', 'item': 'Blinky'}
    }

    current_room = 'Start Chamber'
    inventory = []
    needed_items = ['Cherry', 'Banana', 'Orange Pellet', 'Super Pellet', 'Blue Pellet', 'Energy Pellet']

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        move = input("Enter your move: ")

        if move.lower() == 'exit':
            end_game("Munchkin powers down.")
            break

        elif move.lower().startswith('go '):
            direction = move[3:].capitalize()
            current_room = get_new_state(direction, current_room, rooms)

        elif move.lower().startswith('get '):
            item = move[4:]
            if 'item' in rooms[current_room] and item == rooms[current_room]['item']:
                if item not in inventory:
                    inventory.append(item)
                    print(item, "collected!")
                    del rooms[current_room]['item']
                else:
                    print("You already have that.")
            else:
                print("There's nothing like that here.")

        else:
            print("That’s not a move I understand.")

        if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Blinky':
            end_game("NOM NOM…GAME OVER! Blinky got you.")
            break

        if sorted(inventory) == sorted(needed_items):
            end_game("Congratulations! You collected all the items and escaped Blinky!")
            break

# Start the game
if __name__ == "__main__":
    main()
