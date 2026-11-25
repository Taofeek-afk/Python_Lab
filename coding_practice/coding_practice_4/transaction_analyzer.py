transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "salary", "amount": 500000, "type": "income"},
    {"name": "internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "food", "amount": 45000, "type": "expense"},
]


def transaction_analyzer(transaction: list[dict]):
    total_income = 0
    expense = 0
    status = "Balanced"
    
    highest_expense = 0
    largest_expense = ""
    
    num_of_expense = 0
    
    for row in transactions:
        if row["type"] == "income":
            total_income += row["amount"]
        elif row["type"] == "expense":
            expense += row["amount"]
            num_of_expense += 1
        
        if row["amount"] > highest_expense and row["type"] == "expense":
            highest_expense = row["amount"]
            largest_expense = row["name"]
        
    if total_income - expense < total_income//2:
        status = "Loss"
    elif total_income - expense > total_income//2:
        status = "Profit"

    return total_income, expense, (total_income-expense), (largest_expense, highest_expense), num_of_expense, status


total_income, expense, balance, largest_expense, num_of_expense, status = transaction_analyzer(transactions)

print("Total income:", total_income)
print("Expense:", expense)
print("Balance:", balance)
print("Largest Expense:", f"{largest_expense[0]}({largest_expense[1]})")
print("num_of_expense:", num_of_expense)
print("status:", status)
