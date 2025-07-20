# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. View list")
    print("3. Remove item")
    print("4. Exit")

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

def view_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def remove_item():
    try:
        item_number = int(input("Enter the number of the item to remove: "))
        if 1 <= item_number <= len(shopping_list):
            removed = shopping_list.pop(item_number - 1)
            print(f"{removed} removed from the shopping list.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_list()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
