
import pickle
import sys
import os
import time

def list_address(addresses):
    for person in addresses:
        print(person)

def add_person(addresses):
    first_name = input("Enter the first name: ")
    last_name = input("Eter the last name: ")
    email = input("Enter the email address: ")
    
    address = {'first name':first_name, 'last name':last_name, 'email':email}
    addresses.append(address)
    
    currentfile = 'pickle-' + time.strftime("%Y%m%d-%H%M%S") + '.p'
    pickle.dump(addresses, open('./pickles/' + currentfile, 'ab'))
    
def restore():
    print("What file do you want to use a restore point? ")
    for file1 in os.listdir('./pickles'):
        print(file1)
    picklefile = input("Type the filename: ")
    with open('./pickles/' + picklefile, 'rb') as f:
        restorepoint = pickle.load(f)
    addresses = restorepoint
    return addresses
    
def command():
    command = input('Please enter a command for address book- \n\tq: Quit, l: List all people, a: Add a new person, r: Restore to a specific time-stamp: ') 
    command = str(command)
    command = command.lower().strip()
    return command

def menu(): 
    addresses = []
    while True:
        this = command()
        if this == 'q':
            sys.exit("Goodbye!")    
        elif this  == 'l':
            list_address(addresses)
        elif this == 'a':
            add_person(addresses)
        elif this == 'r':
            addresses = restore()
        else:
            print("Not a valid command.\n")

menu()
