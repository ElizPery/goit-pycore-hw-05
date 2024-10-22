# Decorator for handling errors of input
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Contact is not in contacts"
    return inner

# Function take user input (first command) and return parsed data 
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Decorator to handle ValueError
@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    # Function add contact with data in args (name, phone) to the dict contacts if name is already in contacts return  'This name is already in contacts'

    name, phone = args

    if name in contacts:
        return 'This name is already in contacts'
    
    contacts[name] = phone
    return 'Contact is added!'

# Decorator to handle ValueError
@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    # Function takes data about contact and update phone of contact by name

    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return 'Contact is updated!'
    
    return 'Contact is not in contacts'

# Decorator to handle IndexError and KeyError
@input_error
def show_phone(args: str, contacts: dict) -> str:
    # Function takes name of contact and return its phone

    name = args[0]

    phone = contacts[name]
    return phone
    
# Function takes dict of contacts and return it, if no contacts return 'No contacts found'
def show_all(contacts: dict) -> str:
    all_contacts = []

    if len(contacts) == 0:
        return 'No contacts found'
    for name, phone in contacts.items():
        all_contacts.append(f'Contact: {name} {phone}\n')
    
    return ''.join(all_contacts).strip()


def main():
    contacts = {}

    print('Welcome to the assistance bot!')

    while True:
        user_input = input('Enter a command >>> ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Goodbye!')
            break
        elif command == 'hello':
            print('Hello, how can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command')

if __name__ == '__main__':
    main()