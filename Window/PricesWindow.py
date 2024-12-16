import tkinter as tk
from tkinter import ttk
import json
import os


def get_prices():
    def submit():
        # Salvar os valores preenchidos
        for item, entry in entriesBuy.items():
            buyPrices[item] = entry.get() or "0"
        for item, entry in entriesSell.items():
            sellPrices[item] = entry.get() or "0"
        for item, entry in entriesJita.items():
            jitaPrices[item] = entry.get() or "0"

        # Salva os preços no arquivo JSON
        with open("Arquivos\prices.json", "w") as f:
            json.dump({
                "buy": buyPrices,
                "sell": sellPrices,
                "jita": jitaPrices
            }, f)

        root.destroy()

    # Carregar lista de itens do arquivo
    industry_items_file = "Arquivos\IndustryItems.txt"
    if not os.path.exists(industry_items_file):
        raise FileNotFoundError(
            f"O arquivo {industry_items_file} não foi encontrado.")

    with open(industry_items_file, "r") as f:
        IndustryItems = [line.strip() for line in f if line.strip()]

    # Carregar preços anteriores, se existirem
    prices_file = "Arquivos\prices.json"
    if os.path.exists(prices_file):
        with open(prices_file, "r") as f:
            saved_prices = json.load(f)
    else:
        saved_prices = {"buy": {}, "sell": {}, "jita": {}}

    root = tk.Tk()
    root.title("Defina os preços de Compra, Venda e Jita")

    # Cria um canvas com barra de rolagem
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    entriesBuy = {}
    entriesSell = {}
    entriesJita = {}
    buyPrices = {}
    sellPrices = {}
    jitaPrices = {}

    # Adiciona rótulos para as colunas
    header_item = ttk.Label(frame, text="Item", font=("Arial", 10, "bold"))
    header_item.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    header_buy = ttk.Label(frame, text="Buy Prices",
                           font=("Arial", 10, "bold"))
    header_buy.grid(row=0, column=1, padx=5, pady=5)

    header_sell = ttk.Label(frame, text="Sell Prices",
                            font=("Arial", 10, "bold"))
    header_sell.grid(row=0, column=2, padx=5, pady=5)

    header_jita = ttk.Label(frame, text="Jita Prices",
                            font=("Arial", 10, "bold"))
    header_jita.grid(row=0, column=3, padx=5, pady=5)

    # Adiciona rótulos e entradas
    for i, item in enumerate(IndustryItems, start=1):
        label = ttk.Label(frame, text=item)
        label.grid(row=i, column=0, sticky="w", padx=5, pady=2)

        entryBuy = ttk.Entry(frame, width=10)
        entryBuy.insert(0, saved_prices.get("buy", {}).get(item, "0"))
        entryBuy.grid(row=i, column=1, padx=5, pady=2)
        entriesBuy[item] = entryBuy

        entrySell = ttk.Entry(frame, width=10)
        entrySell.insert(0, saved_prices.get("sell", {}).get(item, "0"))
        entrySell.grid(row=i, column=2, padx=5, pady=2)
        entriesSell[item] = entrySell

        entryJita = ttk.Entry(frame, width=10)
        entryJita.insert(0, saved_prices.get("jita", {}).get(item, "0"))
        entryJita.grid(row=i, column=3, padx=5, pady=2)
        entriesJita[item] = entryJita

    # Botão de envio
    submit_button = ttk.Button(frame, text="Save", command=submit)
    submit_button.grid(row=len(IndustryItems) + 1,
                       column=0, columnspan=4, pady=10)

    # Atualiza o canvas quando o frame for redimensionado
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", update_scroll_region)

    root.mainloop()
    return buyPrices, sellPrices, jitaPrices


if __name__ == "__main__":
    buyPrices, sellPrices, jitaPrices = get_prices()
    print("Buy Prices:", buyPrices)
    print("Sell Prices:", sellPrices)
    print("Jita Prices:", jitaPrices)
