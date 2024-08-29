def calculate_total_rent(monthly_rent, number_of_months, additional_costs=0):
    """
    Calculate the total rent amount including additional costs.

    Parameters:
    monthly_rent (float): The rent amount per month.
    number_of_months (int): Number of months the rent is calculated for.
    additional_costs (float): Any additional costs to be added to the total rent.

    Returns:
    float: The total rent amount.
    """
    total_rent = monthly_rent * number_of_months
    total_rent += additional_costs
    return total_rent

def main():
    try:
        monthly_rent = float(input("Enter the monthly rent amount ($): "))
        number_of_months = int(input("Enter the number of months: "))
        additional_costs = float(input("Enter any additional costs ($), if none enter 0: "))
        total_rent = calculate_total_rent(monthly_rent, number_of_months, additional_costs)
        print(f"\nThe total rent for {number_of_months} months is: ${total_rent:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
