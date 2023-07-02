def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone "
        except IndexError:
            return "Invalid command"

    return inner


@input_error
def hello_command():
    return "How can I help you?"


@input_error
def add_command(command, contacts):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"{name} was added"


@input_error
def change_command(command, contacts):
    _, name, phone = command.split()
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for user {name} was changed"


@input_error
def phone_command(command, contacts):
    _, name = command.split()
    if name not in contacts:
        raise KeyError
    return f"Phone number for user {name} is {contacts[name]}"


@input_error
def show_all_command(contacts):
    if not contacts:
        return "No contacts found"
    else:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone} \n"
        return result


def main():
    contacts = {}

    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print(hello_command())
        elif command.startswith("add"):
            print(add_command(command, contacts))
        elif command.startswith("change"):
            print(change_command(command, contacts))
        elif command.startswith("phone"):
            print(phone_command(command, contacts))
        elif command == "show all":
            print(show_all_command(contacts))
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command")
    return


if __name__ == "__main__":
    main()
