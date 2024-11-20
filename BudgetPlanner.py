from User import User


class BudgetPlanner:
    def __init__(self, db):
        self.db = db

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        User.create_user(username, password, self.db)

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return User.login_user(username, password, self.db)

    def logout(self):
        print("You have successfully logged out.\n")

    def set_salary(self, user):
        salary = float(input("Enter your monthly salary: "))
        user.set_salary(salary, self.db)

    def set_goal(self, user):
        goal = input("Enter your goal (e.g., Car, House, etc.): ")
        goal_amount = float(input(f"How much will the {goal} cost? "))
        months_needed = int(input(f"How many months will it take to achieve your goal? "))
        user.set_goal(goal, goal_amount, months_needed, self.db)

    def input_expenses(self, user):
        print("Enter your monthly expenses:")
        while True:
            expense_name = input(
                "Enter expense name (e.g., Internet, Water, Electricity, etc.) or type 'done' to finish: ")
            if expense_name.lower() == 'done':
                break
            amount = float(input(f"How much do you pay for {expense_name}? "))
            user.add_expense(expense_name, amount, self.db)

    def display_budget_summary(self, user):
        query = "SELECT salary, goal, goal_amount, months_needed FROM users WHERE id = %s"
        user_data = self.db.fetch_one(query, (user.id,))

        salary = user_data[0]
        goal = user_data[1]
        goal_amount = user_data[2]
        months_needed = user_data[3]

        query = "SELECT SUM(amount) FROM expenses WHERE user_id = %s"
        total_expenses = self.db.fetch_one(query, (user.id,))[0] or 0  # Default to 0 if no expenses

        monthly_goal_contribution = goal_amount / months_needed if months_needed > 0 else 0
        remaining_after_expenses = salary - total_expenses - monthly_goal_contribution

        print(f"\nBudget Summary for your goal of {goal}:")
        print(f"Monthly Salary: {salary}")
        print(f"Total Monthly Expenses: {total_expenses}")
        print(f"Amount to be saved each month for your goal: {monthly_goal_contribution:.2f}")
        print(f"Remaining after expenses and goal savings: {remaining_after_expenses:.2f}")

        if remaining_after_expenses > 0:
            print(f"You have {remaining_after_expenses:.2f} left to save or invest in other areas.")
        else:
            print("You don't have enough left after your expenses and goal savings. Consider reducing expenses or increasing your income.")