import random, string, time, asyncio, os, json, keyboard

async def start():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> _
    ''')

async def start1():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> r_
    ''')

async def start2():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> ru_
    ''')

async def start3():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> run_
    ''')

async def start4():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> run _
    ''')

async def start5():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> run .\game.exe_
    ''')

async def start6():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> run .\game.exe
    ''')

async def home():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> run .\game.exe


     █   █▀▀▀ █▀▀█ █▀▄▀█ █▀▀   █▀▀ █ █ █▀▀
      █  █ ▀█ █▄▄█ █ ▀ █ █▀▀   █▀▀ ▄▀▄ █▀▀
    ▀  █ ▀▀▀▀ ▀  ▀ ▀   ▀ ▀▀▀ ▀ ▀▀▀ ▀ ▀ ▀▀▀

    ''')

async def home1():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r'''

    PS C:\User> run .\game.exe


     █   █▀▀▀ █▀▀█ █▀▄▀█ █▀▀   █▀▀ █ █ █▀▀
      █  █ ▀█ █▄▄█ █ ▀ █ █▀▀   █▀▀ ▄▀▄ █▀▀
    ▀  █ ▀▀▀▀ ▀  ▀ ▀   ▀ ▀▀▀ ▀ ▀▀▀ ▀ ▀ ▀▀▀


    Welcome to the HARDEST quiz about coding that will EVER be submitted in this assessment!


    ''')
    

def qONE():
    print(r'''
    Question 1: Which one of these is correct?

    1: print(Hello World!)
    2: Hello World!
    3: print("Hello World!")
    4: print Hello World!

    ''')
    option=input("    ")
    if option == "1":
        print('\n    Wrong Answer! The correct answer is 3: print("Hello World!")\n')
    elif option == "2":
        print('\n    Wrong Answer! The correct answer is 3: print("Hello World!")\n')
    elif option == "3":
        print('\n    Correct Answer!\n')
    elif option == "4":
        print('\n    Wrong Answer! The correct answer is 3: print("Hello World!")\n')
    elif option == "hint":
        print("\n    You don't need a hint! Please try again. (╯°□°）╯︵ ┻━┻\n")
        time.sleep(1.5)
        qONE()        
    else:
        print("\n    That isnt a valid answer! Please try again.\n")
        time.sleep(1.5)
        qONE()
        
def qTWO():
    print(r'''
    Question 2: Which one of these is correct?

    1: input "Press [ENTER] to continue."
    2: input("Press [ENTER] to continue.")
    3: input(Press [ENTER] to continue.)
    4: Press [ENTER] to continue.

    ''')
    option=input("    ")
    if option == "1":
        print('\n    Wrong Answer! The correct answer is 2: input("Press [ENTER] to continue.") \n')
    elif option == "2":
        print('\n    Correct Answer!\n')
    elif option == "3":
        print('\n    Wrong Answer! The correct answer is 2: input("Press [ENTER] to continue.")\n')
    elif option == "4":
        print('\n    Wrong Answer! The correct answer is 2: input("Press [ENTER] to continue.")\n')
    elif option == "hint":
        print("\n    You don't need a hint! Please try again. (╯°□°）╯︵ ┻━┻\n")
        time.sleep(1.5)
        qTWO()        
    else:
        print("\n    That isnt a valid answer! Please try again.\n")
        time.sleep(1.5)
        qTWO()
        
def qTHREE():
    print(r'''
    Question 3: Which one of these is correct?

    1: if name is not "Bob":
    2: if the name isnt "Bob":
    3: if name not == "Bob":
    4: if name != "Bob":

    ''')
    option=input("    ")
    if option == "1":
        print('\n    Wrong Answer! The correct answer is 4: if name != "Bob":\n')
    elif option == "2":
        print('\n    Wrong Answer! The correct answer is 4: if name != "Bob":\n')
    elif option == "3":
        print('\n    Wrong Answer! The correct answer is 4: if name != "Bob":\n')       
    elif option == "4":
        print('\n    Correct Answer!\n')
    elif option == "hint":
        print("\n    You don't need a hint! Please try again. (╯°□°）╯︵ ┻━┻\n")
        time.sleep(1.5)
        qTHREE()        
    else:
        print("\n    That isnt a valid answer! Please try again.")
        time.sleep(1.5) 
        qTHREE()     

def qFOUR():
    print(r'''
    Question 4: Which one of these is NOT a programming language?

    1: JavaScript
    2: Python
    3: HTML
    4: Excel

    ''')
    option=input("    ")
    if option == "1":
        print('\n    Wrong Answer! The correct answer is 3: HTML\n')
    elif option == "2":
        print('\n    Wrong Answer! The correct answer is 3: HTML\n')
    elif option == "3":
        print('\n    Correct Answer!\n')       
    elif option == "4":
        print('\n    Wrong Answer! The correct answer is 3: HTML\n')
    elif option == "hint":
        print("\n    You don't need a hint! Please try again. (╯°□°）╯︵ ┻━┻\n")
        time.sleep(1.5)
        qFOUR()        
    else:
        print("\n    That isnt a valid answer! Please try again.")
        time.sleep(1.5)
        qFOUR()

def qFIVE():
    print(r'''
    Question 5: What is Python used for?

    1: Automate Tasks
    2: Make software
    3: Build websites
    4: All of the above

    ''')
    option=input("    ")
    if option == "1":
        print('\n    Wrong Answer! The correct answer is 4: All of the above\n')
    elif option == "2":
        print('\n    Wrong Answer! The correct answer is 4: All of the above\n')
    elif option == "3":
        print('\n    Wrong Answer! The correct answer is 4: All of the above\n')
    elif option == "4":
        print('\n    Correct Answer!\n')       
    elif option == "hint":
        print("\n    You don't need a hint! Please try again. (╯°□°）╯︵ ┻━┻\n")
        time.sleep(1.5)
        qFOUR()        
    else:
        print("\n    That isnt a valid answer! Please try again.")
        time.sleep(1.5)
        qFIVE()

def end():
    print("    Thank you for playing!\n\n    Made by Jack Weller! =)")
