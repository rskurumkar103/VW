import os


class ShoppingList:
    FILE_NAME = "shopping_list.txt"

    def __init__(self):
        self.items = {}  # Dictionary: {item_name: quantity}
        self.load_items()

    def start_menu(self):
        print("What do you want to add to your shopping list?")
        print("Commands:")
        print("  DONE    - Save and exit")
        print("  HELP    - Show this menu")
        print("  SHOW    - Display shopping list")
        print("  REMOVE  - Remove an item")
        print("  CLEAR   - Empty the entire list")
        print("  SEARCH  - Search for an item")
        print("You may add quantities like: Milk x2")
        print("-----------------------------------------")

    def normalize_item(self, item):
        return item.strip().capitalize()

    def parse_item(self, user_input):
        
        parts = user_input.lower().split(" x")
        name = self.normalize_item(parts[0])
        quantity = 1

        if len(parts) > 1:
            try:
                quantity = int(parts[1])
                if quantity <= 0:
                    quantity = 1
            except ValueError:
                quantity = 1

        return name, quantity

    def add_to_list(self, user_input):
        name, quantity = self.parse_item(user_input)

        if not name:
            print("Cannot add an empty item.")
            return

        if name in self.items:
            self.items[name] += quantity
            print(f"Updated {name} quantity to {self.items[name]}.")
        else:
            self.items[name] = quantity
            print(f"{name} was added to your shopping list.")

        print(f"You have {len(self.items)} unique items on your list.")

    def remove_item(self, item):
        name = self.normalize_item(item)

        if name in self.items:
            del self.items[name]
            print(f"{name} was removed from your shopping list.")
            print(f"You have {len(self.items)} items on your list.")
        else:
            print(f"{name} was not found in your shopping list.")

    def show_shopping_list(self):
        print("My Shopping List:")
        if not self.items:
            print("(Your shopping list is empty.)")
            return

        for item in sorted(self.items.keys()):
            quantity = self.items[item]
            if quantity > 1:
                print(f"- {item} x{quantity}")
            else:
                print(f"- {item}")

    def search_items(self, term):
        term = term.lower()
        results = [item for item in self.items if term in item.lower()]

        if not results:
            print("No matching items found.")
        else:
            print("Search Results:")
            for item in sorted(results):
                qty = self.items[item]
                print(f"- {item} x{qty}" if qty > 1 else f"- {item}")

    def clear_list(self):
        confirm = input("Are you sure you want to clear the entire list? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.items.clear()
            print("Shopping list cleared.")
        else:
            print("Clear cancelled.")

    def save_items(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                for item, quantity in self.items.items():
                    file.write(f"{item},{quantity}\n")
        except IOError:
            print("Error saving shopping list.")

    def load_items(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        try:
                            name, quantity = line.split(",")
                            self.items[self.normalize_item(name)] = int(quantity)
                        except ValueError:
                            continue
        except IOError:
            print("Error loading shopping list.")


def main():
    shopping_list = ShoppingList()
    shopping_list.start_menu()

    try:
        while True:
            user_input = input("> ").strip()

            if not user_input:
                continue

            command = user_input.upper()

            if command == "DONE":
                shopping_list.save_items()
                print("See you soon! Your shopping list has been saved.")
                shopping_list.show_shopping_list()
                break

            elif command == "HELP":
                shopping_list.start_menu()

            elif command == "SHOW":
                shopping_list.show_shopping_list()

            elif command == "REMOVE":
                shopping_list.show_shopping_list()
                item_to_remove = input("What do you want to remove?: ").strip()
                shopping_list.remove_item(item_to_remove)

            elif command == "CLEAR":
                shopping_list.clear_list()

            elif command == "SEARCH":
                term = input("Enter search term: ").strip()
                shopping_list.search_items(term)

            else:
                shopping_list.add_to_list(user_input)

    except EOFError:
        shopping_list.save_items()
        print("\nEOF detected. Your shopping list has been saved. Goodbye!")


if __name__ == "__main__":
    main()
