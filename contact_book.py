# This is a simple contact book program that allows users to add contacts and view them.
def manage_contacts():
    contacts = {}
    while True:
        choice = input("Enter action: a = add contact, v - view contacts, q - quit: ");
        choice = choice.lower()
        if choice not in ['a', 'v', 'q']:
            print("Invalid choice. Please try again.")
            continue
        if choice == 'q':
            break
        if choice == 'a':
            name = input("Enter contact name: ")
            number = input("Enter contact phone number: ")
            contacts[name] = number
            print("Contact added.")
        if choice == 'v':
            if len(contacts) == 0:
                print("No contacts to display.")
            else:
                print("Contacts:")
                for name, number in contacts.items():
                    print(name, number)

manage_contacts()
