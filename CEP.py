import requests

def main():
    print('#####################')
    print('Consulta CEP')
    print('#####################')
    print()

    #Verifica quantidade de digitos
    cep_input = input('Digite o CEP para a consulta')
    if len(cep_input) !=8:
        print('Quantidade de dígitos inválida')
        exit()

    #Requisicao API viaCEP
    request = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep_input))
    address_data = request.json()

    #Imprimi informações senao imprimi CEP Inválido
    if 'erro' not in address_data:
            print('==> CEP ENCONTRADO <==')

            print('CEP: {}'.format(address_data['cep']))
            print('Logradouro: {}'.format(address_data['logradouro']))
            print('Complemento: {}'.format(address_data['complemento']))
            print('Bairro: {}'.format(address_data['bairro']))
            print('Cidade: {}'.format(address_data['localidade']))
            print('Estado: {}'.format(address_data['uf']))
    else:
            print('{}: CEP inválido.'.format(cep_input))
            print('------------------------')
    option = int(input('Deseja realizar uma nova consulta?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')




if __name__ == '__main__':
    main()
