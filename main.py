from Database import Database
from BudgetPlanner import BudgetPlanner

def main():
    # Connect to the database
    db = Database(host="localhost", user="root", password="racharacha123", database="budget_planner")
    planner = BudgetPlanner(db)

    while True:
        print("Hello! Welcome to the Budget Planner")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            planner.register()
        elif choice == '2':
            user = planner.login()
            if user:
                while True:
                    print("\n1. Set Salary\n2. Set Goal\n3. Input Monthly Expenses\n4. Display Budget Summary\n5. Logout")
                    action = input("Choose an action (1-5): ")

                    if action == '1':
                        planner.set_salary(user)
                    elif action == '2':
                        planner.set_goal(user)
                    elif action == '3':
                        planner.input_expenses(user)
                    elif action == '4':
                        planner.display_budget_summary(user)
                    elif action == '5':
                        planner.logout()
                        break
                    else:
                        print("Invalid option. Try again.")
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Try again.")

    db.close()  # Close the database connection

if __name__ == "__main__":
    main()