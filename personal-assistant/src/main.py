from commands import find_closest_command, get_command_input,get_command_input_agree
from save_load_books import *
from open_ai_input_assistent import *
from memory import *
from notes_core import Notebook,Tag
from common_functions import STR_EPIC_ASSISTANT
from colorama import init
from goose_game import *
import keyboard
import os
from abc import ABC, abstractmethod
import multiprocessing

Use_Open_Ai = False
work_books = None


class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_command_menu(self):
        pass

    @abstractmethod
    def get_user_input(self, prompt):
        pass

    @abstractmethod
    def show_message(self, message):
        pass

class ConsoleUserInterface(UserInterface):
    def display_contacts(self, contacts):
        # Вивести контакти у консоль
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def display_notes(self, notes):
        # Вивести нотатки у консоль
        for note in notes:
            print(f"Title: {note.title}, Tag: {note.tag}, Description: {note.description}")

    def display_command_menu(self):
        # Вивести доступні команди у консоль
        print("Available commands:")
        # Додайте тут код для виведення списку команд

    def get_user_input(self, prompt):
        # Отримати введення користувача з консолі
        return input(prompt)

    def show_message(self, message):
        # Вивести повідомлення користувачу
        print(message)


def use_open_ai():
    activated = activate_openai()
    global Use_Open_Ai
    if not activated:
        print( Fore.MAGENTA + 'Do you want to use OpenAi in your work? You will need to enter an OpenAI API key. This is used by the extension to access the API and is only sent to OpenAI.' + Style.RESET_ALL)
        agree = get_command_input_agree("Yes or No: ")
        if agree.lower() == 'yes':
            print(STR_OPENAI_HELP)
            key = get_command_input('Enter an OpenAI API key: ')
            activated = activate_openai(key)         
            Use_Open_Ai = True
            return activated
        if agree.lower() == 'no':
            print(Fore.MAGENTA + 'No problem, Sir. You will use base commands of Jarvis.' + Style.RESET_ALL)
            return False
    else:
        Use_Open_Ai = True
        return activated

def start_work():
    # Initialize colorama
    init()

    # Load the address book from storage, or create a new one if it doesn't exist
    address_book = None
    try:
        address_book = load_addressbook()
    except:
        print("Unfortunately, load address book failed")
    if not address_book:
        address_book = AddressBook()
    # Load the notes book from storage, or create a new one if it doesn't existя
    notes_book = None
    try:
        notes_book = load_notebook()
    except:
        print("Unfortunately, load  notebook failed")
    if not notes_book:
        notes_book = Notebook()
    print(STR_EPIC_ASSISTANT)
    address_book.get_birthdays_per_week()
    if use_open_ai():
        print(Fore.MAGENTA + 'If you will write something except commands, on this will answer ChatGPT.' + Style.RESET_ALL)
    return (address_book, notes_book)

def end_work():
    try:
        global work_books
        save_addressbook(work_books[0])
        save_notebook(work_books[1])
        global Use_Open_Ai
        if Use_Open_Ai:
            save_openai()
    except:
        print("Unfortunately, save failed :(")
    finally:
        os._exit(0) 

def command_exe(command=dict, adress_book=AddressBook, note_book=Notebook):
    cmd_func = command.get('func')
    if len(command.get('arguments')) > 0:
        # Prompt the user to enter arguments for the command
        args = []
        mes = f'For this command we need {str(command.get("arguments"))}'
        if command.get('name') == 'add new contact':
            mes += 'If you want to skip unimportant argument (email,address or birthday) write pass.'
        elif command.get('name') == 'change exist contact':
            mes += 'For second argument "changed field" write: "phone","email","birthday" or "address"'
        elif command.get('name') == 'edit note info':
            mes += 'For second argument "changed field" write: "title","tag" or "description"'
        print(mes)
        got_args = False
        i = 0
        while not got_args:
            f_arg = command.get("arguments")[i]
            if f_arg == 'name':
                f_class = Name
            elif f_arg == 'phone':
                f_class = Phone
            elif f_arg == 'birthday':
                f_class = Birthday
            elif f_arg == 'email':
                f_class = Email
            elif f_arg == 'address':
                f_class = Address
            elif f_arg == 'tag':
                f_class = Tag
            else:
                f_class = None
            args.append(get_command_input(
                f'Enter {f_arg}: ', check_class=f_class, need_comp=False,check_add_command=command, arg_number = i))
            if len(args) == len(command.get("arguments")):
                got_args = True
            else:
                i += 1
        try:
            return cmd_func(*args, a_book=adress_book, n_book=note_book)
        except SetterValueIncorrect as e:
            print(e.message + '\n Please try again this command or another one.')
            return None
    else:
        return cmd_func(a_book=adress_book, n_book=note_book)


def main():
    global work_books
    work_books = start_work()
    a_book = work_books[0]
    n_book = work_books[1]

    # keyboard.add_hotkey('esc', lambda: end_work())

    user_interface = ConsoleUserInterface()

    global Use_Open_Ai
    while True:

        # Вивести меню команд користувачу
        user_interface.display_command_menu
        
        # Отримати команду користувача через інтерфейс
        input_string = user_interface.get_user_input("Enter a command: ")

        # # Get user input for a command
        # input_string = get_command_input("Enter a command: ")
        # parse input function that get back command or None
        command = find_closest_command(input_string)
        
        
        if command:
            result = command_exe(command, a_book, n_book)
            if isinstance(result, list):
                # Print each item in the result listc
                for i in result:
                    user_interface.show_message(i)
                    # print(i)
            else:
                user_interface.show_message(result) if result else None
                # print(result) if result else None
                if result == "Starting the game...":
                    play()
                    end_work()

            # End of app
            if command["name"] == 'ending':
                break
        elif Use_Open_Ai:
            user_interface.show_message(input_answer_from_ai(input_string))
            # print(Fore.MAGENTA + input_answer_from_ai(input_string) + Style.RESET_ALL)
        else:
            user_interface.show_message("Sorry, I don't understand this command. Please try again.")

            # print("Sorry, i don't understand this your command. Please try again.")

    end_work()

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def test_factorize():
    a, b, c, d = factorize(128), factorize(255), factorize(99999), factorize(10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


def parallel_factorize(number, pool_size=None):
    if pool_size is None:
        pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(pool_size)
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    test_factorize()
    print("All tests passed for synchronous version.")

    pool_size = multiprocessing.cpu_count()
    a, b, c, d = parallel_factorize(128, pool_size), parallel_factorize(255, pool_size), parallel_factorize(99999, pool_size), parallel_factorize(10651060, pool_size)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    print("All tests passed for parallel version.")
    
    main()
