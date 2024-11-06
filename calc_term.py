# term/calc_term.py
from utils.calc_utils import calc_profit_and_cost, format_currency

def get_user_input(prompt: str) -> int:
    """Fetches and returns an integer value from the user based on a prompt."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def display_results(profit: int, total_cost: int, quantity: int) -> None:
    """Displays profit and total cost formatted with thousands separator."""
    print(f"Profit: {format_currency(profit)}")
    print(f"Total cost for {quantity} units: {format_currency(total_cost)}")

def main():
    """Main function that runs the program."""
    buy_price = get_user_input("Enter purchase price: ")
    sell_price = get_user_input("Enter selling price: ")
    quantity = get_user_input("Enter quantity (units): ")
    
    profit, total_cost = calc_profit_and_cost(buy_price, sell_price, quantity)
    display_results(profit, total_cost, quantity)

if __name__ == "__main__":
    main()

