

from .commands import find_closest_command,get_command_input
from .save_load_book import save_address_book,load_address_book
from .memory import * #AddressBook,SetterValueIncorrect,Name,Phone,Birthday,Address,Email
from .notes_core import Notebook
from .common_functions import STR_EPIC_ASSISTANT,YELLOW

def start_work():
    # Load the address book from storage, or create a new one if it doesn't exist
    address_book = load_address_book()
    if not address_book:
        address_book = AddressBook()
    # Load the notes book from storage, or create a new one if it doesn't existя
    notes_book = Notebook()
    print(STR_EPIC_ASSISTANT)
    address_book.get_birthdays_per_week()
    return (address_book,notes_book)

def command_exe(command = dict,adress_book = AddressBook,note_book = Notebook):
    cmd_func = command.get('func')
    if len(command.get('arguments')) > 0:
            # Prompt the user to enter arguments for the command
            args = []
            mes = f'For this command we need {str(command.get("arguments"))}'
            if command.get('name') == 'add new contact':
                mes += 'If you want to skip unimportant argument (email,address or birthday) write pass.'
            elif command.get('name') == 'change exist contact':
                mes +=  'For second argument "changed field" write: "phone","email","birthday" or "address"'

            print(mes)
            got_args = False
            i = 0
            while not got_args:
                f_arg = command.get("arguments")[i]
                match f_arg:
                    case 'name':
                        f_class = Name
                    case 'phone':
                        f_class = Phone
                    case 'birthday':
                        f_class = Birthday
                    case 'email':
                        f_class = Email
                    case 'address':
                        f_class = Address
                    case _:
                        f_class = None
                args.append(get_command_input(f'Enter {f_arg}: ',check_class = f_class,need_comp=False))  
                if len(args) == len(command.get("arguments")):
                    got_args = True    
                else:
                    i += 1   
            try:   
                return cmd_func(*args,a_book = adress_book,n_book = note_book)
            except SetterValueIncorrect as e:
                print(e.message + '\n Please try again this command or another one.')
                return None
    else:
        return cmd_func(a_book = adress_book,n_book = note_book)

def main(): 
    work_books = start_work()
    a_book = work_books[0]
    n_book = work_books[1]
    while True:
        # Get user input for a command
        input_string = get_command_input("Enter a command: ")
        #parse input function that get back command or None
        command = find_closest_command(input_string)
        if command:
            result = command_exe(command,a_book,n_book)
            if isinstance(result,list):
                # Print each item in the result listc
                for i in result:
                    print(i)
            else:
                print(result) if result else None
            #End of app
            if command["name"] == 'ending':
                break
        else:
            print("Sorry, i don't understand this your command. Please try again.")
    # Save the address book to storage
    save_address_book(a_book)
    # here will be save notebook in storage


if __name__ == '__main__':
    main()
