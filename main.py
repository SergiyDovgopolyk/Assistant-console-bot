def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Type 'help' for a list of commands."

    return wrapper

contacts = {}

@input_error
def add_contact(input_str):
    _, name, phone = input_str.split()
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

@input_error
def change_contact(input_str):
    _, name, phone = input_str.split()
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
            return f"Contact {name} not found"

@input_error
def get_phone(input_str):
    _, name = input_str.split()
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}"
    else:
            return f"Contact {name} not found"

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
            result = "Contacts:\n"
            for name, phone in contacts.items():
                result += f"{name}: {phone}\n"
            return result

def main():
        while True:
            command = input("Enter a command: ").strip().lower()

            if command in ['hello', 'hi']:
                print("How can I help you?")
            elif command.startswith("add "):
                result = add_contact(command)
                print(result)
            elif command.startswith("change "):
                result = change_contact(command)
                print(result)
            elif command.startswith("phone "):
                result = get_phone(command)
                print(result)
            elif command == "show all":
                result = show_all_contacts()
                print(result)
            elif command in ["good bye", "close", "exit"]:
                print("Good bye!")
                break
            else:
                print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()



