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
            return None, None
    elif tipo_login == 'nome de usuário':
        if validar_nome_usuario(login):
            print("Login é um nome de usuário válido.")
        else:
            print("Nome de usuário inválido.")
            return None, None
    elif tipo_login == 'cpf':
        if validar_cpf(login):
            print("Login é um CPF válido.")
        else:
            print("CPF inválido.")
            return None, None
    elif tipo_login == 'rg':
        if validar_rg(login):
            print("Login é um RG válido.")
        else:
            print("RG inválido.")
            return None, None
    else:
        print("Tipo de login inválido.")
        return None, None

    if validar_senha(senha):
        print("Senha é válida.")
        return login, senha
    else:
        print("Senha não é válida.")
        return None, None

def cadastrar_usuario():
    novo_login = input("Digite seu novo login: ")
    nova_senha = input("Digite sua nova senha: ")

    if not validar_senha(nova_senha):
        print("Nova senha inválida. Encerrando o cadastro...")
        return False

    return novo_login, nova_senha

def maior_primo_ate_N(N):
    if N < 2:
        return None

    for num in range(N, 1, -1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            return num

def hash_senha(senha_ord, num_primo):
    return int(senha_ord) % num_primo

def menu():
    while True:  # Loop infinito para manter o menu ativo
        print("\nMenu:")
        print("1. Cadastrar novo usuário")
        print("2. Encontrar maior número primo até N")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Cadastro de novo usuário
            novo_login, nova_senha = cadastrar_usuario()
            if novo_login is not None and nova_senha is not None:
                print("\nUsuário cadastrado com sucesso! Você pode continuar a usar o programa.")
                num_primo = maior_primo_ate_N(100)  # Utiliza um número primo como chave criptográfica
                senha_ord = ''.join(str(ord(c)) for c in nova_senha)
                hash_senha_resultado = hash_senha(senha_ord, num_primo)
                print(f"A senha foi criptografada com sucesso. Hash da senha: {hash_senha_resultado}")

        elif opcao == "2":
            # Autenticação do usuário
            login, senha = autenticar_usuario()
            if login is not None and senha is not None:
                N = int(input("Digite o valor de N (deve ser maior ou igual a 2): "))
                maior_primo = maior_primo_ate_N(N)
                if maior_primo:
                    print(f"O maior número primo até {N} é: {maior_primo}")
                else:
                    print("Não há números primos dentro do intervalo fornecido.")
            else:
                print("Autenticação falhou. Tente novamente.")

        elif opcao == "3":
            print("Encerrando...")
            break  # Encerra o loop e sai do programa

        else:
            print("Opção inválida. Tente novamente.")

# Iniciando o menu
menu()