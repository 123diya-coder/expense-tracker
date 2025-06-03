import json
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

expenses = []

# 🔽 Load data from file
def load_expenses_from_file():
    global expenses
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            try:
                expenses = json.load(file)
            except json.JSONDecodeError:
                expenses = []

# 🔼 Save data to file
def save_expenses_to_file():
    with open("data.json", "w") as file:
        json.dump(expenses, file, indent=4)

# ➕ Add expense
def add_expense():
    try:
        amount = float(input(Fore.YELLOW + "💰 Enter amount: ₹"))
    except ValueError:
        print(Fore.RED + "❌ Invalid amount! Please enter a valid number.")
        return

    category = input(Fore.YELLOW + "📂 Enter category: ").strip()
    note = input(Fore.YELLOW + "📝 Note (optional): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses.append(expense)
    save_expenses_to_file()
    print(Fore.GREEN + f"✅ Expense added: ₹{amount} in {category} - {note}")

# 👀 View expenses
def view_expenses():
    if not expenses:
        print(Fore.BLUE + "📭 No expenses recorded yet.")
        return

    print(Fore.CYAN + "\n📋 Your Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} ({exp['note']})")
    print()

# 🗑️ Delete an expense
def delete_expense():
    view_expenses()
    try:
        index = int(input(Fore.YELLOW + "❌ Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses_to_file()
            print(Fore.RED + f"🗑️ Deleted: ₹{removed['amount']} - {removed['category']}")
        else:
            print(Fore.RED + "❌ Invalid index.")
    except ValueError:
        print(Fore.RED + "❌ Please enter a valid number.")

# 📌 Main loop
def main():
    load_expenses_from_file()

    while True:
        print(Fore.MAGENTA + "\n💼 Expense Tracker Menu:")
        print("1. ➕ Add Expense")
        print("2. 👀 View Expenses")
        print("3. 🗑️ Delete Expense")
        print("4. 🚪 Exit")

        choice = input(Fore.CYAN + "🔘 Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print(Fore.GREEN + "👋 Bye! Expense Tracker closed.")
            break
        else:
            print(Fore.RED + "❌ Invalid choice! Please select 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
