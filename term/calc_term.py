import os
import sys
import time
from colorama import init, Fore, Back, Style

# Add parent directory to sys.path to allow imports from higher levels
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize colorama
init(autoreset=True)

# ASCII Art Title (for a cool header)
def print_title():
    title = """
$$$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|\_$$  _|\__$$  __|
$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ |        $$ |     $$ |   
$$$$$$$  |$$$$$$$  |$$ |  $$ |$$$$$\      $$ |     $$ |   
$$  ____/ $$  __$$< $$ |  $$ |$$  __|     $$ |     $$ |   
$$ |      $$ |  $$ |$$ |  $$ |$$ |        $$ |     $$ |   
$$ |      $$ |  $$ | $$$$$$  |$$ |      $$$$$$\    $$ |   
\__|      \__|  \__| \______/ \__|      \______|   \__|   
"""

    print(Fore.MAGENTA + Style.BRIGHT + title)

# Calculation function
def calc_profit_and_cost(buy_price: int, sell_price: int, quantity: int) -> tuple:
    """Calculates profit and total cost based on purchase price, selling price, and quantity."""
    profit = (sell_price - buy_price) * quantity
    total_cost = buy_price * quantity
    return profit, total_cost

def get_user_input(prompt: str) -> int:
    """Fetches and returns an integer value from the user based on a prompt."""
    while True:
        try:
            user_input = input(Fore.CYAN + prompt)
            # Handle input as integer
            return int(user_input)
        except ValueError:
            print(Fore.RED + "Error: Please enter a valid integer.")

def display_results(profit: int, total_cost: int, quantity: int) -> None:
    """Displays profit and total cost formatted with thousands separator."""
    print(Fore.GREEN + "\n" + Style.BRIGHT + "╔══════════════════════════════════════╗")
    print(Fore.GREEN + "║" + Fore.YELLOW + Style.BRIGHT + f" Profit: {profit:,.0f} SEK " + "║")
    print(Fore.GREEN + "║" + Fore.YELLOW + Style.BRIGHT + f" Total cost for {quantity:,.0f} units: {total_cost:,.0f} SEK " + "║")
    print(Fore.GREEN + "╚══════════════════════════════════════╝")

def show_loading_message():
    """Displays a loading message with animation."""
    loading_message = "Calculating"
    for _ in range(4):
        print(Fore.MAGENTA + loading_message + "." * (_ + 1), end="\r")
        time.sleep(0.5)
    print(Fore.MAGENTA + "Calculation complete!      ")

def clear_screen():
    """Clears the terminal screen for a fresh view between stages."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_transition():
    """Displays a smooth transition effect between sections."""
    print(Fore.CYAN + "\n" + "-"*40 + "\n")

def main():
    """Main function that runs the program."""
    clear_screen()
    print_title()
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Profit and Cost Calculator!\n")
    print(Fore.CYAN + "---------------------------------------------\n")

    # Get inputs from the user
    buy_price = get_user_input("Enter purchase price: ")
    print_transition()
    sell_price = get_user_input("Enter selling price: ")
    print_transition()
    quantity = get_user_input("Enter quantity (units): ")
    print_transition()

    # Show loading message
    show_loading_message()

    # Clear screen and display results
    clear_screen()
    display_results(calc_profit_and_cost(buy_price, sell_price, quantity)[0],
                   calc_profit_and_cost(buy_price, sell_price, quantity)[1],
                   quantity)

    # Keep the program running until the user decides to exit
    input(Fore.CYAN + "\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        input(Fore.CYAN + "\nPress Enter to exit...")

