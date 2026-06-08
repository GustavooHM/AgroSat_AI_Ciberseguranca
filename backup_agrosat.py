import os
import shutil
from datetime import datetime

origem = "dados/banco_agrosat_ai.txt"
pasta_backup = "backups"

os.makedirs(pasta_backup, exist_ok=True)

data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
destino = f"{pasta_backup}/backup_agrosat_ai_{data_hora}.txt"

try:
    shutil.copy2(origem, destino)
    print("Backup realizado com sucesso!")
    print(f"Arquivo original: {origem}")
    print(f"Arquivo de backup: {destino}")
except FileNotFoundError:
    print("Erro: arquivo original não encontrado.")
except Exception as erro:
    print(f"Erro ao realizar backup: {erro}")