class questions:               
    def __init__(self):                 
        pass

    def questions_post_pandemic(self):     
        import pandas as pd                     
        from datetime import datetime          
        from os import system
        listaQ = []                             
        exit = 1
        while exit  != 2:                       
            print("\n##########{:^150}##########\n".format("PESQUISA HÁBITOS PÓS PANDEMIA"))   
            
            try:                                
                idade = int(input("Idade do Entrevistado: "))       
                if idade == 00:                                 
                    print("\nIdade inválida. Programa encerrado\n")    
                    break
                
                elif idade >150:
                    print("\nIdade inválida\n")         
                    continue                            

                

            except:
                print("\nOpção inválida. Favor inserir uma idade válida\n")
                continue                 
                

            genero = 4
            while genero >3:            
                try:                    
                    genero = int(input("\nAgora nos diga o seu genero\n[1] - Masculino\n[2] - Feminino\n[3] - Prefiro não informar\nselecione sua opção: "))        #variável com menu de opções para o usuário
                    if genero == 1:         
                        gender = "Masculino"   
                    elif genero == 2:           
                        gender = "Feminino"   
                    elif genero == 3:               
                        gender = "Não informado"   
                    else:
                        print("\nOpção inválida\n")         
                except:
                    print("\nOpção inválida. Favor escolher uma opção conforme menu.\n")  

            print("\n##########{:^150}##########\n".format("VAMOS INICIAR NOSSA PESQUISA"))  
            
            
            
            q1 = 4
            while q1 >3:        
                try:             
                    q1 = int(input("\nAlgum familiar ou alguém próximo a você veio a óbito devido ao Covid 19?\n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: "))        
                    if q1 >3:           
                        print("\nOpção inválida\n")         
                except:
                    print("\nOpção inválida. Favor escolher uma opção conforme menu.\n")   
            
            q2 =4
            while q2 >3:                         
                try:                                        
                    q2 = int(input("\nVocê tomou todas as doses da vacina contra o Covid 19? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: : "))  
                    if q2 >3:                               
                        print("\nOpção inválida\n")         
                except:
                    print("\nOpção inválida. Favor escolher uma opção conforme menu.\n")            
            
            q3 =4
            while q3 >3:                          
                try:                                        
                    q3 = int(input("\nVocê ainda usa a máscara em locais públicos? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: "))      
                    if q3 >3:                               
                        print("\nOpção inválida\n")         
                except:
                    print("\nOpção inválida. Favor escolher uma opção conforme menu.\n")            
            q4 =4
            while q4 >3:                          
                try:                                       
                    q4 = int(input("\nE alcool ? ainda faz uso dele ? \n[1] - SIM\n[2] - NÃO\n[3] - NÃO SEI\nSelecione sua resposta: "))       
                    if q4 >3:                               
                        print("\nOpção inválida\n")         
                except:
                    print("\nOpção inválida. Favor escolher uma opção conforme menu.\n")        
            
            data = datetime.now()                       
            data = data.strftime(f"%d/%m/%Y")           
            horario = datetime.now()                    
            horario = horario.strftime(f"%H:%M:%S")        

            

            listaQ.append([idade,gender,q1,q2,q3,q4,data,horario]) 
            
            exit = 4
            while exit >=3:            
                try:                    
                    exit = int(input("\nDeseja iniciar outra pesquisa?\n[1] - SIM\n[2] - NÃO\nSelecione sua opção: "))
                    if exit == 1:      
                        system("cls")
                        pass          
                    elif exit == 2:     
                        dflista = pd.DataFrame(listaQ)      
                
                        dflista.to_csv("DadosEntrevistados.csv",  mode = "a" ,index = False, header = False, encoding= "utf-8")   

                    
                        print("\n##########{:^150}##########\n".format("THE YELLOW SQUAD"))  
                        print("\n##########{:^150}##########\n".format("Mergulhando fundo em busca das solucões para os seus problemas"))  
                        
                        
                    else:
                        print("\nOpção inválida\n")         
                except:
                    print("\nOpção inválida. Favor escolher uma opção conforme menu.\n")       
                        


                


        

            
        