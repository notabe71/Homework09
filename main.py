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
def hello_command(command, contacts):
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
def show_all_command(command, contacts):
    if not contacts:
        return "No contacts found"
    else:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone} \n"
        return result


@input_error
def bye_command(command, contacts):
    return "Good bye!"


OPERATIONS = {
    "hello": hello_command,
    "add": add_command,
    "change": change_command,
    "phone": phone_command,
    "show_all": show_all_command,
    "close": bye_command,
    "good bye": bye_command,
    "exit": bye_command

}


def get_handler(operation):
    return OPERATIONS[operation]


def main():
    contacts = {}

    while True:
        command = input("Enter a command: ").lower()

        comm_arr = command.split()
        if command and comm_arr[0] in OPERATIONS.keys():
            handler = get_handler(comm_arr[0])

            res = handler(command, contacts)
            print(res)
            if res == "Good bye!":
                break
        else:
            print("Invalid command")

    return


if __name__ == "__main__":
    main()
