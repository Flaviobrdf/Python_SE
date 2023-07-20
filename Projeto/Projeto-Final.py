import CadFornecedor



def dados_fornecedor():
    nome = input("Digite o nome do fornecedor: ")
    #telefone = input("Digite o telefone do fornecedor: ")
    while True:
        telefone = validar_telefone()
        email = verificar_email()
        ativo = 1
        return nome, telefone, email, ativo
    

def validar_telefone():
    while True:
        telefone = input("Digite um número: ")
        if telefone.isdigit():  
            numeroDigi = int(telefone) 
            if numeroDigi > 10000000:
                return numeroDigi
            else:
                print("Numero incompleto. Digite o número correto:")
        else:
            print("O valor digitado não é um número. Digite o número correto:")
    
def verificar_email():
    while True:
        email = input("Digite um e-mail: ")
        if "@" in email:
            return email
        else:
            print("E-mail inválido. Certifique-se de incluir o caractere '@'.")
      
#while True:
def menu():
        print("Escolha uma ação:")
        print("1 - Listar Fornecedores Ativos")
        print("2 - Cadastrar Fornecedor")
        print("3 - Buscar Fornecedor")
        print("4 - Inativar Fornecedor")
        print("5 - Listar Fornecedores Inativos")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            CadFornecedor.listar_fornecedores()
            menu()

        elif opcao == "2":
            nome, telefone, email, ativo = dados_fornecedor()
            fornecedor_id = CadFornecedor.cadastrar_fornecedor(nome, telefone, email, ativo)
            print("Fornecedor cadastrado com o ID: {fornecedor_id}")
            menu()

        elif opcao == "3":
            codigo_fornecedor = int(input("Digite o código do fornecedor que deseja visualizar: "))
            CadFornecedor.buscar_fornecedor_por_codigo(codigo_fornecedor)
            menu()

        elif opcao == "4":
            codigo_fornecedor = int(input("Digite o código do fornecedor que deseja inativar: "))
            CadFornecedor.buscar_fornecedor_por_codigo(codigo_fornecedor)
            opcao = input("Deseja INATIVAR fornecedor? (s/n): ")
            if opcao.lower() == 's':
                CadFornecedor.tornar_fornecedor_inativo(codigo_fornecedor)
            menu()

        elif opcao == "5":
                CadFornecedor.listar_fornecedores_inativos()
                menu()

        elif opcao == "6":
            print("Encerrando o programa.")
            
        else:
            print("Opção inválida.")
            menu()

 
if __name__ == "__main__":
    menu()
    