def main():
    #Questionando qual serviço o cliente deseja


    inicio = int(input("Você entrou em contato com a NeoPorto, o mais novo serviço de atendimento ao cliente da Porto Seguro. Como posso te ajudar?\n1 - Guincho para veiculos pesados.\n2 - Outros serviços\nInforma a opção desejada: "))


    if inicio == 1:
        veiculos_pesados()
    elif inicio == 2:
        outros_serv()
    else:
        print("Opção invalida.")
        main()

def outros_serv():
    print("Outros serviços.")

def veiculos_pesados():
    # Solicitando os dados para verificar se já é cliente Porto Seguro cadastrado
    global dados
    global placa
    dados = input("Para prosseguir preciso que informe o CPF ou CNPJ: ")
    placa = input("E a placa do veículo: ")
    cliente = 1
    if  cliente == 1:
        # Questionando qual o tipo de veiculo pesado para o atendimento
        print("Certo, já encontrei seu cadastro! Você não possui historico de atendimentos anteriores! \nPara mais informações, você pode dizer qual tipo de veiculo pesado ele é?")

        tp = int(input("1- Trator \n2- Caminhão \n3- Carreta \n4- Veículo pessoal \n5- Veículo de passageiros \nOpção: "))
        if tp == 1:
            carac_trator()
            print()
            eixos()
            print()
            carga()
            print()
            peso()
            print()
            solic_endereco()
            print()
            ref()
            print()
            destino()
            print()
            taxi()
            print()
            confirma_solic()
        elif tp == 2:
            carac_caminhao()
            print()
            eixos()
            print()
            carga()
            print()
            peso()
            print()
            solic_endereco()
            print()
            ref()
            print()
            destino()
            print()
            taxi()
            print()
            confirma_solic()
        elif tp == 3:
            carac_carreta()
            print()
            eixos()
            print()
            carga()
            print()
            peso()
            print()
            solic_endereco()
            print()
            ref()
            print()
            destino()
            print()
            taxi()
            print()
            confirma_solic()
        elif tp == 4:
            carac_veic_pessoal()
            print()
            eixos()
            print()
            carga()
            print()
            peso()
            print()
            solic_endereco()
            print()
            ref()
            print()
            destino()
            print()
            taxi()
            confirma_solic()
        elif tp == 5:
            carac_veic_passageiros()
            print()
            eixos()
            print()
            carga()
            print()
            peso()
            print()
            solic_endereco()
            print()
            ref()
            print()
            destino()
            print()
            taxi()
            print()
            confirma_solic()
        else:
            print("Outros.")

    else:
        # Cliente não cadastrado
        print(
            "Você ainda não possui cadastro com a Porto Seguro. Por gentileza entre em contato no telfone: XX-XXXX-XXXX.")
        main()

# Exemplo com Trator
def carac_trator():
    print("Certo! Escolha entre as opções abaixo a que mais se encaixa como o seu veículo! Se não nenhuma das alternativas abaixo, selecione 'outros' '")
    int(input("1- Trator de rodas \n2-Trator de rasto \n3- Trator normal ou standard \n4- Trator fruteiro \n5- Outros \nOpção: "))

# Exemplo com Caminhão
def carac_caminhao():
    print("Certo! Escolha entre as opções abaixo a que mais se encaixa como o seu veículo! Se não nenhuma das alternativas abaixo, selecione 'outros' '")
    int(input("1- VUC(Veículo Urbano de Carga) \n2-Caminhão Toco \n3- Caminhão Truck \n4- Cavalo Mecânico (ou Caminhão Extrapesado) \n5- Cavalo Mecânico Trucado (ou LS) \n6- Outros \nOpção: "))

# Exemplo com Carreta
def carac_carreta():
    print("Certo! Escolha entre as opções abaixo a que mais se encaixa como o seu veículo! Se não nenhuma das alternativas abaixo, selecione 'outros' '")
    int(input("1- Carreta Sider \n2- Carreta baú \n3- Carreta Cavalo Truckado \n4- Carreta Prancha \n5- Graneleira \n6- Carreta Rodotrem \n7- Carreta Bitrem/treminhão \n8- Outros \nOpção: "))

# Exemplo com veiculo pessoal
def carac_veic_pessoal():
    print("Certo! Escolha entre as opções abaixo a que mais se encaixa como o seu veículo! Se não nenhuma das alternativas abaixo, selecione 'outros' '")
    int(input("1- Caminhonete \n2- Carretinhas \n3- Van \n4- Micro-onibus \n5- Outros \nOpção: "))

# Exemplo com veiculo de passageiros
def carac_veic_passageiros():
    print("Certo! Escolha entre as opções abaixo a que mais se encaixa como o seu veículo! Se não nenhuma das alternativas abaixo, selecione 'outros' '")
    int(input("1- Onibus \n2- Micro-onibus \n3- Van \n4- Outros \nOpção: "))


# Questionando se possui eixos
def eixos():
    print("O veiculo possui eixos?")
    int(input("1- Dois eixos \n2- Três eixos \n3- Quatro ou mais eixos \n4- Não possui eixos \nOpção: "))

# Questionando se possui carga
def carga():
    print("Certo! Só para completar, o veículo está com alguma carga?")
    int(input("Digite 1- Sim ou 0- Não: \nOpção: "))

# Questionando o peso
def peso():
    input("Informe o peso aproximado do veiculo: ")

# Solicitando o endereço do veiculo
def solic_endereco():
   global endereco
   endereco = (input("Por favor, informe o endereço ou envie a localização onde está o veiculo: "))
   print(endereco)

# Solicitando referencia do veiculo
def ref():
    global referenc
    referenc = (input("Por favor, informe um ponto de referencia. Se não houver, digite não possui: "))
    print(referenc)

# Solicitando endereço aonde o veiculo ira ficar
def destino():
    global des
    des = int(input("Preciso que informe aonde o guincho levará o veiculo. Você possui o endereço? (1- SIM ou 0- NÃO): "))
    if des == 1:
       global destino_local
       destino_local =(input("Por favor, digite o endereço completo! Digite assim: 'Rua (av. ou rod.) numero, cidade e estado': "))
       print(destino_local)
    else:
       print("Não se preocupe, iremos resolver ista para você.")


# Verificando se precisa de taxi
def taxi():
    ta = int(input("Você precisa de taxi para deixar o local? (1- SIM ou 0- NÃO): "))
    if ta == 1:
        local = int(input("Você está no mesmo endereço do veiculo? (1-SIM ou 0- NÃO): "))
        if local == 1:
            confirma_solic()
        else:
            end_taxi = input("Informe o endereço: ")


# Confirmando os dados e mostrando o resumo da solicitação
def confirma_solic():
    print("*********************************************************")
    print("Certo. Confira o resumo da sua solicitação: ")
    print("CPF ou CNPJ: ", {dados})
    print("Placa do veiculo: ", {placa})
    print("Localização: ", {endereco})
    print("Referencia: ", {referenc})
    if des == 1:
       print("Destino: ", {destino_local})
       print("*********************************************************")
    else:
        print("Destino: A confirmar \n")
        print("*********************************************************")
    conf = int(input("Está tudo correto? \n1- Sim \n2- Voltar o inicio \n3- Voltar para tipo de veiculo \n4- Voltar para localização do veiculo \n5- Voltar para destino final \nOpção: "))
    if conf == 1:
        print("Aguarde! Sua ajuda em breve estará a caminho!\n")
    elif conf == 2:
        main()
    elif conf == 3:
        veiculos_pesados()
    elif conf == 4:
        solic_endereco()
    elif conf == 5:
        destino()
    else:
        print("Opção invalida.")
    main()


if (__name__ == "__main__"):
    main()