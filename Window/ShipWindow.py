import json
import tkinter as tk
from tkinter import ttk

# Carregar JSON de um arquivo
with open('Arquivos/item_en.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

# Parse do JSON
data = json.loads(json_data)

# Extraindo os nomes


def extract_names(data):
    names = []
    for key, value in data.items():
        names.append(value.get("en_name", "Unknown"))  # Usa o campo "en_name"
    return names


names_list = extract_names(data)

# Função para atualizar a lista no Combobox conforme a digitação


def update_list(event):
    typed_text = combo_box.get().lower()
    if typed_text == "":
        combo_box["values"] = names_list  # Restaura a lista completa
    else:
        filtered_names = [
            name for name in names_list if typed_text in name.lower()]
        combo_box["values"] = filtered_names
    combo_box.event_generate("<Down>")  # Abre o dropdown automaticamente

# Função para exibir o nome selecionado


def show_selected_name():
    selected_name = combo_box.get()
    label_selected.config(text=f"Selecionado: {selected_name}")


# Criando a janela principal
root = tk.Tk()
root.title("Selecionar Nome")
root.geometry("300x200")

# Combobox para exibir os nomes
label_prompt = tk.Label(root, text="Selecione um nome:")
label_prompt.pack(pady=10)

combo_box = ttk.Combobox(root, values=names_list, state="normal")
combo_box.pack(pady=5)
combo_box.bind("<KeyRelease>", update_list)  # Atualiza lista enquanto digita

# Botão para confirmar a seleção
button_select = tk.Button(root, text="Confirmar", command=show_selected_name)
button_select.pack(pady=10)

# Rótulo para mostrar o nome selecionado
label_selected = tk.Label(root, text="Selecionado: None")
label_selected.pack(pady=10)

# Inicia o loop da interface


def run_app():
    root.mainloop()


if __name__ == "__main__":
    run_app()
