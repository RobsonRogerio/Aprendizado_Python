import pyautogui
import calendar
from time import sleep
from pathlib import Path

from funcoes_buscar_imagens import clica_na_imagem_spotify

pasta_imgs_spotify = Path('D:\\Cursos\\Python\\Asimov\\Projetos\\PyAutoGUI\\Onboarding_Funcionarios\\imgs_spotify')

def clique_mes(mes_nascimento):
    meses = {
        'January': str(pasta_imgs_spotify) + '\\opcao_janeiro.png',
        'February': str(pasta_imgs_spotify) + '\\opcao_fevereiro.png',
        'March': str(pasta_imgs_spotify) + '\\opcao_marco.png',
        'April': str(pasta_imgs_spotify) + '\\opcao_abril.png',
        'May': str(pasta_imgs_spotify) + '\\opcao_maio.png',
        'June': str(pasta_imgs_spotify) + '\\opcao_junho.png',
        'July': str(pasta_imgs_spotify) + '\\opcao_julho.png',
        'August': str(pasta_imgs_spotify) + '\\opcao_agosto.png',
        'September': str(pasta_imgs_spotify) + '\\opcao_setembro.png',
        'October': str(pasta_imgs_spotify) + '\\opcao_outubro.png',
        'November': str(pasta_imgs_spotify) + '\\opcao_novembro.png',
        'December': str(pasta_imgs_spotify) + '\\opcao_dezembro.png'
    }
    imagem_mes_nascimento = pyautogui.locateOnScreen(meses[mes_nascimento], confidence=0.9)

    return pyautogui.click(imagem_mes_nascimento)

def clique_genero(genero):
    generos = {
        'homem': str(pasta_imgs_spotify) + '\\opcao_genero_homem.png',
        'mulher': str(pasta_imgs_spotify) + '\\opcao_genero_mulher.png',
        'nao_binario': str(pasta_imgs_spotify) + '\\opcao_genero_nao_binario.png',
        'nao_informado': str(pasta_imgs_spotify) + '\\opcao_genero_nao_informado.png',
        'outro': str(pasta_imgs_spotify) + '\\opcao_genero_outro.png'
    }
    imagem_opcao_genero = pyautogui.locateOnScreen(generos[genero], confidence=0.9)

    return pyautogui.click(imagem_opcao_genero)

def spotify_registro(email, senha, usuario, cpf, nascimento, dados_cartao, genero):

    MES = calendar.month_name[int(nascimento[4:6])]

    #acesso ao navegador
    clica_na_imagem_spotify('icone_chrome_bk')
    sleep(3)
    
    #acesso ao modo visitante do chrome
    clica_na_imagem_spotify('botao_modo_visitante_chrome')
    sleep(1)

    #maximiza a janela do chrome
    pyautogui.keyDown('alt')
    sleep(1)
    pyautogui.press(' ')
    sleep(1)
    pyautogui.press('x')
    sleep(1)
    pyautogui.keyUp('alt')
    sleep(2)
    
    # #abre nova guia anonima
    # pyautogui.hotkey('ctrl', 'shift', 'n')
    # sleep(2)
    #acessa a barra de pesquisa
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write('spotify', interval=0.10)
    pyautogui.press('space')
    pyautogui.press('enter')
    sleep(5)
    #acessa pagina spotify
    try:
        clica_na_imagem_spotify('link_spotify')
    except:
        clica_na_imagem_spotify('link_spotify_black')    
    sleep(8)
    #clica em permitir tudo (cookies)
    clica_na_imagem_spotify('botao_perm_cookies')
    sleep(4)
    #clica em 'inscreva-se'
    clica_na_imagem_spotify('botao_inscrever_se')
    sleep(6)
    #clica no campo de texto e insere email
    clica_na_imagem_spotify('campo_email')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(email, interval=0.1)
    #clica em 'seguinte'
    clica_na_imagem_spotify('botao_seguinte')
    sleep(1)
    #clica no campo de texto e insere uma senha
    clica_na_imagem_spotify('campo_senha')
    pyautogui.write(senha, interval=0.10)
    #clica em 'seguinte'
    clica_na_imagem_spotify('botao_seguinte')
    sleep(1)
     #clica no campo de texto e insere o Nome de usuario
    clica_na_imagem_spotify('campo_nome')
    pyautogui.write(usuario, interval=0.10)
    #preenche o campo do dia da data de nascimento
    clica_na_imagem_spotify('campo_dia_nascimento')
    pyautogui.write(nascimento[-2:], interval=0.10)
    #clica no dropdown para selecionar o mês da data de nascimento
    clica_na_imagem_spotify('campo_mes_nascimento')
    #clica no mês da data de nascimento
    sleep(1)

    #clica_na_imagem_spotify(pasta_imgs_spotify/'opcao_outubro')
    clique_mes(MES)
    sleep(1)
    
    #preenche ano da data de nascimento
    clica_na_imagem_spotify('campo_ano_nascimento')
    pyautogui.write(nascimento[:4], interval=0.10)
    sleep(1)
    
    #seleciona genero
    clique_genero(genero)
    #clica_na_imagem_spotify(pasta_imgs_spotify/'opcao_genero_homem')   
    #scroll para o botão avançar
    pyautogui.scroll(-300)
    #clica em 'seguinte'
    clica_na_imagem_spotify('botao_avancar')
    sleep(1)
    #concordar com termos e condições
    clica_na_imagem_spotify('opcao_concordo_com_termos')
    sleep(1)
    #clicar em registrar-se
    clica_na_imagem_spotify('botao_inscrever_se_2')
    sleep(10)
    #clicar no captcha e depois em continuar
    clica_na_imagem_spotify('captcha')
    sleep(2)
    clica_na_imagem_spotify('botao_continuar_captcha')
    sleep(10)
    #acessa tour guiado
    clica_na_imagem_spotify('campo_pesq_artista')
    sleep(2)
    pyautogui.write('teste')
    try:
        clica_na_imagem_spotify('label_artista')
    except:
        clica_na_imagem_spotify('icone_interno_spot')
    sleep(2)
    #Acessar aba Premium
    clica_na_imagem_spotify('botao_ver_planos_premium')
    sleep(3)

    #clica em comece agora
    clica_na_imagem_spotify('botao_comece_agora')
    sleep(8)

    # #Ver planos
    # clica_na_imagem_spotify('botao_ver_todos_planos')
    # sleep(1)
    # #seleciona plano individual
    # clica_na_imagem_spotify('botao_exper_individual')
    # pyautogui.scroll(-20)
    # pyautogui.move(0, 310)
    # pyautogui.click()
    
    #Clica no card da assinatura
    # clica_na_imagem_spotify('card_assinatura_mensal')
    # sleep(1)
    #Seleciona tipo de pagamento - cartão de crédito

    clica_na_imagem_spotify('card_cartao_credito_2')
    sleep(3)
    #desce um pouco a tela
    pyautogui.scroll(-500)
    sleep(4)
    #preenchimento das informações de pagamento
    clica_na_imagem_spotify('campo_num_cartao')
    pyautogui.write(dados_cartao['numero'], interval=0.10)
    clica_na_imagem_spotify('campo_val_cartao')
    pyautogui.write(dados_cartao['validade'], interval=0.10)
    clica_na_imagem_spotify('campo_codigo_cvv')
    pyautogui.write(dados_cartao['cvv'], interval=0.10)
    clica_na_imagem_spotify('campo_nome_cartao')
    pyautogui.write(dados_cartao['nome'] + dados_cartao['sobrenome'], interval=0.10)
    clica_na_imagem_spotify('campo_cpf_cartao')
    pyautogui.write(cpf, interval=0.10)
    #desce ate o fim da pagina
    pyautogui.scroll(-1000)
    #clica no botao compre agora
    clica_na_imagem_spotify('botao_concluir_compra')
    sleep(15)
    #fecha a janela
    pyautogui.hotkey('ctrl', 'w')
    sleep(2)

# DADOS_CARTAO = {'numero': '5544618169021780', 'validade': '01/28', 'cvv': '111', 'nome': 'NOME', 'sobrenome': 'SOBRENOME'}
# spotify_registro('chaves_chapadim@gmail.com.br','avdFG*96$%$','fulano_abczas', '25836974125', '19771025', DADOS_CARTAO, 'homem')