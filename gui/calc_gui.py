import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import sys

# Add the parent directory (root of the project) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import 'utils'
from utils.calc_utils import calc_profit_and_cost, format_currency

# Path to the history and settings files
HISTORY_FILE = "history.json"
SETTINGS_FILE = "settings.json"

# Global variable to store history
history = []

# Load settings from a JSON file
def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r") as file:
                data = json.load(file)
                return data
        except (json.JSONDecodeError, IOError):
            pass
    # Default settings if no settings file is found
    return {"theme": "light", "font_size": 12, "history_limit": 7}

# Save settings to a JSON file
def save_settings(settings):
    try:
        with open(SETTINGS_FILE, "w") as file:
            json.dump(settings, file)
    except Exception as e:
        print(f"Error saving settings: {e}")

# Load history from a JSON file
def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as file:
                data = json.load(file)
                if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                    return data
        except (json.JSONDecodeError, IOError):
            pass
    return []  # Return an empty list if file is missing or invalid

# Save history to a JSON file
def save_history():
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file)
    except Exception as e:
        print(f"Error saving history: {e}")

def calc_profit():
    try:
        # Get values from input fields
        buy_price = int(entry_buy_price.get())
        sell_price = int(entry_sell_price.get())
        quantity = int(entry_quantity.get())
        
        # Calculate profit and total cost
        profit, total_cost = calc_profit_and_cost(buy_price, sell_price, quantity)
        
        # Display the results
        label_profit_value["text"] = format_currency(profit)
        label_total_cost_value["text"] = format_currency(total_cost)
        
        # Add the calculation to history
        result = {
            "buy_price": buy_price,
            "sell_price": sell_price,
            "quantity": quantity,
            "profit": profit,
            "total_cost": total_cost
        }
        history.append(result)
        if len(history) > settings["history_limit"]:  # Keep history within the limit
            history.pop(0)
        
        # Update history tab
        update_history_tab()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values!")

def update_history_tab():
    """Update the history Treeview with the latest data."""
    # Clear the history treeview
    for row in history_tree.get_children():
        history_tree.delete(row)

    # Populate the treeview with the latest history
    for i, record in enumerate(history, start=1):
        history_tree.insert(
            "", "end", values=(
                i,
                record["buy_price"],
                record["sell_price"],
                record["quantity"],
                format_currency(record["profit"]),
                format_currency(record["total_cost"]),
                "Select"
            )
        )

def on_select_item(event):
    """Handle the selection of a history item."""
    selected_item = history_tree.selection()
    if selected_item:
        # Highlight the selected row by changing its background color
        history_tree.tag_configure('selected', background='#D3D3D3')  # Light gray color
        history_tree.item(selected_item, tags='selected')
        selected_row = history_tree.item(selected_item)
        selected_index = int(selected_row['values'][0]) - 1  # Get the row index (start from 0)
        return selected_index
    return None

def on_delete_button_click():
    """Handle the delete button click event."""
    selected_index = on_select_item(None)
    if selected_index is not None:
        delete_history_item(selected_index)

def delete_history_item(item_index):
    """Delete a specific item from history and update the view."""
    try:
        del history[item_index]
        save_history()
        update_history_tab()
    except IndexError:
        messagebox.showerror("Error", "Invalid history item.")

def delete_all_history():
    """Clear all history and update the view."""
    global history
    history = []
    save_history()
    update_history_tab()

def on_close():
    """Save history and close the application."""
    save_history()
    save_settings(settings)
    root.destroy()

def format_currency(value):
    """Format the currency with appropriate symbols and negative values."""
    if value < 0:
        return f"-${abs(value):,.2f}"
    return f"${value:,.2f}"

def apply_settings():
    """Apply settings such as theme and font size."""
    if settings["theme"] == "dark":
        root.configure(bg="#333")
        for widget in root.winfo_children():
            widget.configure(bg="#333", fg="#fff")
    else:
        root.configure(bg="#f0f4f8")
        for widget in root.winfo_children():
            widget.configure(bg="#f0f4f8", fg="#000")
    
    # Update font size
    font = ("Helvetica", settings["font_size"])
    title.configure(font=("Helvetica", settings["font_size"], "bold"))
    label_profit.configure(font=font)
    label_total_cost.configure(font=font)
    calc_button.configure(font=font)
    remove_button.configure(font=font)
    delete_all_button.configure(font=font)

# Load settings and history
settings = load_settings()
history = load_history()

# Create main window
root = tk.Tk()
root.title("Profit and Cost Calculator")
root.geometry("700x500")

# Header
title = ttk.Label(root, text="Profit and Cost Calculator", font=("Helvetica", settings["font_size"], "bold"))
title.pack(pady=10)

# Apply settings after the title is created
apply_settings()

# Style configuration
style = ttk.Style()
style.configure("TNotebook", background="#f0f4f8", padding=5)
style.configure("TNotebook.Tab", font=("Helvetica", 12), padding=[10, 5])
style.configure("TFrame", background="#f0f4f8")
style.configure("TLabel", background="#f0f4f8", font=("Helvetica", settings["font_size"]))
style.configure("TButton", font=("Helvetica", settings["font_size"]), padding=5)
style.configure("Treeview", font=("Helvetica", settings["font_size"]), rowheight=25)
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
style.map("TButton", background=[("active", "#4CAF50")], foreground=[("active", "white")])

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tab 1: Calculator
tab_calculator = ttk.Frame(notebook)
notebook.add(tab_calculator, text="Calculator")

# Input frame
frame_inputs = ttk.Frame(tab_calculator, padding=10)
frame_inputs.pack(pady=10)

label_buy_price = ttk.Label(frame_inputs, text="Purchase Price:")
label_buy_price.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_buy_price = ttk.Entry(frame_inputs, font=("Helvetica", settings["font_size"]), width=15)
entry_buy_price.grid(row=0, column=1, padx=5, pady=5)

label_sell_price = ttk.Label(frame_inputs, text="Selling Price:")
label_sell_price.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_sell_price = ttk.Entry(frame_inputs, font=("Helvetica", settings["font_size"]), width=15)
entry_sell_price.grid(row=1, column=1, padx=5, pady=5)

label_quantity = ttk.Label(frame_inputs, text="Quantity (units):")
label_quantity.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_quantity = ttk.Entry(frame_inputs, font=("Helvetica", settings["font_size"]), width=15)
entry_quantity.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
calc_button = ttk.Button(tab_calculator, text="Calculate", command=calc_profit)
calc_button.pack(pady=15)

# Results frame
frame_results = ttk.Frame(tab_calculator, padding=10)
frame_results.pack(pady=10)

label_profit = ttk.Label(frame_results, text="Profit:")
label_profit.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_profit_value = ttk.Label(frame_results, text="N/A", font=("Helvetica", settings["font_size"], "bold"), foreground="#4CAF50")
label

