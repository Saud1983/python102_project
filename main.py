def new_entry(person_name):
    """This function is for adding new entry to info dictionary"""

    add = True  # To give the user a chance to double check his entry before submitting it.
    while add:
        t_key = person_name  # To save a new kay temporarily until the final approval.
        t_value = input("Please Enter the age:\n")  # To save a new value temporarily until the final approval.
        # print(f"The person's name is: '{t_key}', and he is: '{t_value}' years old\n")
        # submit = input("Enter 'Y' to save the entry or simply enter any value to add them again\n").lower()
        submit = "y"
        if submit == "y":  # Save the new key/value pair to the phonebook.
            t_key = t_key.lower().capitalize()
            all_persons[t_key] = int(t_value)
            add = False


def unpacking(name, age):
    print(f'My name is {name}, and I am {age} years old')


running = True
all_persons = {}
current_person = {}
while running:
    new_name = input("Enter '.' for printing the result, or add a new name :\n")

    # choices
    if new_name == ".":
        for key, value in all_persons.items():
            current_person['name'] = key
            current_person['age'] = value
            unpacking(**current_person)
        running = False
    else:
        new_entry(new_name)
