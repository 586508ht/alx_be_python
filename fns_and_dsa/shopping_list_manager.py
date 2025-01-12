# shopping_list_manager.py

def main():
    shopping_list = []  # Initialize an empty shopping list

    while True:
        # Display the menu
        print("\nShopping List Manager")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the list")
        print("4. Exit")

        # Get the user's choice
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")
        elif choice == '2':
            # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the list.")
        elif choice == '3':
            # View the list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("\nThe shopping list is empty.")
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
