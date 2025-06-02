import json
import os

expenses = []

# 🔄 Load existing data from data.json if it exists
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        try:
            expenses = json.load(f)
        except json.JSONDecodeError:
            expenses = []

def save_expenses():
    with open("data.json", "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("❌ Invalid amount! Please enter a valid number.")
        return
    
    category = input("Enter category: ").strip()
    note = input("Note (optional): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses.append(expense)
    save_expenses()  # 🧠 Save to file
    print(f"✅ Expense added: ₹{amount} in {category} - {note}")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\nYour Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} ({exp['note']})")
    print()

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Bye! Expense Tracker closed.")
            break
        else:
            print("Invalid choice! Please select 1, 2 or 3.")

if __name__ == "__main__":
    main()
