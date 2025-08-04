from datetime import datetime
import json 


class Expense:
    def __init__(self,date,category,amount:float,notes:str=None):
        try:
            self.date:str = datetime.strptime(date,"%Y-%m-%d").date().isoformat()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

        self.category = category
        self.amount = float(amount)
        self.notes = notes
    
    def to_dict(self):
        return{
            "date":self.date,
            "category":self.category,
            "amount":self.amount,
            "notes":self.notes
        }
    @classmethod
    def from_dict(cls,data):
        return cls(
            date=data.get("date", ""),
            category=data.get("category", ""),  
            amount=float(data.get("amount", 0)),
            notes=data.get("notes", "")
            )

def save_expenses_to_json(Expenses,filename):
   with open(f"{filename}.json", "w") as f:
    json.dump([e.to_dict() for e in Expenses], f, indent=4)

def load_expenses_from_json(filename):
    try:
        with open(f"{filename}.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Expense.from_dict(d) for d in data]
    except FileNotFoundError:
        return []


def get_expense_date():
    user_input = input("Enter date (YYYY-MM-DD) or leave empty for today: ")
    if user_input.strip():  # If there's something typed
        return user_input
    else:
        return datetime.today().strftime("%Y-%m-%d")


def add_expense():
    date = get_expense_date()
    category = input("Enter category (e.g. Food, Transport): ")
    amount = float(input("Enter amount: "))
    notes = input("Enter notes (optional): ")
    return Expense(date, category, amount, notes)


def main():
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

if __name__ == "__main__":
    main()



    


