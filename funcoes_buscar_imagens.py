import pyautogui
from time import sleep
from pathlib import Path

caminho_imagens_netflix = Path.cwd()/'imgs_netflix'
caminho_imagens_spotify = Path.cwd()/'imgs_spotify'

def clica_na_imagem_netflix(img):
    imagem = str(caminho_imagens_netflix/img) + '.png'
    sleep(1)
    local_imagem = pyautogui.locateOnScreen(imagem, confidence=0.85)
    return pyautogui.click(local_imagem)

def clica_na_imagem_spotify(img):
    imagem = str(caminho_imagens_spotify/img) + '.png'
    sleep(1)
    local_imagem = pyautogui.locateOnScreen(imagem, confidence=0.85)
    return pyautogui.click(local_imagem)