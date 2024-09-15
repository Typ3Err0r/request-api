import argparse
import requests

def verificar_exposicao(api_url):
    try:
        # Faça uma solicitação GET para a API
        response = requests.get(api_url)

        # Verifique se a resposta indica que a API está acessível
        if response.status_code == 200:
            print(f'\033[31m A API em {api_url} está sem verificação.\033[0m')
        else:
            print(f'\033[32m A API em {api_url} retornou um status diferente de 200.\033[0m')

    except requests.RequestException as e:
        print(f'Erro ao acessar a API em {api_url}: {str(e)}')

def main():
    parser = argparse.ArgumentParser(description='Verificar exposição de APIs ao navegador.')
    parser.add_argument('-w', '--file', help='Caminho para o arquivo de lista de hosts (wordlist).')
    parser.add_argument('-u', '--url', help='URL de um host específico para verificar.')

    args = parser.parse_args()

    if args.file:
        # Se o argumento -f (--file) foi fornecido, ler a lista de hosts do arquivo
        with open(args.file, 'r') as file:
            lista_de_urls = [line.strip() for line in file if line.strip()]
    elif args.url:
        # Se o argumento -u (--url) foi fornecido, usar apenas esse host
        lista_de_urls = [args.url]
    else:
        print('É necessário fornecer um arquivo de lista de hosts (-w) ou um host específico (-u).')
        return

    # Verificar cada URL na lista
    for url in lista_de_urls:
        verificar_exposicao(url)

if __name__ == "__main__":
    main()

