def manage_contacts():
    contacts = {}
    while True:
        choice = input("Enter action: a = add contact, v - view contacts, q - quit: ");
        choice = choice.lower()
        if choice not in ['a', 'v', 'q']:
            print("Invalid choice. Please try again.")
            continue