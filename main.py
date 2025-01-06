import os
import unicodedata
import re

def slugify(text):
    """
    Converte um texto para um formato de slug amigável para URLs.
    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[\s_-]+', '-', text)

def renomear_arquivos_pasta(caminho_pasta):
    """
    Renomeia todos os arquivos na pasta aplicando um slug aos seus nomes.

    Args:
        caminho_pasta (str): Caminho da pasta que contém os arquivos.
    """
    if not os.path.isdir(caminho_pasta):
        print(f"Erro: {caminho_pasta} não é uma pasta válida.")
        return

    for nome_arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

        if os.path.isfile(caminho_completo):
            nome, extensao = os.path.splitext(nome_arquivo)
            nome_slug = slugify(nome)
            novo_nome = f"{nome_slug}{extensao}"
            novo_caminho = os.path.join(caminho_pasta, novo_nome)

            try:
                os.rename(caminho_completo, novo_caminho)
                print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
            except Exception as e:
                print(f"Erro ao renomear {nome_arquivo}: {e}")

# Exemplo de uso
caminho = input("Digite o caminho da pasta: ")
renomear_arquivos_pasta(caminho)
