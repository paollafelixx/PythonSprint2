def main():
    #Questionando qual serviço o cliente deseja

    inicio = int(input("Você entrou em contato com a NeoPorto, o mais novo serviço de atendimento ao cliente da Porto Seguro. Como posso te ajudar?\n1 - Guincho para veiculos pesados.\n2 - Outros serviços\nInforma a opção desejada: "))
    # Verificando se o o cliente já cadastrado ou não
    cliente = 0

    if inicio == 1:
        # Solicitando os dados para verificar se já é cliente Porto Seguro cadastrado
        dados = float(input("Para prosseguir preciso que informe o CPF ou CNPJ: "))
        placa = input("E a placa do veículo: ")
        # Cliente cadastrado
        if cliente == 1:
           # Questionando qual o tipo de veiculo pesado para o atendimento
           print("Certo, já encontrei seu cadastro! Você não possui historico de atendimentos anteriores!")
           print("Para mais informações, você pode dizer qual tipo de veiculo pesado ele é?")
           int(input("1- Trator \n2- Caminhão \n3- Carreta \n4- Veículo pessoal \n5- Veículo de passageiros \nOpção: "))
        else:
            # Cliente não cadastrado
            print("Você ainda não possui cadastro com a Porto Seguro. Por gentileza entre em contato no telfone: XX-XXXX-XXXX.")








if (__name__ == "__main__"):
    main()