# Emma McNeill
# Purpose: the purpose of this program is to display a list
# of pets, ask the user to choose a pet, and give the user more
# information about that pet.


import pymysql
from pets import Pet
from creds import *

#SQL Command to retrieve the desired data
petSelect = """
    select 
        pets.id,
        pets.name as petName,
        pets.age,
        owners.name as ownerName, 
        types.animal_type as animalType
    from pets 
        join owners on pets.owner_id = owners.id 
        join types on pets.animal_type_id = types.id;
    """

# this will allow the user to end the program nicely
toQuit = {"q", "quit"}

def endProgram():
    print("Thanks for choosing a pet!")
    exit()


def endStuff():
    try:
        input("Press [ENTER] to continue.")
    except EOFError:
        print("Thanks for not saving the animals.... exiting...")
        endProgram()
    except Exception as e:
        print(f"An error has occurred. Exiting: {e}")
        endProgram()

try:

    myConnection = pymysql.connect(host="localhost",
                                   user="root",
                                   password=password,
                                   db="pets",
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
except EOFError:
    print("Ending pet chooser program... See you later. ")
    endProgram()
except Exception as e:
    print(f"An error has occurred. Exiting: {e}")
    print()
    exit()

# connect to data
with myConnection.cursor() as cursor:
    cursor.execute(petSelect)
    petDict = cursor.fetchall()


listPets = list()

for pet in petDict:
    listPets.append(Pet(pet["petName"],
                          pet["ownerName"],
                          pet["age"],
                          pet["animalType"]))

#menu of pets
while True:
    # print the list of pets
    print("Here is our list of pets:")
    for i in range(0, len(listPets)):
        print("",i+1,")", listPets[i].petName)
    print(f"If you would like to quit, enter q or Q")
    print()
    #choose pet
    try:
        print("Enter the integer corresponding to the pet you choose.")
        choice = input("Choice:   ")
        print()
# if q or Q is entered, end program
        if choice.lower() in toQuit:
            endProgram()
        choice = int(choice)
        if choice not in range(1, len(listPets) + 1):
            raise ValueError

    except ValueError:
        print("Invalid selection. Please enter an integer on your list of pets.")
        print()
        endStuff()
    except Exception as e:
        print(f"An error has occurred.  Exiting: {e}")
        endProgram()
    else:
        print("You chose " + listPets[choice - 1].petName + "! " + listPets[choice - 1].petName + " is a " + listPets[choice - 1].animalType + ".",
              listPets[choice - 1].petName + " is " + str(listPets[choice - 1].petAge) + " years old.",
              listPets[choice - 1].petName + "'s owner is " + listPets[choice - 1].ownerName + ".")
        print()
        endStuff()