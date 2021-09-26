import datetime
from datetime import date


def new_entry():
    """This function is for adding new entry to info dictionary"""

    add = True  # To give the user a chance to double check his entry before submitting it.
    while add:
        new_key = input("Please Enter the person name:\n")  # To save a new kay temporarily until the final approval.
        new_value = input("Please Enter the birth day in this format DD-MM-YYYY:\n")  # To save a new value temporarily until the final approval.
        # print(f"The person's name is: '{new_key}', and hers/his birth day on '{new_value}' \n")
        # submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()
        submit = "y"
        if submit == "y":  # Save the new key/value pair to the a dictionary named all_persons.
            new_key = new_key.lower().capitalize()  # It's the person's name that will be a key in the dictionary after giving it a proper formatting

            # Getting the current year out of the Operating System.
            today = date.today()  # The current date from the Operating System
            today = today.strftime('%Y')  # The year of the current date

            # Getting the current year out of the given birthday of the current person.
            birthday_year = new_value.split('-')[2]  # The year of the current given birthday

            # Getting the name of the day out of the given birthday of the current person
            birthday = new_value.split('-')  # Converting the current birthday to a list that has 3 elements
            birthday = datetime.date(int(birthday[2]), int(birthday[1]), int(birthday[0]))  # Converting the current birthday from a string type to a datetime type in a proper order(Y,M,D)/type(integer) arguments that datetime.date work with.
            day_name = birthday.strftime('%A')  # Retrieving the full day name as a string
            all_persons[new_key] = [int(today) - int(birthday_year), day_name]  # Add a new key/value pair to the dictionary where the kay is the person's name, and the value is a list of 2 element, one is the person's age, and the second one is the day name
            add = False


def unpacking(name, info):
    print(f'{name} is {info[0]} years old, and she/he was born on {info[1]}')


running = True
all_persons = {}  # Initial value of a global dictionary that saves all entries.
current_person = {}  # Initial value of a global dictionary that save only one key/value pair at a time that to be called again and again for unpacking purposes.


while running:
    new_name = input("Enter '0' for printing the result, or enter '1' to add a new name :\n")

    # choices
    if new_name == "0":
        # Start unpacking the dictionary that has all the information one by one
        for key, value in all_persons.items():  # Iterate throw the dictionary (all_persons)
            current_person['name'] = key  # It's the person's name
            current_person['info'] = value  # It's a list contains 2 elements [ age, the full name of the day ]
            unpacking(**current_person)

        running = False
    else:
        new_entry()
