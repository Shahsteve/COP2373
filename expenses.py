from functools import reduce

# Create function that uses while and if loops to gather data from user or calculate total.
def get_expenses():

    expenses = []

    while True:
        expense_type = input("Enter expense type (or 'end' to finish): ")

        if expense_type.lower() == "end":
            break

        amount = float(input("Enter expense amount here: "))

        expenses.append({"type": expense_type, "amount": amount})

    return expenses

#Created functions to analyze data gathered from user and compares highest and lowest expenses as well as the
#total
def analyzeex(expenses):

    # Uses a lambda function to determine highest and lowest within list.
    total = reduce(lambda x, y: x + y["amount"], expenses, 0)

    highest = max(expenses, key=lambda x: x["amount"])

    lowest = min(expenses, key=lambda x: x["amount"])

    return total, highest, lowest

#Created a function to access data and print results of the first two functions.
def main():

    print("Enter monthly expenses below: ")

    expenses = get_expenses()

    total, highestex, lowestex = analyzeex(expenses)

    print("Total Expenses:", total)

    print("Highest Expense:", highestex["type"], "-", highestex["amount"])

    print("Lowest Expense:", lowestex["type"], "-", lowestex["amount"])

#Calls the main function
if __name__ == "__main__":
    main()