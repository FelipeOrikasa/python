 #PRIMEIRA ETAPA DA CRIAÇÃO DO CÓDIGO
def validar_email(email):
    if '@' not in email or '.' not in email:
        return False

    partes = email.split('@')
    if len(partes) != 2:
        return False

    username, dominio = partes
    if not username or not dominio:
        return False

    if '.' not in dominio[1:]:
        return False

    return True


def validar_nome_usuario(nome_usuario):
    return nome_usuario.isalnum() or '_' in nome_usuario

def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def validar_rg(rg):
    return len(rg) == 9 and rg.isdigit()

def validar_senha(senha):
    if len(senha) < 12:
        return False
    
    num_count = sum(1 for c in senha if c.isdigit())
    upper_count = sum(1 for c in senha if c.isupper())
    lower_count = sum(1 for c in senha if c.islower())
    special_count = sum(1 for c in senha if c in '!@#$%&*()[]{};,.:/\\|')
    
    if num_count < 2 or upper_count < 2 or lower_count < 2 or special_count < 2:
        return False
    
    return True

def autenticar_usuario():
    tipo_login = input("Digite o tipo de seu login (e-mail, nome de usuário, CPF ou RG): ").lower()
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if tipo_login == 'e-mail':
        if validar_email(login):
            print("Login é um e-mail válido.")
        else:
            print("E-mail inválido.")
    elif tipo_login == 'nome de usuário':
        if validar_nome_usuario(login):
            print("Login é um nome de usuário válido.")
        else:
            print("Nome de usuário inválido.")
    elif tipo_login == 'cpf':
        if validar_cpf(login):
            print("Login é um CPF válido.")
        else:
            print("CPF inválido.")
    elif tipo_login == 'rg':
        if validar_rg(login):
            print("Login é um RG válido.")
        else:
            print("RG inválido.")
    else:
        print("Tipo de login inválido.")

    if validar_senha(senha):
        print("Senha é válida.")
    else:
        print("Senha não é válida.")

autenticar_usuario()

#SEGUNDA ETAPA DA CRIAÇÃO DO CÓDIGO

def validar_senha(senha):
    return len(senha) >= 12 and any(c.isdigit() for c in senha) and any(c.isupper() for c in senha) and any(c.islower() for c in senha) and any(c in '!@#$%&*()[]{};,.:/\\|' for c in senha)

def cadastrar_usuario(login_atual, senha_atual):
    login_input = input("Digite seu login atual: ")
    senha_input = input("Digite sua senha atual: ")

    if login_input != login_atual or senha_input != senha_atual:
        print("Login ou senha incorretos. Encerrando...")
        return

    novo_login = input("Digite seu novo login: ")
    nova_senha = input("Digite sua nova senha: ")

    if not validar_senha(nova_senha):
        print("Nova senha inválida. Encerrando...")
        return

    print("Usuário cadastrado com sucesso!")

def menu():
    login_atual = "usuario@exemplo.com"
    senha_atual = "Senha@123"

    print("\nMenu:")
    print("1. Cadastrar novo usuário")
    print("2. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario(login_atual, senha_atual)
    elif opcao == "2":
        print("Encerrando...")
    else:
        print("Opção inválida. Tente novamente.")
        menu()

# Iniciando o menu
menu()

