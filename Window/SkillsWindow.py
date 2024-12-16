import tkinter as tk
from tkinter import ttk
import json
import os


def get_skills():
    def submit():
        # Salvar os valores preenchidos
        for skill, entry in entriesBasic.items():
            basicSkills[skill] = entry.get() or "0"
        for skill, entry in entriesAdvanced.items():
            advancedSkills[skill] = entry.get() or "0"
        for skill, entry in entriesExpert.items():
            expertSkills[skill] = entry.get() or "0"

        # Salva os skills no arquivo JSON
        with open("Arquivos/skills.json", "w") as f:
            json.dump({
                "basic": basicSkills,
                "advanced": advancedSkills,
                "expert": expertSkills
            }, f)

        root.destroy()

    # Carregar lista de skills do arquivo
    skills_list_file = "Arquivos/Skillslist.txt"
    if not os.path.exists(skills_list_file):
        raise FileNotFoundError(
            f"O arquivo {skills_list_file} não foi encontrado.")

    with open(skills_list_file, "r") as f:
        SkillsList = [line.strip() for line in f if line.strip()]

    # Carregar habilidades anteriores, se existirem
    skills_file = "Arquivos/skills.json"
    if os.path.exists(skills_file):
        try:
            with open(skills_file, "r") as f:
                saved_skills = json.load(f)
        except json.JSONDecodeError:
            # Inicializa com valores padrão se o arquivo estiver vazio ou inválido
            saved_skills = {"basic": {}, "advanced": {}, "expert": {}}
    else:
        saved_skills = {"basic": {}, "advanced": {}, "expert": {}}

    root = tk.Tk()
    root.title("Defina os níveis de habilidades: Básico, Avançado e Expert")

    # Cria um canvas com barra de rolagem
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.grid(row=0, column=0, sticky="nsew")

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    entriesBasic = {}
    entriesAdvanced = {}
    entriesExpert = {}
    basicSkills = {}
    advancedSkills = {}
    expertSkills = {}

    # Adiciona rótulos para as colunas
    header_skill = ttk.Label(frame, text="Skill", font=("Arial", 10, "bold"))
    header_skill.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    header_basic = ttk.Label(frame, text="Basic", font=("Arial", 10, "bold"))
    header_basic.grid(row=0, column=1, padx=5, pady=5)

    header_advanced = ttk.Label(
        frame, text="Advanced", font=("Arial", 10, "bold"))
    header_advanced.grid(row=0, column=2, padx=5, pady=5)

    header_expert = ttk.Label(frame, text="Expert", font=("Arial", 10, "bold"))
    header_expert.grid(row=0, column=3, padx=5, pady=5)

    # Adiciona rótulos e entradas
    for i, skill in enumerate(SkillsList, start=1):
        label = ttk.Label(frame, text=skill)
        label.grid(row=i, column=0, sticky="w", padx=5, pady=2)

        entryBasic = ttk.Entry(frame, width=10)
        entryBasic.insert(0, saved_skills.get("basic", {}).get(skill, "0"))
        entryBasic.grid(row=i, column=1, padx=5, pady=2)
        entriesBasic[skill] = entryBasic

        entryAdvanced = ttk.Entry(frame, width=10)
        entryAdvanced.insert(0, saved_skills.get(
            "advanced", {}).get(skill, "0"))
        entryAdvanced.grid(row=i, column=2, padx=5, pady=2)
        entriesAdvanced[skill] = entryAdvanced

        entryExpert = ttk.Entry(frame, width=10)
        entryExpert.insert(0, saved_skills.get("expert", {}).get(skill, "0"))
        entryExpert.grid(row=i, column=3, padx=5, pady=2)
        entriesExpert[skill] = entryExpert

    # Botão de envio
    submit_button = ttk.Button(frame, text="Save", command=submit)
    submit_button.grid(row=len(SkillsList) + 1,
                       column=0, columnspan=4, pady=10)

    # Atualiza o canvas quando o frame for redimensionado
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", update_scroll_region)

    root.mainloop()
    return basicSkills, advancedSkills, expertSkills


if __name__ == "__main__":
    basicSkills, advancedSkills, expertSkills = get_skills()
    print("Basic Skills:", basicSkills)
    print("Advanced Skills:", advancedSkills)
    print("Expert Skills:", expertSkills)
