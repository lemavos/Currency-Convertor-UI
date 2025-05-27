import tkinter as tk

# Currency data with countries
currencies = {
    "AED": {"name": "United Arab Emirates Dirham", "country": "United Arab Emirates"},
    "AFN": {"name": "Afghan Afghani", "country": "Afghanistan"},
    "ALL": {"name": "Albanian Lek", "country": "Albania"},
    "AMD": {"name": "Armenian Dram", "country": "Armenia"},
    "ANG": {"name": "Netherlands Antillean Guilder", "country": "Netherlands Antilles"},
    "AOA": {"name": "Angolan Kwanza", "country": "Angola"},
    "ARS": {"name": "Argentine Peso", "country": "Argentina"},
    "AUD": {"name": "Australian Dollar", "country": "Australia"},
    "AZN": {"name": "Azerbaijani Manat", "country": "Azerbaijan"},
    "BAM": {"name": "Bosnia-Herzegovina Convertible Mark", "country": "Bosnia and Herzegovina"},
    "BBD": {"name": "Barbadian Dollar", "country": "Barbados"},
    "BDT": {"name": "Bangladeshi Taka", "country": "Bangladesh"},
    "BGN": {"name": "Bulgarian Lev", "country": "Bulgaria"},
    "BHD": {"name": "Bahraini Dinar", "country": "Bahrain"},
    "BIF": {"name": "Burundian Franc", "country": "Burundi"},
    "BND": {"name": "Brunei Dollar", "country": "Brunei"},
    "BOB": {"name": "Bolivian Boliviano", "country": "Bolivia"},
    "BRL": {"name": "Brazilian Real", "country": "Brazil"},
    "BRLT": {"name": "Brazilian Real Tourism", "country": "Brazil"},
    "BSD": {"name": "Bahamian Dollar", "country": "Bahamas"},
    "BTC": {"name": "Bitcoin", "country": "Global"},
    "BWP": {"name": "Botswana Pula", "country": "Botswana"},
    "BYN": {"name": "Belarusian Ruble", "country": "Belarus"},
    "BZD": {"name": "Belize Dollar", "country": "Belize"},
    "CAD": {"name": "Canadian Dollar", "country": "Canada"},
    "CHF": {"name": "Swiss Franc", "country": "Switzerland"},
    "CLP": {"name": "Chilean Peso", "country": "Chile"},
    "CNH": {"name": "Chinese Yuan Offshore", "country": "China"},
    "CNY": {"name": "Chinese Yuan", "country": "China"},
    "COP": {"name": "Colombian Peso", "country": "Colombia"},
    "CRC": {"name": "Costa Rican Colón", "country": "Costa Rica"},
    "CUP": {"name": "Cuban Peso", "country": "Cuba"},
    "CVE": {"name": "Cape Verdean Escudo", "country": "Cape Verde"},
    "CZK": {"name": "Czech Koruna", "country": "Czech Republic"},
    "DJF": {"name": "Djiboutian Franc", "country": "Djibouti"},
    "DKK": {"name": "Danish Krone", "country": "Denmark"},
    "DOGE": {"name": "Dogecoin", "country": "Global"},
    "DOP": {"name": "Dominican Peso", "country": "Dominican Republic"},
    "DZD": {"name": "Algerian Dinar", "country": "Algeria"},
    "EGP": {"name": "Egyptian Pound", "country": "Egypt"},
    "ETB": {"name": "Ethiopian Birr", "country": "Ethiopia"},
    "ETH": {"name": "Ethereum", "country": "Global"},
    "EUR": {"name": "Euro", "country": "European Union"},
    "FJD": {"name": "Fijian Dollar", "country": "Fiji"},
    "GBP": {"name": "British Pound Sterling", "country": "United Kingdom"},
    "GEL": {"name": "Georgian Lari", "country": "Georgia"},
    "GHS": {"name": "Ghanaian Cedi", "country": "Ghana"},
    "GMD": {"name": "Gambian Dalasi", "country": "Gambia"},
    "GNF": {"name": "Guinean Franc", "country": "Guinea"},
    "GTQ": {"name": "Guatemalan Quetzal", "country": "Guatemala"},
    "HKD": {"name": "Hong Kong Dollar", "country": "Hong Kong"},
    "HNL": {"name": "Honduran Lempira", "country": "Honduras"},
    "HRK": {"name": "Croatian Kuna", "country": "Croatia"},
    "HTG": {"name": "Haitian Gourde", "country": "Haiti"},
    "HUF": {"name": "Hungarian Forint", "country": "Hungary"},
    "IDR": {"name": "Indonesian Rupiah", "country": "Indonesia"},
    "ILS": {"name": "Israeli New Shekel", "country": "Israel"},
    "INR": {"name": "Indian Rupee", "country": "India"},
    "IQD": {"name": "Iraqi Dinar", "country": "Iraq"},
    "IRR": {"name": "Iranian Rial", "country": "Iran"},
    "ISK": {"name": "Icelandic Krona", "country": "Iceland"},
    "JMD": {"name": "Jamaican Dollar", "country": "Jamaica"},
    "JOD": {"name": "Jordanian Dinar", "country": "Jordan"},
    "JPY": {"name": "Japanese Yen", "country": "Japan"},
    "KES": {"name": "Kenyan Shilling", "country": "Kenya"},
    "KGS": {"name": "Kyrgyzstani Som", "country": "Kyrgyzstan"},
    "KHR": {"name": "Cambodian Riel", "country": "Cambodia"},
    "KMF": {"name": "Comorian Franc", "country": "Comoros"},
    "KRW": {"name": "South Korean Won", "country": "South Korea"},
    "KWD": {"name": "Kuwaiti Dinar", "country": "Kuwait"},
    "KYD": {"name": "Cayman Islands Dollar", "country": "Cayman Islands"},
    "KZT": {"name": "Kazakhstani Tenge", "country": "Kazakhstan"},
    "LAK": {"name": "Lao Kip", "country": "Laos"},
    "LBP": {"name": "Lebanese Pound", "country": "Lebanon"},
    "LKR": {"name": "Sri Lankan Rupee", "country": "Sri Lanka"},
    "LSL": {"name": "Lesotho Loti", "country": "Lesotho"},
    "LTC": {"name": "Litecoin", "country": "Global"},
    "LYD": {"name": "Libyan Dinar", "country": "Libya"},
    "MAD": {"name": "Moroccan Dirham", "country": "Morocco"},
    # ...remaining currencies...
}

# Create the main window
def open_root():
    root = tk.Tk()
    root.title("Currencies and Countries")
    root.configure(background="white")
    root.resizable(False, False)
    
    # Add a Listbox to display currencies and countries
    listbox = tk.Listbox(root, width=60, height=20, background="white", foreground="black", font=("Arial", 11, "bold"))
    listbox.pack(padx=10, pady=10)

    # Populate the Listbox with currency codes, names, and countries
    for code, details in currencies.items():
        listbox.insert(tk.END, f"{code}: {details['name']} ({details['country']})")

    # Start the tkinter main loop
    root.mainloop()
