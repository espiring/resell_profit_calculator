def calc_profit_and_cost(buy_price: int, sell_price: int, quantity: int) -> tuple:
    """Calculates profit and total cost based on purchase price, selling price, and quantity."""
    profit = (sell_price - buy_price) * quantity
    total_cost = buy_price * quantity
    return profit, total_cost

def get_user_input(prompt: str) -> int:
    """Fetches and returns an integer value from the user based on a prompt."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def display_results(profit: int, total_cost: int, quantity: int) -> None:
    """Displays profit and total cost formatted with thousands separator."""
    print(f"Profit: {profit:,.0f} SEK")
    print(f"Total cost for {quantity} units: {total_cost:,.0f} SEK")

def main():
    """Main function that runs the program."""
    buy_price = get_user_input("Enter purchase price: ")
    sell_price = get_user_input("Enter selling price: ")
    quantity = get_user_input("Enter quantity (units): ")
    
    profit, total_cost = calc_profit_and_cost(buy_price, sell_price, quantity)
    display_results(profit, total_cost, quantity)

if __name__ == "__main__":
    main()

