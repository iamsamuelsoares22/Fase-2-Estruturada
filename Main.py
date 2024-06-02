from ServicoMenu import *
from ServicoDataBase import *


def main():
    
    #Função para limpar o banco de dados(uso de testes) - OBS: APENAS PARA USO DE TESTES, PARA NÃO ARMAZENAR OS DADOS DE TESTE
    #truncateDataBase(con)
    
    #Contador de manifestações
    qtdManifestacoes = 0 
    
    while True:
        print("\nMenu: \n 1) - Listar das Manifestações \n 2) - Listar Manifestacoes por tipo \n 3) - Criar uma nova Manifestação \n 4) - Exibir quantidade de manifestações \n 5) - Pesquisar uma manifestação por código \n 6) - Excluir uma Manifestação pelo Código \n 7) - Sair do Sistema")

        escolha = int(input("\n Digite sua escolha: "))
        
        if escolha == 1:
            exibirManifestacoes(con, qtdManifestacoes)

        elif escolha == 2:
            exibirManifestacoestipo(con, qtdManifestacoes)
            
        elif escolha == 3:
            qtdManifestacoes += 1
            criarManifestacoes(con)

        elif escolha == 4:
            quantidadeManifestacoes(qtdManifestacoes)

        elif escolha == 5:
            pesquisarManifestacao(con, qtdManifestacoes)

        elif escolha == 6:
            confirmExcluir = excluirManifestacao(con, qtdManifestacoes)
            if confirmExcluir:
                qtdManifestacoes -= 1

        elif escolha == 7:
            break

        else:
            print("\nOpção inválida, tente novamente!")
            
            
# ------------------------- main ------------------------- #
con = iniciarConexao('localhost','root','12345','ouvidoria') #Iniciando conexão com banco de dados
main()
encerrarConexao(con) #Encerrando conexão com banco de dados
