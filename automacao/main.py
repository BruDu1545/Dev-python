# Passo 1: Acessar o sitema da empresa Link:(https://dlp.hashtagtreinamentos.com/python/intensivao/login)
# Passo 2: Fazer o login 
# Passo 3: Importar a base de dados dos produtos
# Passo 4: cadastrar produto
# Passo 5: Repetir o processo com todos os dados

import pandas 
# pandas.read_csv -> le a base de dados em formato csv

import time
import pyautogui
# pyautogui.click -> clicar
# pyautogui.press -> pressionar tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado
# pyautogui.PAUSE -> define o intervalo das funcoes

pyautogui.PAUSE = 0.5

# Passo 1: Acessar o sitema da empresa Link:(https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Acessa a página do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera o carregamento da pagina
time.sleep(5)

# Passo 2: Fazer o login 
pyautogui.click(x=465, y=375)
pyautogui.write("brunocarletto@gmail.com")

pyautogui.press("tab")
pyautogui.write("bruno123")

pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
table_csv = pandas.read_csv("produtos.csv")

time.sleep(3)

# Passo 4: cadastrar produto e Passo 5: repetir isso com todos os registros

for row in table_csv.index:
    pyautogui.click(x=425, y=264)

    # codigo
    codigo = table_csv.loc[row, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = table_csv.loc[row, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = table_csv.loc[row, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = table_csv.loc[row, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_un
    preco_unitario = table_csv.loc[row, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = table_csv.loc[row, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(table_csv.loc[row, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    # cadastrar
    pyautogui.press("enter")
    pyautogui.scroll(10000)


