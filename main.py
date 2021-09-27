import datetime
from datetime import date
import re


def new_entry(entry):

    pattern = re.compile(r"[a-zA-Z]+, ?(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[12]?)-\d{4}")
    if re.match(pattern,entry):
        entry_parts = entry.split(',')
        new_key = entry_parts[0].lower().capitalize()  # It's the person's name that will be a key in the dictionary after giving it a proper formatting
        new_value = entry_parts[1]

        # Getting the current year out of the given birthday of the current person.
        birthday_year = new_value.split('-')[2]  # The year of the current given birthday

        # Getting the name of the day out of the given birthday of the current person
        birthday = new_value.split('-')  # Converting the current birthday to a list that has 3 elements
        birthday = datetime.date(int(birthday[2]), int(birthday[1]), int(birthday[0]))  # Converting the current birthday from a string type to a datetime type in a proper order(Y,M,D)/type(integer) arguments that datetime.date work with.
        day_name = birthday.strftime('%A')  # Retrieving the full day name as a string
        all_persons[new_key] = [int(today) - int(birthday_year), day_name]  # Add a new key/value pair to the dictionary where the kay is the person's name, and the value is a list of 2 element, one is the person's age, and the second one is the day name

    else:
        print(f'Invalid Entry {entry}')


def unpacking(name, info):
    print(f'{name} is {info[0]} years old, and she/he was born on {info[1]}')
    all_persons[name] = info[0]


running = True
all_persons = {}  # Initial value of a global dictionary that saves all entries.
current_person = {}  # Initial value of a global dictionary that save only one key/value pair at a time that to be called again and again for unpacking purposes.

# Getting the current year out of the Operating System.
today = date.today().strftime('%Y')  # Getting the year of the current date from the Operating System

while running:
    new_name = input("Please enter the name and value according to this format 'name, DD-MM-YYYY, or '0' for printing the result:\n")

    # choices
    if new_name == "0":
        # Start unpacking the dictionary that has all the information one by one
        for key, value in all_persons.items():  # Iterate throw the dictionary (all_persons)
            current_person['name'] = key  # It's the person's name
            current_person['info'] = value  # It's a list contains 2 elements [ age, the full name of the day ]
            unpacking(**current_person)

        if len(all_persons) > 1:
            print(f"The oldest one is {max(all_persons, key=all_persons.get)}")
            print(f"The youngest one is {min(all_persons, key=all_persons.get)}")

        else:
            print('There is no oldest or youngest person')
        print(f"Total People: {len(all_persons)}")
        running = False
    else:
        new_entry(new_name)
