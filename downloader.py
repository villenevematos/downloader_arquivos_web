import requests


# Define uma função para baixar um arquivo da internet
def download_file(url, save_path):
    try:
        # Envia uma requisição HTTP GET para a URL fornecida
        response = requests.get(url)
        
        # Verifica se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Abre (ou cria) um arquivo local no modo binário de escrita
            with open(save_path, 'wb') as file:
                # Escreve o conteúdo da resposta no arquivo
                file.write(response.content)
            print(f"Arquivo baixado com sucesso: {save_path}")
        else:
            # Caso o status não seja 200, exibe mensagem de erro com o código
            print(f"Falha ao baixar o arquivo. Código de status: {response.status_code}")
    except Exception as e:
        # Captura e exibe qualquer erro ocorrido durante o processo
        print(f"Erro: {e}")

# URL do arquivo PDF a ser baixado
url_download = "https://cafeculturabrasil.com/wp-content/uploads/2025/10/MB-cafe-cultura-cardapio-impresso-167x30cm-2025_261-1.pdf"

# Caminho onde o arquivo será salvo localmente
save_path = 'C:/Users/CASA/Downloads/documentos/.pdf/Cardapio.pdf'

# Chama a função para realizar o download do arquivo
download_file(url_download, save_path)