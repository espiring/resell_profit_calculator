import tkinter as tk
from tkinter import messagebox

def calc_profit():
    try:
        buy_price = int(entry_buy_price.get())
        sell_price = int(entry_sell_price.get())
        quantity = int(entry_quantity.get())
        
        profit = (sell_price - buy_price) * quantity
        total_cost = buy_price * quantity
        
        label_profit["text"] = f"Vinst: {profit:,.0f} kr"
        label_total_cost["text"] = f"Totalkostnad för {quantity} enheter: {total_cost:,.0f} kr"
    except ValueError:
        messagebox.showerror("Fel", "Vänligen ange giltiga numeriska värden!")

root = tk.Tk()
root.title("Vinst- och Kostnadsberäknare")
root.geometry("400x300")
root.configure(bg="#f0f0f5")  # Ljus bakgrundsfärg

#Rubrik
title = tk.Label(root, text="Beräkna Vinst och Totalkostnad", font=("Helvetica", 16, "bold"), bg="#f0f0f5", fg="#333333")
title.pack(pady=10)

# Inputfält och labels
frame = tk.Frame(root, bg="#f0f0f5")
frame.pack(pady=10)

# Labels och inputfält för inköpspris
label_buy_price = tk.Label(frame, text="Inköpspris:", font=("Helvetica", 12), bg="#f0f0f5", fg="#444444")
label_buy_price.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_buy_price = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry_buy_price.grid(row=0, column=1, padx=5, pady=5)

# Labels och inputfält för säljpris
label_sell_price = tk.Label(frame, text="Säljpris:", font=("Helvetica", 12), bg="#f0f0f5", fg="#444444")
label_sell_price.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_sell_price = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry_sell_price.grid(row=1, column=1, padx=5, pady=5)

# Etiketter och inmatningsfält för mängd
label_quantity = tk.Label(frame, text="Mängd (enheter):", font=("Helvetica", 12), bg="#f0f0f5", fg="#444444")
label_quantity.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_quantity = tk.Entry(frame, font=("Helvetica", 12), width=15)
entry_quantity.grid(row=2, column=1, padx=5, pady=5)

# Knapp för beräkning
calc_button = tk.Button(root, text="Beräkna", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=calc_profit)
calc_button.pack(pady=15)

# Resultatslabels
label_profit = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f5", fg="#333333")
label_profit.pack(pady=5)

label_total_cost = tk.Label(root, text=""

