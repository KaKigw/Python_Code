from Smart_Expense_Tracker import Expense,save_expenses_to_json,load_expenses_from_json,get_expense_date,add_expense
import streamlit as st



filename = input("Which file do you want to save on?").strip()
expenses = load_expenses_from_json(filename)
print(f"Loaded {len(expenses)} expense(s).\n")

while True:
    print("\nMenu:")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Save and exit")

    choice = input("Choose an option: ")

    if choice == "1":
        new_expense = add_expense()
        expenses.append(new_expense)
        print("Expense added.")
    elif choice == "2":
        for e in expenses:
            print(f"- {e.date}: {e.category} - ${e.amount} ({e.notes})")
    elif choice == "3":
        save_expenses_to_json(expenses,filename)
        print(f"Expenses saved in {filename}.json. Exiting...")
        break
    else:
        print("Invalid choice. Try again.")


