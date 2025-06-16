import random

riddles = [
    {'r':"Whats 2 + 2? ",'ans':'4'},
    {'r':"Whats 5 + 2? ",'ans':'7'},
    {'r':"Whats 0 + 0? ",'ans':'0'}
]
riddle = random.choice(riddles)


game_map = {
    "entrance": {
        "desc": "You stand at the entrance of a dimly lit cavern. The air is damp and cool.",
        "north": "hallway", 
        "items": ["torch"]
    },
    "hallway": {
        "desc": "A narrow stone corridor stretches before you, with shadows dancing on the walls.",
        "south": "entrance",
        "east": "trap_room",
        "west": "treasure_room",
        "items": []
    },
    "treasure_room": {
        "desc": "Piles of ancient coins and gems glitter in each corner.",
        "east": "hallway",
        'west': "riddle_chamber",
        "items": ["gold coin", "ruby"]
    },
    "trap_room": {
        "desc": "You feel the floor give slightly beneath your feet—something here seems dangerous.",
        "west": "hallway",
        "items": []
    },
    "riddle_chamber": {
    "desc": "An echoing voice asks you a question before you can pass.",
    "items": []
     # no direction keys here yet...
    }
}
 
current_location = 'entrance'
player_inventory = []

def look(location: str ) -> None:
    '''
        print the desc,item and exits of current location.
    '''
    print('\nDiscription: ',game_map[location]['desc'])
    print("Items: ",game_map[location]['items'])
    exits = [d for d in ("north","south","east","west") if d in game_map[location]]
    print("Exits:", ", ".join(exits))
    if not exits:
        ask_riddle()

def move(direction:str) -> None:
    '''Attempt to move in the given direction; update current location or notify failure.'''
    global current_location
    if direction in game_map[current_location]:
        current_location = game_map[current_location][direction]
        print(f'\nLocation chnaged to {current_location}.')
    else:
        print("\nYou can't go that way.")
    pass

def take(item:str) -> None:
    '''
        Adds item from current location to inventory if they exist.
    '''
    if item in game_map[current_location]['items']:
        player_inventory.append(item)
        game_map[current_location]['items'].remove(item)
        print(f'\n{item} acquired.')
    else:
        print("\nThat's not here.")
    
def inventory() -> None:
    '''print the items in inventory'''
    if player_inventory:
        for index , item in enumerate(player_inventory,start=1):
            print(f"{index}. {item}")
    else:
        print("No items in the inventory.")

def ask_riddle():
    global riddle
    print(riddle['r'])
    ans = input("Enter answer: ").strip()
    if ans == riddle['ans']:
        game_map["riddle_chamber"].update({"south": "entrance"})
        print("You may now exit south")
    else:
        ask_riddle()

while True:
    action = input("\nCommands: move north, take torch, look, inventory, quit\n> ").strip().lower()
    parts = action.split(" ",1)
    cmd = parts[0].strip()
    if cmd == 'move':
        if len(parts) > 1:
            arg = parts[1].strip()
            move(parts[1])
        else:
            print("Wrong input")
    elif cmd == 'take':
        if len(parts) > 1:
            arg = parts[1].strip()
            take(parts[1])
        else:
            print("Wrong input")
    elif action == 'look':
        look(current_location)
    elif action == 'inventory':
        inventory()
    elif action == 'quit':
        break
    else:
        print("Wrong Input.")