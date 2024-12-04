import tkinter as tk
from tkinter import ttk

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        
        # Current hard-coded exchange rates (as of the latest known values)
        exchange_rates = {
            'USD': 1.0,       # Base currency
            'EUR': 0.92,      # 1 USD = 0.92 EUR
            'INR': 84.72,     # 1 USD = 83.00 INR
            'GBP': 0.78       # 1 USD = 0.78 GBP
        }
        
        if from_currency in exchange_rates and to_currency in exchange_rates:
            # Convert amount from the source currency to USD first, then to the target currency
            amount_in_usd = amount / exchange_rates[from_currency]
            converted_amount = amount_in_usd * exchange_rates[to_currency]
            result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            result_var.set("Currency not supported.")
    except ValueError:
        result_var.set("Invalid amount entered.")

# Tkinter setup
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x300")

# GUI Components
entry_amount = tk.Entry(window)
entry_amount.pack(pady=10)

from_currency_var = tk.StringVar(window)
from_currency_var.set("USD")
to_currency_var = tk.StringVar(window)
to_currency_var.set("EUR")

from_currency_menu = ttk.Combobox(window, textvariable=from_currency_var, values=['USD', 'EUR', 'INR', 'GBP'])
from_currency_menu.pack(pady=10)

to_currency_menu = ttk.Combobox(window, textvariable=to_currency_var, values=['USD', 'EUR', 'INR', 'GBP'])
to_currency_menu.pack(pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

result_var = tk.StringVar(window)
result_label = tk.Label(window, textvariable=result_var)
result_label.pack(pady=20)

window.mainloop()
