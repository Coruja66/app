import time
from pypresence import Presence
import psutil  # Para verificar processos em execução
import win32gui  # Para obter o título da janela

# Inicialize a conexão com o Discord RPC
RPC = Presence('1108191461075320952')  # Coloque o ID da sua aplicação Discord aqui
RPC.connect()

game_id = "16201790479"  # Substitua pelo ID do seu jogo no Roblox

# Função para verificar se o jogo Roblox está em execução e se é o jogo específico
def is_specific_game_running():
    for process in psutil.process_iter():
        if "RobloxPlayerBeta.exe" in process.name():
            cmdline = process.cmdline()
            if any(game_id in arg for arg in cmdline):
                return True
    return False

# Loop principal
while True:
    if is_specific_game_running():
        # Define as informações de Rich Presence para o Roblox
        RPC.update(
            details="Jogando alpha",
            state="teste",
            large_image="resenha",  # Nome do asset de imagem grande
            large_text="Roblox",  # Texto ao passar o mouse sobre a imagem grande
            small_image="resenha",  # Nome do asset de imagem pequena
            small_text="Jogo do Roblox"  # Texto ao passar o mouse sobre a imagem pequena
        )
    else:
        # Se não estiver jogando Roblox, limpa o Rich Presence
        RPC.clear()

    time.sleep(15)  # Verifica a cada 15 segundos se o jogo está em execução
