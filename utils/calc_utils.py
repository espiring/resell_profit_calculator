# utils/calc_utils.py
def calc_profit_and_cost(buy_price: int, sell_price: int, quantity: int) -> tuple:
    """Calculates profit and total cost based on purchase price, selling price, and quantity."""
    profit = (sell_price - buy_price) * quantity
    total_cost = buy_price * quantity
    return profit, total_cost

def format_currency(value: int) -> str:
    """Formats the given integer value with thousands separators and adds SEK."""
    return f"{value:,.0f} SEK"

