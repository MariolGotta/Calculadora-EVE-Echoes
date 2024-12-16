from tkinter import *
import subprocess


def PricesWindow():
    subprocess.Popen(["Python", "Window\\PricesWindow.py"])


def SkillsWindow():
    subprocess.Popen(["Python", "Window\\SkillsWindow.py"])


def ShipWindow():
    subprocess.Popen(["Python", "Window\\ShipWindow.py"])


janelaPrincipal = Tk()

janelaPrincipal.title("Calculadora Industrial - FLBR")


boas_vindas = Label(

    janelaPrincipal, text="Bem Vindo à aplicação destinada ao jogo EVE Echoes da Corporação FLBR \n" +

    "Esta calculadora é destianda ao Cálculo de valores de naves e itens")

boas_vindas.grid(column=0, row=0)


botao = Button(janelaPrincipal, text="Calculadora de Nave",
               command=ShipWindow)

botao.grid(column=0, row=1)

botao = Button(janelaPrincipal, text="Quais planetas escolher?",
               command="")

botao.grid(column=0, row=2)

botao = Button(janelaPrincipal, text="Configurações de Skill",
               command=SkillsWindow)

botao.grid(column=0, row=3)

botao = Button(janelaPrincipal, text="Configurações de Preços",
               command=PricesWindow)

botao.grid(column=0, row=4)

janelaPrincipal.mainloop()
