 Smart Expense Tracker with Auto Category & Alerts

def auto_category(note):
    note = note.lower()

    if any(word in note for word in ["food", "pizza", "burger", "lunch", "dinner", "tea", "coffee"]):
        return "Food"
    elif any(word in note for word in ["bus", "cab", "uber", "auto", "train", "petrol"]):
        return "Travel"
    elif any(word in note for word in ["book", "course", "fees", "pen", "notebook", "exam"]):
        return "Study"
    elif any(word in note for word in ["movie", "party", "game", "shopping", "fun"]):
        return "Fun"
    else:
        return "Other"


budget = float(input("Enter your monthly budget limit (₹): "))
total_expense = 0
expenses = []

while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount (₹): "))
        note = input("Enter note: ")

        category = auto_category(note)
        total_expense += amount
        expenses.append((amount, category, note))

        with open("expenses.txt", "a") as file:
            file.write(f"{amount} | {category} | {note}\n")

        print(f"Expense added   (Category: {category})")

        if total_expense > budget:
            print(" ALERT: Budget exceeded!")

    elif choice == "2":
        print("\n--- All Expenses ---")
        try:
            with open("expenses.txt", "r") as file:
                data = file.read()
                if data.strip() == "":
                    print("No expenses found.")
                else:
                    print(data)
        except FileNotFoundError:
            print("No expense file found.")

    elif choice == "3":
        print("\n--- Summary ---")
        print(f"Total Spent: ₹ {total_expense}")
        print(f"Remaining Balance: ₹ {budget - total_expense}")

        category_total = {}
        for amount, category, note in expenses:
            category_total[category] = category_total.get(category, 0) + amount

        print("\nCategory-wise Expense:")
        for cat, amt in category_total.items():
            print(f"{cat}: ₹ {amt}")

    elif choice == "4":
        print("Exiting... Bye ")
        break

    else:
        print("Invalid choice .... Try again.")
