import time
import os
import msvcrt
import json

def save_expenses(expenses):
    with open("data.json", "w") as outfile:
        json.dump(expenses, outfile, indent=4)

def load_expenses():
    try:
        with open("data.json", "r") as infile:
            return json.load(infile)
    except FileNotFoundError:
        return [] 

def save_income(income):
    with open("income.json", "w") as outfile:
        json.dump(income, outfile, indent=4)

def load_income():
    try:
        with open("income.json", "r") as infile:
            return json.load(infile)
    except FileNotFoundError:
        return {"income" :0} 


    
def animate_loading(text):
    os.system("cls")
    frames = ["|", "/", "-", "\\", "|", ""]
    for frame in frames:    
        print(f"\r{text[0]} {frame}", end = " ", flush=True)
        time.sleep(0.3)
    os.system("cls")
    print(f"\r{text[1]} ", end=" ", flush=True)
    print()
    
def update_income(incomeload, income):
    incomeload["income"] = income
    save_income(incomeload)
    

def add_expense(expenses, amount, item, category):
    expenses.append({'amount': amount, 'item': item, 'category': category})
    save_expenses(expenses)
    
def print_expenses(expenses, income):   
    if (not expenses):
        print("-------------------------------------")
        print("\t Your cart is empty")
        print("-------------------------------------")
        print("Press e to exit")
        while True:
            key = msvcrt.getch().decode("utf-8").lower()  
            if key == 'e':
                break
            else:
                print("Wrong Key")
    else:
        print("---------------------------------------------------------------------------------")
        print(f'{"S.N":<5} | {"Item":<15} | {"Amount":<20} | {"Category":<15}')
        print("---------------------------------------------------------------------------------")
        for i, expense in enumerate(expenses, start=1):
            print(f'{i:<5} | {expense["item"].capitalize():<15} | {expense["amount"]:<20} | {expense["category"].capitalize():<15}')
        
        print("----------------------------------------------------------------------------------")
    
        total = total_expenses(expenses)
        print(f"{'':<5} | {'':<15} | Total: {total:<13} | {'':<15}")
        if (income < total):
            sub = total - income
            print(f"WARNING! Your savings are less than expenses by {sub}")
        print("-----------------------------------------------------------------------------------")
    
        print("Press e to exit")
        while True:
            key = msvcrt.getch().decode("utf-8").lower()  
            if key == 'e':
                break
            else:
                print("Wrong Key")
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'].lower() == category.lower(), expenses))
    

def main():
    expenses = load_expenses()
    incomeobj = load_income()
    income = incomeobj["income"]
    while True:
        os.system("cls")
        print("----------------------------------")
        print('|\tExpense Tracker          |')
        print("----------------------------------")
        print('| 1. Add an expense              |')
        print('| 2. List all expenses           |')
        print('| 3. Filter expenses by category |')
        print('| 4. Your Income                 |')
        print('| 5. Exit                        |')
        print("----------------------------------")
       
        choice = input('Enter your choice: ')
        try:
            if choice == '1':
                animate_loading(["Loading ", "Loaded Sucessfully "])
                time.sleep(0.5)
                print("----------------------------------")
                item = input("Enter item name:")
                while True:
                    try:
                        amount = float(input('Enter cost amount: '))
                        break
                    except ValueError:
                            print("Please enter a number value")
                category = input('Enter category: ')
                print("----------------------------------")
                animate_loading(["Adding to Cart","Added item to cart Succesfully"])
                time.sleep(1)

                
                add_expense(expenses, amount, item, category)
            elif choice == '2':
                animate_loading(["Loading Cart", "Cart Loaded Successfully"])
                time.sleep(0.8)
                print_expenses(expenses, income)
                
                
            elif choice == '3':
                os.system("cls")
                category = input('Enter category to filter: ')
                animate_loading(["Loading cart", "Loaded Successfully"])
                print(f'\nExpenses for {category.capitalize()}:')
                expenses_from_category = filter_expenses_by_category(expenses, category)
                if(not expenses_from_category):
                    print("-------------------------------------------------")
                    print(f"\tNo such item found as {category}")
                    print("-------------------------------------------------")
                    print("Press e to exit")
                    while True:
                        key = msvcrt.getch().decode("utf-8").lower()  
                        if key == 'e':
                            break
                        else:
                            print("Wrong Key")
                else:     
                    print_expenses(expenses_from_category, income)
            
            elif choice == '4':
                while True:
                    os.system("cls")
                    print("----------------------------------")
                    print(f'   Your current saving :  {income}\t')
                    print('|                                |')
                    print('|    Press a to add savings      |')
                    print('|  Press s to subtract savings   |')
                    print('|       Press e to exit          |')
                    print("----------------------------------")
                    key = msvcrt.getch().decode("utf-8").lower()  
                    if key == 'e':
                        break
                    
                    elif key =='a':
                        while True:
                            try:
                                os.system("cls")
                                print("Enter e if u want to exit")
                                add = input('How much do you want add: ')
                                if(add=="e"):
                                    break
                                income = income + float(add)
                                os.system("cls")
                                animate_loading(["Adding savings to your account", "Savings Added Successfully"])
                                update_income(incomeobj, income)
                                time.sleep(2)
                                break
                            except ValueError:
                                os.system("cls")
                                print("Please enter a number value")
                                time.sleep(2)
                    elif key =='s':
                        while True:
                            try:
                                os.system("cls")
                                print("Enter e if u want to exit")
                                sub = input('How much do you want subtract: ')
                                if(sub=="e"):
                                    break
                                income = income - float(sub)
                                animate_loading(["Subtracting savings to your account", "Savings Subtracted Successfully"])

                                update_income(incomeobj, income)
                                time.sleep(2)
                                break
                            except ValueError:
                                os.system("cls")
                                print("Please enter a number value")
                                time.sleep(2)
                    else:
                        print("Wrong Key")
                        time.sleep(2)
                        
            elif choice == '5':
                print('Exiting the program.')
                break
            else :
                time.sleep(0.5)
                print("The Selected Choice doesn't exist")
                time.sleep(1)
        except Exception as e:
            print(f"An error occured: {e}")

main()