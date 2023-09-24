# Importar o módulo os para manipular arquivos e pastas
import os

# Definir o caminho da pasta que contém as imagens
pasta = "C:\Users\gusta\OneDrive\Documentos\GitHub\Construção da Rede Neural\Converter imagem\Converter imagem\Gustavo\Nova pasta"

# Percorrer todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    # Verificar se o arquivo é uma imagem
    if arquivo.endswith(".jpg") or arquivo.endswith(".png") or arquivo.endswith(".gif"):
        # Obter o nome antigo do arquivo sem a extensão
        nome_antigo = os.path.splitext(arquivo)[0]
        # Obter a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1]
        # Definir o novo nome do arquivo como carregado + a extensão
        nome_novo = "Carregado " + extensao
        # Renomear o arquivo na pasta
        os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, nome_novo))
        # Imprimir uma mensagem informando que o arquivo foi renomeado
        print(f"O arquivo {nome_antigo}{extensao} foi renomeado para {nome_novo}")
