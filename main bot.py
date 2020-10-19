import random
from home_remedies import home_remedies
from medical_remedies import medical_remedies
from calculations import calculations
def greet_and_introduce():
    response = ["Hi, I'm your medical assistant. May i know your good name?",
    "it's your medical assistant. Could you tell me your name? "]
    print(random.choice(response))

def welcome(name):
    messages=["nice to meet you. How can i help you today?",
    "It's a pleasure meeting you. what would you like to know today?",
    ]
    print(random.choice(messages))

def show_menu():
    print("-----------------")
    print("1.Home remedies")
    print("2.medication")
    print("3.caluclations")
    print("4.exit")
    print("-----------------")
    try:
        return int(input("enter your choice [1-4]:"))
    except:
        print("Can't find this option")
    
def bot():
    greet_and_introduce()
    name=input("name:")
    welcome(name)
    choice=show_menu()
    while(choice != 4):
        if choice == 1:
            home_remedies()
        elif choice == 2:
            medical_remedies()
        elif choice == 3:
            calculations()
        else:
            print("I can't understand")
        choice = show_menu()


bot()