print("Bem-vindo a NEO Porto. Aqui nos agilizamos seu processo de solicitacao de guincho!")
print("")
print("Vamos começar?")
start = int(input("Digite (1) para SIM e (2) para NAO: "))
while start == 1:
    cpf = float(input("Informe seu CPF ou CNPJ: "))
    print("Para prosseguir precisamos de mais algumas informacoes.")
    veic = input("Qual a placa do veiculo: ")
    # PRIMEIRO VEMOS SE O ATENDIMENTO É IMEDIATO OU DE AGENDAMENTO
    imediatouagendamento = int(input("Digite (1) para ATENDIMENTO IMEDIATO ou (2) para AGENDAMENTO: "))
    match imediatouagendamento:
        case 1:
            print("ATENDIMENTO IMEDIATO")
            # CASO SEJA IMEDIATO, AQUI VEMOS O QUE ACONTECEU
            situacao = int(input("Sua situacao e: (1) ACIDENTE DE TRANSITO e (2) FALHA OPERACIONAL: "))
            match situacao:
                # SITUAÇÃO 1 - ACIDENTE DE CARRO
                case 1:
                    print("Acidente de transito")
                    # AQUI PERGUNTAMOS SE O CARRO QUE SOFREU O ACIDENTE DE TRANSITO É LEVE OU COMUM
                    tipo_carro = int(input("O seu veiculo e (1) leve/comum ou (2) pesado?"))
                    if tipo_carro == 1:
                        # TRANSITO + LEVE
                        end_leve = input("Qual endereco para atendimento? ")
                        tel_leve = input("Qual telefone para atendimento? ")
                        print(
                            f"O guinhco para o veiculo comum/leve de placa: {veic} do propietário de CPF: {cpf} está sendo enviado para o endereco: {end_leve}")
                        deseja_cont_leve_transito = input("Encerrar atendimento? (1) para SIM e (2) para NAO")
                        while deseja_cont_leve_transito == 1:
                            print("FIM DO ATENDIMENTO")
                        break
                        # TRANSITO + PESADO
                    elif tipo_carro == 2:
                        end_pesado = input("Qual endereco para atendimento? ")
                        tel_pesado = input("Qual telefone para atendimento? ")
                        # PERGUNTAMOS SE O DONO DO VEICULO PESADO JÁ TEM CONHECIMENTO DO TIPO DE GUINHCO QUE PRECISA
                        guincho_escolha = int(input(
                            "Voce tem conhecimento sobre guinchos e saberia o necessario para seu veiculo?: (1) - SIM e (2) NAO "))
                        # CASO SIM, NÓS PEDIMOS MAIS INFORMAÇÕES PARA CONFIRMAR E ENVIAMOS.
                        if guincho_escolha == 1:
                            tipo_guincho = input("Digite o tipo de guinhco que nos encaminharemos para você")
                            print(
                                "Para não termos erros, digite as proximas informações de acordo com seu conhecimento sobre seu veiculo: ")
                            tipo_carroceria = (input("Digite o tipo de carroceria: "))
                            chassi_alongado = (input("Seu chassi é alongado?: "))
                            comprimento = float(input("Qual o comprimento do seu veiculo?: "))
                            peso_com_carga = float(input("Peso do veiculo com a carga: "))
                            peso_sem_carga = float(input("Peso do veiculo sem a carga: "))
                            quantidade_de_eixos = int(input("Qual a quantidade de eixo: "))
                            print(
                                f"O guinhco {tipo_guincho}para o veiculo comum/leve de placa: {veic} do propietário de CPF: {cpf} está sendo enviado para o endereço: {end_pesado}")
                            deseja_cont_pesado_transito = input("Encerrar atendimento? (1) para SIM e (2) para NAO")
                            while deseja_cont_pesado_transito == 1:
                                print("FIM DO ATENDIMENTO")
                            break
                            # CASO NÃO, NÓS PEDIMOS MAIS INFORMAÇÕES.
                        elif guincho_escolha == 2:
                            print("OK, nos iremos te auxiliar nos próximos passsos!")
                            # TENTAMOS VER SE O DONO SABE ALGO SOBRE VEICULOS PESADOS PRIMEIRO MAS CASO NÃO, NÓS ENVIAMOS O AUXILIO TAMBÉM
                            print(
                                "Digite de acordo com seu conhecimento as seguintes especificações do seu veiculo, se souber. (Caso não saiba, digite apenas 0)")
                            tipo_carroceria = (input("Digite o tipo de carroceria: "))
                            chassi_alongado = (input("Seu chassi é alongado?: "))
                            comprimento = float(input("Qual o comprimento do seu veiculo?: "))
                            peso_com_carga = float(input("Peso do veiculo com a carga: "))
                            peso_sem_carga = float(input("Peso do veiculo sem a carga: "))
                            quantidade_de_eixos = int(input("Qual a quantidade de eixo: "))
                            # SE O DONO NÃO SOUBER DE NADA, NÓS ENVIAMOS O AUXILIO.
                            if tipo_carroceria and chassi_alongado and comprimento and peso_com_carga and peso_sem_carga and quantidade_de_eixos == 0:
                                print(
                                    f"Iremos encaminhar  um de nossos atendentes para te auxiliar melhor. Confirme os dados abaixo: ")
                                print(f"Guincho pedido pelo CPF/CNPJ: {cpf}")
                                print(f"Ser atendido no endereço: {end_pesado}")
                                print(f"Telefone para contato: {tel_pesado}")
                                deseja_cont_pesado_transito_nao_sabe = input(
                                    "Encerrar atendimento? (1) para SIM e (2) para NAO: ")
                                while deseja_cont_pesado_transito_nao_sabe == 1:
                                    print("FIM DO ATENDIMENTO")
                                break
                                # CASO ELE SAIBA DE ALGUMA INFORMAÇÃO
                            else:
                                print(
                                    f"Obrigade pelas informações. O guinhco para o veiculo pesado de placa: {veic} do propietário de CPF: {cpf} está sendo enviado para o endereço: {end_pesado}")
                                deseja_cont_pesado_transito_nao_sabe = input(
                                    "Encerrar atendimento? (1) para SIM e (2) para NAO: ")
                                while deseja_cont_pesado_transito_nao_sabe == 1:
                                    print("FIM DO ATENDIMENTO")
                                break
                    else:
                        print("TIPO DE CARRO INVÁLIDO!")
                case 2:
                    print("FALHA OPERACIONAL")

                    # AQUI PERGUNTAMOS SE O CARRO QUE SOFREU O FALHA OPERACIONAL É LEVE OU COMUM
                    tipo_carro = int(input("O seu veiculo é (1) leve/comum ou (2) pesado? "))
                    if tipo_carro == 1:
                        # FALHA + LEVE
                        end_leve = input("Qual endereco para atendimento? ")
                        tel_leve = input("Qual telefone para atendimento? ")
                        print(
                            f"O guinhco para o veiculo comum/leve de placa: {veic} do propietario de CPF: {cpf} está sendo enviado para o endereco: {end_leve}")
                        deseja_cont_leve_falha = input("Encerrar atendimento? (1) para SIM e (2) para NAO: ")
                        while deseja_cont_leve_falha == 1:
                            print("FIM DO ATENDIMENTO")
                        break
                        # FALHA + PESADO
                    elif tipo_carro == 2:
                        end_pesado = input("Qual endereco para atendimento? ")
                        tel_pesado = input("Qual telefone para atendimento? ")
                        # PERGUNTAMOS SE O DONO DO VEICULO PESADO JÁ TEM CONHECIMENTO DO TIPO DE GUINHCO QUE PRECISA
                        guincho_escolha = int(input("Você sabe que tipo de guincho precisaria? (1) - SIM e (2) NAO "))
                        # CASO SIM, NÓS PEDIMOS MAIS INFORMAÇÕES PARA CONFIRMAR E ENVIAMOS.
                        if guincho_escolha == 1:
                            tipo_guincho = input("Digite o tipo de guinhco que nós encaminharemos para você: ")
                            print(
                                "Para não termos erros, digite as próximas informações de acordo com seu conhecimento")
                            tipo_carroceria = (input("Digite o tipo de carroceria? "))
                            chassi_alongado = (input("Seu chassi é alongado? "))
                            comprimento = float(input("Qual o comprimento do seu veiculo? "))
                            peso_com_carga = float(input("Peso do veiculo com a carga "))
                            peso_sem_carga = float(input("Peso do veiculo sem a carga "))
                            quantidade_de_eixos = int(input("Qual a quantidade de eixo "))

                            print(
                                f"O guinhco {tipo_guincho}para o veiculo comum/leve de placa: {veic} do propietario de CPF: {cpf} está sendo enviado para o endereço {end_pesado}")
                            deseja_cont_pesado_transito = input("Encerrar atendimento? (1) para SIM e (2) para NAO: ")
                            while deseja_cont_pesado_transito == 1:
                                print("FIM DO ATENDIMENTO")
                            break
                            # CASO NÃO, NÓS PEDIMOS MAIS INFORMAÇÕES.
                        elif guincho_escolha == 2:
                            print("Ok, iremos te auxiliar nos proximos passos.")
                            # TENTAMOS VER SE O DONO SABE ALGO SOBRE VEICULOS PESADOS PRIMEIRO MAS CASO NÃO, NÓS ENVIAMOS O AUXILIO TAMBÉM
                            print(
                                "Digite de acordo com seu conhecimento as seguintes especificações se souber. (Caso nao saiba, digite apenas 0 em cada uma")
                            tipo_carroceria = (input("Digite o tipo de carroceria: "))
                            chassi_alongado = (input("Seu chassi é alongado? "))
                            comprimento = float(input("Qual o comprimento do seu veiculo? "))
                            peso_com_carga = float(input("Peso do veiculo com a carga "))
                            peso_sem_carga = float(input("Peso do veiculo sem a carga "))
                            quantidade_de_eixos = int(input("Qual a quantidade de eixo "))
                            # SE O DONO NÃO SOUBER DE NADA, NÓS ENVIAMOS O AUXILIO.
                            if tipo_carroceria and chassi_alongado and comprimento and peso_com_carga and peso_sem_carga and quantidade_de_eixos == 0:
                                print(
                                    f"Iremos encaminhar um de nossos atendentes para te auxiliar melhor. Confirme os dados abaixo: ")
                                print(f"Guincho pedido pelo CPF/CNPJ: {cpf}")
                                print(f"Ser atendido no endereço: {end_pesado}")
                                print(f"Telefone para contato: {tel_pesado}")
                                print(
                                    f"O guinhco para o veiculo pesado de placa: {veic} do propietário de cpf: {cpf} está sendo enviado para o endereço {end_pesado}")
                                deseja_cont_pesado_transito_nao_sabe = input(
                                    "Encerrar atendimento? (1) para SIM e (2) para NAO")
                                while deseja_cont_pesado_transito_nao_sabe == 1:
                                    print("FIM DO ATENDIMENTO")
                                break
                            # CASO ELE SAIBA DE ALGUMA INFORMAÇÃO
                            else:
                                print(
                                    f"Obrigade pelas informações. Iremos tentar enviar o guincho que mais se encaixa com a suas especificacoes. Atendimento para o veiculo pesado de placa: {veic} do propietário de CPF: {cpf} está sendo enviado para o endereco {end_pesado}")
                                deseja_cont_pesado_transito_nao_sabe = input(
                                    "Encerrar atendimento? (1) para SIM e (2) para NAO")
                                while deseja_cont_pesado_transito_nao_sabe == 1:
                                    print("FIM DO ATENDIMENTO")
                                break
        # CASO AGENDAMENTO
        case 2:
            print("AGENDAMENTO: OBS* So realizamos agendamentos dentro do mês do pedido")
            data_agendamento = input("Para qual data gostaria de agendar? ")
            hora_agendamento = input("Que horas seria feito o atendimento? ")
            end_agendamento = input("Qual endereço deveremos ir? ")
            tel_agendamento = input("Qual telefone devemos ligar? ")
            tipo_carro_agedamento = int(input("O seu veiculo e (1) leve/comum ou (2) pesado? "))
            if tipo_carro_agedamento == 1:
                # veiculo leve
                print(
                    f"O guincho para seu veiculo leve irá ser enviado dia: {data_agendamento} as: {hora_agendamento} para o endereco: {end_agendamento}.")
                print(f"iremos contatar pelo telefone: {tel_agendamento}")
                deseja_cont_leve_agendamento = input("Encerrar atendimento? (1) para SIM e (2) para NAO: ")
                while deseja_cont_leve_agendamento == 1:
                    print("FIM DO ATENDIMENTO")
                break
            elif tipo_carro_agedamento == 2:
                # veiculo pesado
                print(
                    "Para melhor assertividade, digite as proximas informações de acordo com seu conhecimento sobre seu veiculo.")
                print("Caso não saiba, digite apenas (0)")
                tipo_carroceria = (input("Digite o tipo de carroceria: "))
                chassi_alongado = (input("Seu chassi é alongado?: "))
                comprimento = float(input("Qual o comprimento do seu veiculo?: "))
                peso_com_carga = float(input("Peso do veiculo com a carga: "))
                peso_sem_carga = float(input("Peso do veiculo sem a carga: "))
                quantidade_de_eixos = int(input("Qual a quantidade de eixo: "))
                if tipo_carroceria and chassi_alongado and comprimento and peso_com_carga and peso_sem_carga and quantidade_de_eixos == 0:
                    print("Obrigado pelas informacoes. ")
                    print(
                        f"O guinhco para o veiculo pesado foi agendado para o dia: {data_agendamento} as: {hora_agendamento}")
                    print(
                        f" MAIS INFORMACOES: placa: {veic} propietário de CPF: {cpf} foi solcicitado para o endereco: {end_agendamento}")
                    deseja_cont_pesado_agendamento = input("Encerrar atendimento? (1) para SIM e (2) para NAO")
                    while deseja_cont_pesado_agendamento == 1:
                        print("FIM DO ATENDIMENTO")
                    break
                else:
                    print("Obrigade pelas informacoes.")
                    print(
                        f"O guinhco para o veiculo pesado de placa: {veic} do propietário de CPF: {cpf} para o endereco: {end_agendamento} foi agendado.")
                    deseja_cont_pesado_agendamento = input("Encerrar atendimento? (1) para SIM e (2) para NAO")
                    while deseja_cont_pesado_agendamento == 1:
                        print("FIM DO ATENDIMENTO")
                    break
            else:
                print("TIPO DE VEICULO INVÁLIDO")
            print("FIM DO ATENDIMENTO")

print("ATENDIMENTO ENCERRADO")