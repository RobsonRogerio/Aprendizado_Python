import pyautogui
from time import sleep

from funcoes_buscar_imagens import clica_na_imagem_netflix

def netflix_registro(email, senha, dados_cartao): #email, senha, dados_cartao
    #acesso ao navegador:
    clica_na_imagem_netflix('icone_chrome')
    sleep(1)
    #acesso ao modo visitante do chrome:
    clica_na_imagem_netflix('botao_modo_visitante_chrome')
    sleep(1)
    #abre nova guia anônima
    pyautogui.hotkey('ctrl', 'shift', 'n')
    sleep(2)
    #acessa barra de navegação/pesquisa
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('netflix', interval=0.10)
    pyautogui.press('space')
    pyautogui.press('enter')
    sleep(4)
    #acessa página netflix
    try:
        clica_na_imagem_netflix('icone_netflix')
    except:
        clica_na_imagem_netflix('icone_netflix_branco')
    sleep(4)
    #clica no campo de texto, apaga se houver algo preenchido
    clica_na_imagem_netflix('campo_email')
    sleep(2)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')
    pyautogui.write(email, interval=0.10)
    pyautogui.press('enter')
    sleep(2)
    #clica no botão próximo 1:
    clica_na_imagem_netflix('botao_proximo_1')
    sleep(2)
    #clica no campo senha para adicionar a senha:
    clica_na_imagem_netflix('campo_adicionar_senha')
    pyautogui.write(senha, interval=0.10)
    pyautogui.press('enter')
    sleep(2)
    #clicar no botão pular verificação de email:
    clica_na_imagem_netflix('botao_pular_verif_email')
    sleep(2)
    #scroll até o fim da página
    pyautogui.scroll(-100)
    #clicar no botão próximo na tela escolha seu plano:
    clica_na_imagem_netflix('botao_proximo_2')
    sleep(2)
    #escolha do plano:
    clica_na_imagem_netflix('botao_padrao_anuncios')
    sleep(1)
    #scroll até o fim da página:
    pyautogui.scroll(-900)
    #clica no botão próximo:
    clica_na_imagem_netflix('botao_proximo_3')
    sleep(2)
    #seleciona a forma de pagamento:
    clica_na_imagem_netflix('botao_forma_pagto_cc')
    sleep(2)
    #preenchimento das informações de pagamento
    clica_na_imagem_netflix('campo_num_cartao')
    pyautogui.write(dados_cartao['numero'], interval=0.10)
    sleep(1)

    clica_na_imagem_netflix('campo_data_validade_cc')
    pyautogui.write(dados_cartao['validade'], interval=0.10)
    sleep(1)

    clica_na_imagem_netflix('campo_cvv_cc')
    pyautogui.write(dados_cartao['cvv'], interval=0.10)
    sleep(1)
    
    clica_na_imagem_netflix('campo_nome_cc')
    pyautogui.write(dados_cartao['nome'], interval=0.10)
    sleep(1)

    #scroll até o fim da página
    pyautogui.scroll(-600)
    clica_na_imagem_netflix('botao_iniciar_assinatura')

    #fecha a janela do navegador
    sleep(10)
    pyautogui.hotkey('ctrl', 'w')

# DADOS_CARTAO = {'numero': '5544618169021780', 'validade': '01/28', 'cvv': '111', 'nome': 'NOME', 'sobrenome': 'SOBRENOME'}

# netflix_registro('fulano_btv_@uol.com.br','456*+-#$',DADOS_CARTAO)
