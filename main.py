while True:
    print("Password Manager")
    print("----------------")
    print("1. Create new password")
    print("2. View password")
    print("3. Delete password")
    print("4. Show all passwords")
    print("5. Update password")
    print("6. Exit")
    print("----------------")
    print("Enter your choice: ", end="")
    choice = int(input())
    match choice:
        case 1:
            try:
                create_password()
            except Exception as e:
                print("Error: ", e)
        case 2:
            try:
                view_password()
            except Exception as e:
                print("Error: ", e)
        case 3:
            try:
                delete_password()
            except Exception as e:
                print("Error: ", e)
        case 4:
            try:
                show_all_passwords()
            except Exception as e:
                print("Error: ", e)
        case 5:
            try:
                update_password()
            except Exception as e:
                print("Error: ", e)
        case 6:
            try:
                print("Exiting...")
                break
            except Exception as e:
                print("Error: ", e)
        case _:
            print("Invalid choice")