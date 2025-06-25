def menu():
    while True:
        print("choose your operation by the number indicated against it")
        print("1. Add New Password")
        print("2. View All Passwords")
        print("3. Search Password")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == '1':
            print(" Add Password - Work in progress")
        elif choice == '2':
            print(" View All - Work in progress")
        elif choice == '3':
            print(" Search - Work in progress")
        elif choice == '4':
            print(" Delete - Work in progress")
        elif choice == '5':
            print(" Exiting KeyNest...")
            break
        else:
            print("Invalid choice. Please select a valid option.")