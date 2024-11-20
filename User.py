class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.salary = 0
        self.goal = None
        self.goal_amount = 0
        self.months_needed = 0
        self.monthly_expenses = {}

    @staticmethod
    def create_user(username, password, db):
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        db.execute_query(query, (username, password))
        print(f"User {username} registered successfully!")

    @staticmethod
    def login_user(username, password, db):
        query = "SELECT * FROM users WHERE username = %s"
        user_data = db.fetch_one(query, (username,))
        if user_data and user_data[2] == password:  # Password is in the 3rd column
            print(f"Welcome back, {username}!")
            return User(user_data[0], user_data[1], user_data[2])
        else:
            print("Invalid username or password. Please try again.")
            return None

    def set_salary(self, salary, db):
        query = "UPDATE users SET salary = %s WHERE id = %s"
        db.execute_query(query, (salary, self.id))
        print(f"Salary set to {salary} for user {self.username}")

    def set_goal(self, goal, goal_amount, months_needed, db):
        query = "UPDATE users SET goal = %s, goal_amount = %s, months_needed = %s WHERE id = %s"
        db.execute_query(query, (goal, goal_amount, months_needed, self.id))
        print(f"Goal set to {goal} with target amount {goal_amount} over {months_needed} months.")

    def add_expense(self, expense_name, amount, db):
        query = "INSERT INTO expenses (user_id, expense_name, amount) VALUES (%s, %s, %s)"
        db.execute_query(query, (self.id, expense_name, amount))
        print(f"Expense '{expense_name}' of {amount} added successfully.")