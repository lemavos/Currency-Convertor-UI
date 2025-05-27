import requests
from tkinter import *
import currencies

def open_currencies():
    currencies.open_root()
    
def convert():
    try:
        # Obter os valores dos campos de entrada
        currency1_value = currency1.get().strip().upper()
        currency2_value = currency2.get().strip().upper()
        qtd_converting_value = qtd_converting.get().strip()
        
        # Validação de entrada
        if not currency1_value or not currency2_value:
            Label(root, text="", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=260, width=400, height=60)
            Label(root, text="Error: Please fill in both currencies.", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=120, y=260, width=400, height=20)
            return
        if not qtd_converting_value.isdigit() or float(qtd_converting_value) <= 0:
            Label(root, text="", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=260, width=400, height=60)
            Label(root, text="Error: Please enter a valid amount greater than 0.", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=120, y=260, width=400, height=20)
            return
        
        qtd_converting_value = float(qtd_converting_value)
        
        # API para obter os dados de conversão
        API = f"https://economia.awesomeAPI.com.br/json/last/{currency1_value}-{currency2_value}"
        API_response = requests.get(API)
        data = API_response.json()
        
        currencies_converting = currency1_value + currency2_value
        if currencies_converting not in data:
            Label(root, text="", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=260, width=400, height=60)
            Label(root, text="Error: That currency does not exist or was not found.", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=120, y=260, width=400, height=20)
            return
        
        # Realizar a conversão
        currency_convert = float(data[currencies_converting]["bid"])
        qtd_converted = currency_convert * qtd_converting_value
        
        # Exibir o resultado
        Label(root, text=f"", background="white", foreground="green", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=260, width=1000, height=70)
        Label(root, text=f"One {currency1_value} is equal to {currency_convert:.2f} {currency2_value}.", background="white", foreground="green", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=260, width=400, height=20)
        Label(root, text=f"{qtd_converting_value} {currency1_value} is equal to {qtd_converted:.2f} {currency2_value}.", background="white", foreground="green", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=280, width=400, height=20)
    
    except Exception as e:
        Label(root, text=f"", background="white", font=("Arial", 10, "bold")).place(x=140, y=260, width=400, height=60)
        Label(root, text=f"Unexpected error: {e}", background="white", foreground="red", anchor="w", font=("Arial", 10, "bold")).place(x=140, y=260, width=400, height=20)

root = Tk()
root.title("Currency Converter")
root.geometry("450x350")
root.configure(background="white")
root.resizable(False, False)  # trava o redimensionamento da janela

# apresentacao do app
Label(root, text="Welcome to the currency convertor.",background="white",foreground="black",anchor="w", font=("Arial", 12, "bold")).place(x=10,y=10,width=430,height=20)

# entry para o usuario informar a moeda desejada
Label(root, text="Entry currency 1:",background="white",foreground="black",anchor="w", font=("Arial", 10, "bold")).place(x=10,y=50,width=120,height=20)
currency1 = Entry(root)
currency1.place(x=140,y=50,width=60,height=20)

# entry para o usuario informar a moeda desejada
Label(root, text="Entry currency 2:",background="white",foreground="black",anchor="w", font=("Arial", 10, "bold")).place(x=10,y=90,width=120,height=20)
currency2 = Entry(root)
currency2.place(x=140,y=90,width=60,height=20)

# entry que fala quanto dinheiro esta sendo convertido
Label(root, text="Type how much Currency 1 you want convert:",background="white",foreground="black",anchor="w", font=("Arial", 10, "bold")).place(x=10,y=130,width=280,height=20)
qtd_converting = Entry(root)
qtd_converting.place(x=300,y=130,width=80,height=20)

# botao para abrir as opcoes de moedas
Button(root,text="See currencies",command=open_currencies, font=("Arial", 10, "bold")).place(x=170,y=180,width=110,height=25)

# botao para converter a moeda
Button(root,text="Convert",command=convert, font=("Arial", 10, "bold")).place(x=190,y=215,width=70,height=25)

root.mainloop()
