from ServicoDataBase import *



def exibirManifestacoes(con, qtdManifestacoes):
    if qtdManifestacoes != 0:
       selectManifestacoes(con)
    else:
        print("\nNão existe nenhuma manifestação!")
        
        
def exibirManifestacoestipo(con, qtdManifestacoes):
    if qtdManifestacoes != 0:
        while True:
            print("\nQual é o tipo da manifestação que você deseja exibir: \n\n 1) Elogio \n 2) Sugestão \n 3) Reclamação")
            escolha = int(input("\n Digite sua escolha: "))
            
            if escolha == 1:
                tipo = "Elogio"
                break
            
            elif escolha == 2:
                tipo = "Sugestão"
                break
                
            elif escolha == 3:    
                tipo = "Reclamação" 
                break
                
            else: 
                print("Escolha inválida, tente novamente!") 
                
        selectManifestacoesTipos(con, tipo)
        
    else:
        print("\nNão existe nenhuma manifestação!")
        
        
def criarManifestacoes(con):
    # ------ Escolha do tipo da manifestação ------ #
    while True:
        print("\nQual é o tipo da sua manifestação: \n\n 1) Elogio \n 2) Sugestão \n 3) Reclamação")
        escolha = int(input("\n Digite sua escolha: "))
        
        if escolha == 1:
            tipo = "Elogio"
            break
        
        elif escolha == 2:
            tipo = "Sugestão"
            break
            
        elif escolha == 3:    
            tipo = "Reclamação" 
            break
            
        else: 
            print("Escolha inválida, tente novamente!") 
            
    # ------ Armarzenando manifestação ------ #
    manifestacao = str(input("\nDigite sua manisfetação: "))
    insertManifestacao(con, manifestacao, tipo)

    print("\nNova manifestação criada com sucesso!")
    
def quantidadeManifestacoes(qtdManifestacoes):
    print("\nA quantidade de manifestações é " + str(qtdManifestacoes))
    
def pesquisarManifestacao(con, qtdManifestacoes):
    if qtdManifestacoes != 0:
        while True:
            codigo = int(input("\nDigite o código da manisfestação: "))
            manifestacao = selectManifestacaoID(con, str(codigo))
            
            if len(manifestacao) != 0:
                print(f"\nTodas as manifestações com o id '{codigo}':\n\n")
                print(f"{'|Id':<5} {'|Manifestação':<30} {'|Tipo':<10}")
                print("-"*44)
                for (id, manifestacao, tipo) in manifestacao:
                    print(f"{'|'+str(id):<5} {'|'+manifestacao:<30} {'|'+tipo:<10}")
                    
                break

                    
            else:
                print("\nNão existe nenhuma manifestação com esse código!")
                
    else:
        print("\nNão existe nenhuma manifestação!")
        
    
def excluirManifestacao(con, qtdManifestacoes):
    if qtdManifestacoes != 0:
        while True:
            exibirManifestacoes(con, qtdManifestacoes) #Exibir lista para escolha de exclusão do usuario
            excluir = int(input("\nDigite o código(id) da manifestação que deseja excluir: "))
            
            # ------- Verificar se a manifestação existe/excluir ------- #
            manifestacao = selectManifestacaoID(con, str(excluir))
            if len(manifestacao) != 0:
                deleteManifestacao(con, str(excluir))
                print("\nManifestação excluída com sucesso!")
                return True
                
            else:
                print("\nEssa manisfestação não existe, tente novamente!")
    
    else:
        print("\nNão existe nenhuma manifestação!")
        
        
    
    
    
    
    
    
    
    
        
    

    
    