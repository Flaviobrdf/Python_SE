import sqlite3



def criar_tabela():
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS fornecedor01 (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        email TEXT NOT NULL,
                        ativo BOOL NOT NULL
                    )''')
    connection.commit()
    connection.close()

def cadastrar_fornecedor(nome, telefone, email, ativo):
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO fornecedor01 (nome, telefone, email, ativo) VALUES (?, ?, ?, ?)',
                   (nome, telefone, email, ativo))
    #fornecedor_cod = cursor.lastrowid
    connection.commit()
    connection.close()
    print("Fornecedor cadastrado com sucesso!")

def listar_fornecedores():
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM fornecedor01 WHERE ativo = 1')
    fornecedor01 = cursor.fetchall()
    connection.close()

    if fornecedor01:
        print("Lista de Fornecedores:")
        for fornecedor in fornecedor01:
            print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Telefone: {fornecedor[2]}, Email: {fornecedor[3]}, Ativo: {fornecedor[4]}")
    else:
        print("Não há fornecedores cadastrados.")


def listar_fornecedores_inativos():
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM fornecedor01 WHERE ativo = 0')
    fornecedores_inativos = cursor.fetchall()

    connection.close()

    if fornecedores_inativos:
        print("Fornecedores Inativos:")
        for fornecedor in fornecedores_inativos:
            print(f"ID: {fornecedor[0]}, Nome: {fornecedor[1]}, Telefone: {fornecedor[2]}, Email: {fornecedor[3]}, Ativo: {fornecedor[4]}")
    else:
        print("Não há fornecedores inativos.")


def tornar_fornecedor_inativo(codigo_fornecedor):
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()

    # Consulta SQL para atualizar o campo "ativo" do fornecedor para 0 (falso)
    cursor.execute('UPDATE fornecedor01 SET ativo = 0 WHERE id = ?', (codigo_fornecedor,))

    connection.commit()
    connection.close()

    print("Fornecedor com ID {codigo_fornecedor} foi marcado como inativo.")


def buscar_fornecedor_por_codigo(codigo):
    connection = sqlite3.connect('cadastro.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM fornecedor01 WHERE id = ?', (codigo,))
    fornecedor = cursor.fetchone()
    connection.close()

    if fornecedor:
        print(f"Detalhes do Fornecedor (ID: {fornecedor[0]}):")
        print(f"Nome: {fornecedor[1]}")
        print(f"Telefone: {fornecedor[2]}")
        print(f"Email: {fornecedor[3]}")
        print(f"Ativo: {fornecedor[4]}")
    else:
        print("Fornecedor não encontrado.")

if __name__ == "__main__":
    criar_tabela()