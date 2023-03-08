###                         Projeto em grupo módulo 2 Resilia/Senac                          ###
###                            The Yellow Submarine Researcher                               ###
###   Membros: Cassio Ribeiro, Daniel Marques, Joice Souza , Vitor Rangel, Matheus Barbosa   ###


class questions:                # classe criada e denominada 'questions'.
    def __init__(self):                 #def init sem parâmetro e com o pass para que ele nada faça.
        pass

    def questions_post_pandemic(self):     # def que irá realizar a pesquisa pós pendemia.
        import pandas as pd                     #\
        from datetime import datetime           #/ bibliotecas usadas durante o código.
        from os import system                   # biblioteca para dar um clear na tela ao reiniciar a pesquisa
        from termcolor import colored           # Biblioteca usada para colorir todas nossas strings de amarelo
        listaQ = []                             # lista vazia criada para armazenar os dados da pesquisa para posteriormente serem gravdas num arquivo CSV.
        exit = 1
        while exit  != 2:                       # estrutura de repetição onde será coletada os dados de cada entrevistado.
            print(("\n{:^170}\n").format(colored("PESQUISA HÁBITOS PÓS PANDEMIA", "yellow")))   #print de saudação.
            
            try:                                # tratamento de exceção para evitar erros no código.
                idade = int(input(colored("Idade do Entrevistado: ", "yellow")))       # variável 'idade' onde é inserida a idade do entrevistado.
                if idade == 00:                                 #condicional para encerrar o programa conforme solicitado pelo usuário.
                    print(colored("\nIdade inválida. Programa encerrado\n","yellow" ))    #print para informar que o programa foi encerrado devido a idade inexistente inserida.
                    break
                
                elif idade >150:
                    print(colored("\nIdade inválida\n","yellow"))       #print para orientar o usuário a inserir uma opção válida.
                    continue                            # 'continue' usado para pedir novamente a idade caso ela seja maior de 150.
                elif idade < 15:                        
                    print(colored("\nIdade inválida. É preciso ser maior de 15 anos para participar da pesquisa\n","yellow"))       #print para orientar o usuário a inserir uma opção válida.
                    continue
                

            except:
                print(colored("\nOpção inválida. Favor inserir uma idade válida\n","yellow"))
                continue                 # 'continue' usado para pedir novamente a idade caso tenha sido inserido algo diferente de número.
                

            genero = 4
            while genero >3:            #estrutura de repetição que irá coletar o genero do entrevistado.
                try:                    # tratamento de exceção para evitar erros no código.
                    genero = int(input(colored("\nAgora nos diga o seu genero\n[1] - Masculino\n[2] - Feminino\n[3] - Prefiro não informar\nselecione sua opção: ", "yellow")))        #variável com menu de opções para o usuário.
                    if genero == 1:         # condicional para validar o genero masculino.
                        gender = "Masculino"   # variável onde é armazenada o genero do entrevistado conforme escolha no menu anterior.
                    elif genero == 2:           # condicional para validar o genero feminino.
                        gender = "Feminino"   # variável onde é armazenada o genero do entrevistado conforme escolha no menu anterior.
                    elif genero == 3:               # condicional para validar o genero não informado.
                        gender = "Não informado"   # variável onde é armazenada o genero do entrevistado conforme escolha no menu anterior.
                    else:
                        print(colored("\nOpção inválida\n","yellow"))         #print para orientar o usuário a inserir uma opção válida.
                except:
                    print(colored("\nOpção inválida. Favor escolher uma opção conforme menu.\n","yellow"))  #print para orientar o usuário a inserir uma opção válida.

            print("\n{:^170}\n".format(colored("VAMOS INICIAR NOSSA PESQUISA", "yellow")))  #print de saudação para iniciar as perguntas da pesquisa.
            
            
            
            q1 = 4
            while q1 >3:        #estrutura de repetição que irá coletar a resposta da primeira pergunta do entrevistado.
                try:             # tratamento de exceção para evitar erros no código.
                    q1 = int(input(colored("\nVocê tomou todas as doses da vacina contra o Covid 19? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: ", "yellow")))        #variável com menu de opções para o usuário.
                    if q1 >3:           #condicional para validar a primeira resposta do entrevistado.
                        print(colored("\nOpção inválida\n","yellow"))        #print para orientar o usuário a inserir uma opção válida.
                except:
                    print(colored("\nOpção inválida. Favor escolher uma opção conforme menu.\n","yellow"))   # print para orientar.
            
            q2 =4
            while q2 >3:                         #estrutura de repetição que irá coletar a resposta da segunda pergunta do entrevistado.
                try:                                        # tratamento de exceção para evitar erros no código.
                    q2 = int(input(colored("\nVocê ainda usa a máscara em locais públicos? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: : ", "yellow")))  #variável com menu de opções para o usuário.
                    if q2 >3:                               #condicional para validar a segunda resposta do entrevistado.
                        print(colored("\nOpção inválida\n","yellow"))         #print para orientar o usuário a inserir uma opção válida.
                except:
                    print(colored("\nOpção inválida. Favor escolher uma opção conforme menu.\n","yellow"))          #print para orientar o usuário a inserir uma opção válida.
            
            q3 =4
            while q3 >3:                          #estrutura de repetição que irá coletar a resposta da terceira pergunta do entrevistado.
                try:                                        # tratamento de exceção para evitar erros no código.
                    q3 = int(input(colored("\nVocê ainda faz uso contínuo de alcool para higienização das mãos? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: ", "yellow")))     #variável com menu de opções para o usuário.
                    if q3 >3:                               #condicional para validar a terceira resposta do entrevistado.
                        print(colored("\nOpção inválida\n","yellow"))         #print para orientar o usuário a inserir uma opção válida.
                except:
                    print(colored("\nOpção inválida. Favor escolher uma opção conforme menu.\n","yellow"))            #print para orientar o usuário a inserir uma opção válida.
            q4 =4
            while q4 >3:                          #estrutura de repetição que irá coletar a resposta da quarta pergunta do entrevistado.
                try:                                        # tratamento de exceção para evitar erros no código.
                    q4 = int(input(colored("\nVocê perdeu alçguém próximo devido ao Covid 19 ? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: ", "yellow")))        #variável com menu de opções para o usuário.
                    if q4 >3:                               #condicional para validar a quarta resposta do entrevistado.
                        print(colored("\nOpção inválida\n","yellow"))         #print para orientar o usuário a inserir uma opção válida.
                except:
                    print(colored("\nOpção inválida. Favor escolher uma opção conforme menu.\n","yellow"))        #print para orientar o usuário a inserir uma opção válida.
            
            data = datetime.now()                       # variável que recebe informações em tempo real do sistema.
            data = data.strftime(f"%d/%m/%Y")           # alterando a variável para conter somente a data e organizando no padrão PT/BR.
            horario = datetime.now()                    # variável que recebe informações em tempo real do sistema.
            horario = horario.strftime(f"%H:%M:%S")        # alterando a variável para conter somente a hora exata no momento da coleta.

            

            listaQ.append([idade,gender,q1,q2,q3,q4,data,horario]) #criando uma sub lista com os dados do entrevistado para ser inserida na lista principal.
            
            exit = 4
            while exit >=3:             #estrutura de repetição que irá coletar a informção se o usuário deseja entrevistar mais pessoas nesse momento ou não.
                try:                    # tratamento de exceção para evitar erros no código.
                    exit = int(input(colored("\nDeseja iniciar outra pesquisa?\n[1] - SIM\n[2] - NÃO\nSelecione sua opção: ", "yellow")))
                    if exit == 1:      # condicional para continuar a inserir dados de outros entrevistados.
                        system("cls")   # chamando o comando para dar o clear na tela após o usuário optar por inserir mais dados de outros entrevistados
                        pass           # pass para nada fazer caso seja escolhida essa opção.
                    elif exit == 2:     # condicional que encerra o programa e inicia a transferência dos dados para o arquivo CSV.
                        dflista = pd.DataFrame(listaQ)      # usando o pandas transformamos a lista com os dados em um data frame.
                
                        dflista.to_csv("DadosEntrevistados.csv",  mode = "a" ,index = False, header = False, encoding= "utf-8")   # exportando o data frame criado para nosso arquivo CSV.

                    
                        print("\n{:^170}\n".format(colored("THE YELLOW SQUAD", "yellow")))  #print de saudação final com o nome do nosso squad.
                        print("\n{:^170}\n".format(colored("Mergulhando fundo em busca das solucões para os seus problemas", "yellow")))  #print final com o slogan do nosso squad.
                        
                        
                    else:
                        print(colored("\nOpção inválida\n","yellow"))         #print para orientar o usuário a inserir uma opção válida.
                except:
                    print(colored("\nOpção inválida. Favor escolher uma opção conforme menu.\n","yellow"))       #print para orientar o usuário a inserir uma opção válida.
