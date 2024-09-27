class Budget:
    def __init__(self, name, income, savings):
        self.name = name
        self.income = income
        self.expense = 0
        self.savings = savings
        self.expenses = {}
        self.amount_left = 0

    def add_expenditure(self):
        expense_description = input('Enter expense description: ')
        expense_amount = int(input('Enter expense amount: '))
        self.expenses[expense_description] = expense_amount
        self.expense += expense_amount
        print(f'Added new expense: {expense_description}, Amount: {expense_amount}')

    def budget_details(self):
        print(f"\nBudget details for {self.name}:")
        print(f'Total Budget: {self.income}')
        print('Expenses:')
        if self.expenses:
            for description, amount in self.expenses.items():
                print(f'- {description}: {amount}')
        else:
            print("No expenses added yet.")
        
        total_spent = sum(self.expenses.values())
        self.amount_left = self.income - total_spent - self.savings
        print(f'Total spent: {total_spent}')
        print(f'Amount left for luxuries: {self.amount_left}')

    def saving_details(self):
        savings_amount = int(input('Enter amount to add to savings: '))
    
    # Scenario 1: Check if savings amount is more than the amount left for luxuries
        if savings_amount > self.amount_left:
            print(f'Not enough funds to add {savings_amount} to savings. You only have {self.amount_left} left.')
    # Scenario 2: Check if the total savings would exceed the total income
        elif (self.savings + savings_amount) > self.income:
            print(f'Cannot save {savings_amount}, as total savings would exceed your income of {self.income}.')
        else:
            self.savings += savings_amount
            self.amount_left -= savings_amount
            print(f'Amount {savings_amount} added to savings. Current savings: {self.savings}. Amount left: {self.amount_left}')


# Manage multiple users
users = {}

print('Welcome to the Multi-User Budget App')

while True:
    print('\nWhat would you like to do?')
    print('1. Create a new user budget')
    print('2. Select an existing user')
    print('3. Exit')
    choice = int(input('Enter your choice (1/2/3): '))
    
    if choice == 1:
        name = input('Enter your name: ')
        if name in users:
            print(f"User '{name}' already exists.")
        else:
            income = int(input('Enter your income: '))
            savings = int(input('Enter your savings: '))
            users[name] = Budget(name, income, savings)
            print(f'Budget created for {name}.')
    
    elif choice == 2:
        name = input('Enter the user name: ')
        if name in users:
            user_budget = users[name]
            while True:
                print(f"\nUser: {name}")
                print('1. Add an expense')
                print('2. Show budget details')
                print('3. Add savings')
                print('4. Exit')
                user_choice = int(input('Enter your choice (1/2/3/4): '))
                
                if user_choice == 1:
                    user_budget.add_expenditure()
                elif user_choice == 2:
                    user_budget.budget_details()
                elif user_choice == 3:
                    user_budget.saving_details()
                elif user_choice == 4:
                    break
                else:
                    print('Invalid choice. Please choose from the options.')
        else:
            print(f"User '{name}' not found.")
    
    elif choice == 3:
        print('Exiting the application.')
        break

    else:
        print('Invalid choice. Please choose from the options.')
        
print('Thanks for choosing budget app! Hope to see you soon!!')
