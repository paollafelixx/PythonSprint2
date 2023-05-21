def main():
    #Questionando qual serviço o cliente deseja

    inicio = int(input("Você entrou em contato com a NeoPorto, o mais novo serviço de atendimento ao cliente da Porto Seguro. Como posso te ajudar?\n1 - Guincho para veiculos pesados.\n2 - Outros serviços\nInforma a opção desejada: "))


    match inicio:
        case 1:
            # Solicitando os dados para verificar se já é cliente Porto Seguro cadastrado
            dados = float(input("Para prosseguir preciso que informe o CPF ou CNPJ: "))
            placa = input("E a placa do veículo: ")
        case 2:
            print("Opção desejada: Outros serviços. ")
        case _:
            print("Opção invalida.")







if (__name__ == "__main__"):
    main()


