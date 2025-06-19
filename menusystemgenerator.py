menu_data = {
    "File": ["New", "Open", "Save", "Exit"],
    "Edit": ["Undo", "Redo", "Copy", "Paste"],
    "Help": ["Documentation", "About"]
}
action = {
    ("File",1): 'new_file',
    ("File",2): 'open_file',
    ("File",3): 'save_file',
    ("File",4): 'exit_file',
    ("Edit",1): 'undo_edit',
    ("Edit",2): 'redo_edit',
    ("Edit",3): 'copy_edit',
    ("Edit",4): 'paste_edit',
    ("Help",1): 'Documentation_Help',
    ("Help",2): 'About_Help',

}


def display_menu(menu_dict):
    print("=== Main Menu ===")
    for item in menu_dict:
        print(item)
        for index , subitem in enumerate(menu_dict[item],start=1):
            print(f"  {index}. {subitem}")
    while True:
        user = input("Enter selection (e.g. \"File 2\"): ").strip().capitalize()
        parts = user.split()
        if len(parts) == 2 and parts[0] in menu_data:
            break
    category = parts[0]
    print("You selected:",category)
    return category, int(parts[1])



while True:
    temp = display_menu(menu_data)
    func = action.get(temp)
    if func:
        pass
    else:
        print("Wrong input")