from functools import reduce


def get_expenses():
    """
    Prompts the user for the number of expenses and details for each expense.

    Returns:
        list: A list of tuples, where each tuple contains the expense type (str)
              and the expense amount (float).
    """
    expenses = []
    try:
        num_expenses = int(input("How many monthly expenses do you have? "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of expenses.")
        return expenses

    for i in range(num_expenses):
        expense_type = input(f"Enter the type of expense #{i + 1} (e.g., Rent, Groceries): ")
        try:
            expense_amount = float(input(f"Enter the amount for {expense_type}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
            continue
        expenses.append((expense_type, expense_amount))
    return expenses


def analyze_expenses(expenses):
    """
    Analyzes the list of expenses to compute the total expense,
    the highest expense, and the lowest expense using reduce.

    Args:
        expenses (list): A list of expense tuples (expense_type, expense_amount).

    Returns:
        tuple: A tuple containing:
               - total (float): Sum of all expense amounts.
               - highest_expense (tuple): The expense with the highest amount.
               - lowest_expense (tuple): The expense with the lowest amount.
    """
    if not expenses:
        return 0, ("N/A", 0), ("N/A", 0)

    # Calculate total expense
    total = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    # Calculate highest expense
    highest_expense = reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc, expenses)

    # Calculate lowest expense
    lowest_expense = reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc, expenses)

    return total, highest_expense, lowest_expense


def display_results(total, highest_expense, lowest_expense):
    """
    Displays the analysis of the expenses.

    Args:
        total (float): Total expense amount.
        highest_expense (tuple): Expense with the highest amount.
        lowest_expense (tuple): Expense with the lowest amount.
    """
    print("\nExpense Analysis:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")


def main():
    """
    Main function to run the expense analysis program.
    """
    expenses = get_expenses()
    if not expenses:
        print("No valid expenses entered. Exiting program.")
        return
    total, highest, lowest = analyze_expenses(expenses)
    display_results(total, highest, lowest)


if __name__ == "__main__":
    main()
