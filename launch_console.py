name = input("What is your name? ")
print("Welcome to " + name + "'s Launch Console!")
print("Now you will select an option from a list to gain insights on " + name + "'s Backstory!")
running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Why I joined this program")
    print("4) Exit")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print("I'm a builder-in-training at Code2College.")
    elif choice == "2":
        print("My goal is to ship my first real project this term and to show up consistently and learn powerful information.")
    elif choice == "3":
        print("To get a headstart on my career, make strong connections, and immerse myself in the field of Information Technology.")
    elif choice == "4":
        running = False
        
    else:
        print("Please pick 1, 2, 3, or 4.")