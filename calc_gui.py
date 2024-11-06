import tkinter as tk
from tkinter import messagebox

# Calculation function
def calc_profit():
    try:
        # Get values from input fields
        buy_price = int(entry_buy_price.get())
        sell_price = int(entry_sell_price.get())
        quantity = int(entry_quantity.get())
        
        # Calculate profit and total cost
        profit = (sell_price - buy_price) * quantity
        total_cost = buy_price * quantity
        
        # Display the results with thousands separator
        label_profit["text"] = f"Profit: {profit:,.0f} SEK"
        label_total_cost["text"] = f"Total cost for {quantity} units: {total_cost:,.0f} SEK"
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values!")

# Create main window
root = tk.Tk()
root.title("Profit and Cost Calculator")
root.geometry("400x300")
root.configure(bg="#f0f0f5")  # Light background color

# Header
title = tk.Label(root, text="Calculate Profit and Total Cost", font=("Helvetica", 16, "bold"), bg="#f0f0f5", fg="#333333")
title.pack(pady=10)

# Input fields and labels
frame = tk.Frame(root, bg="#f0f0f5")
frame.pack(pady=10)

# Labels and input fields for purchase price
label_buy_price = tk.Label(frame, text="Purchase Price:", font=("Helvetica", 12), bg="#f0f0f5", fg="#444444")
label_buy_price.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_buy_price = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry_buy_price.grid(row=0, column=1, padx=5, pady=5)

# Labels and input fields for selling price
label_sell_price = tk.Label(frame, text="Selling Price:", font=("Helvetica", 12), bg="#f0f0f5", fg="#444444")
label_sell_price.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_sell_price = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry_sell_price.grid(row=1, column=1, padx=5, pady=5)

# Labels and input fields for quantity
label_quantity = tk.Label(frame, text="Quantity (units):", font=("Helvetica", 12), bg="#f0f0f5", fg="#444444")
label_quantity.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_quantity = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry_quantity.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=calc_profit)
calc_button.pack(pady=15)

# Result labels
label_profit = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f5", fg="#333333")
label_profit.pack(pady=5)

label_total_cost = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f5", fg="#333333")
label_total_cost.pack(pady=5)

# Run the program
root.mainloop()

