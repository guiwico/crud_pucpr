import json

# Função para mostrar o menu principal.
def mostrar_menu_principal():
    print("---- Menu Principal ----")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(9) Sair.")

# Função para mostrar o menu de operações.
def mostrar_menu_operacoes():
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar o menu principal.")

# Função para navegar nas operações de estudantes e professores.
def navegacao_menu_operacoes(nome_arquivo, escolha_pricipal):
    while True:
            print(f"***** [{escolha_principal}] *****\n Menu de operações")
            mostrar_menu_operacoes()
            opcao_menu_operacoes = str(input("Informe a opção desejada: ")).lower()
            escolha_operacoes = converter_escolha_operacoes(opcao_menu_operacoes)

            print(f"===== {escolha_operacoes} =====")

            if escolha_operacoes == "INCLUINDO":
                incluir_nome(nome_arquivo)
            elif escolha_operacoes == "LISTANDO":
                listar_nome(nome_arquivo)
            elif escolha_operacoes == "ATUALIZANDO":
                atualizar_nome(nome_arquivo)
            elif escolha_operacoes == "EXCLUINDO":
                remover_nome(nome_arquivo)
            elif escolha_operacoes == "VOLTANDO":
                break
            else:
                print("Escolha uma opção válida.")


# Função para transformar as opções do menu principal
def converter_escolha_principal(opcao_menu_principal):
    escolha_principal = ""  # Condição vazia que irá receber o novo valor.
    if opcao_menu_principal in ["1", "gerenciar estudantes", "estudantes"]:
        escolha_principal = "ESTUDANTES"
    elif opcao_menu_principal in ["2", "gerenciar professores", "professores", "Professores"]:
        escolha_principal = "PROFESSORES"
    elif opcao_menu_principal in ["3", "gerenciar disciplinas", "disciplinas", "Disciplinas"]:
        escolha_principal = "DISCIPLINAS"
    elif opcao_menu_principal in ["4", "gerenciar turmas", "turmas", "Turmas"]:
        escolha_principal = "TURMAS"
    elif opcao_menu_principal in ["5", "gerenciar matrículas", "matrículas", "Matrículas"]:
        escolha_principal = "MATRICULAS"
    elif opcao_menu_principal in ["9", "sair"]:
        escolha_principal = "SAIR"

    return escolha_principal

# Função para converter as opções do menu de operações
def converter_escolha_operacoes(opcao_menu_operacoes):
    escolha_operacoes = ""
    if opcao_menu_operacoes in ["1", "incluir", "Incluir"]:
        escolha_operacoes = "INCLUINDO"
    elif opcao_menu_operacoes in ["2", "Listar", "listar"]:
        escolha_operacoes = "LISTANDO"
    elif opcao_menu_operacoes in ["3", "Atualizar", "atualizar"]:
        escolha_operacoes = "ATUALIZANDO"
    elif opcao_menu_operacoes in ["4", "Excluir", "excluir"]:
        escolha_operacoes = "EXCLUINDO"
    elif opcao_menu_operacoes in ["9", "Voltar", "voltar"]:
        escolha_operacoes = "VOLTANDO"

    return escolha_operacoes

# Função para incluir um novo nome na lista selecionada, podendo ser usada para estudantes e professores.
def incluir_nome(nome_arquivo):
    dados = {}
    checar_codigo_e_retornar(nome_arquivo)
    codigo = checar_codigo_e_retornar(nome_arquivo)
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    dados["codigo"] = codigo
    dados["nome"] = nome
    dados["cpf"] = cpf
    lista = ler_arquivo(nome_arquivo)
    lista.append(dados)
    salvar_arquivo(lista, nome_arquivo)

# Função pra incluir disciplina.
def incluir_disciplina(nome_arquivo):
    try:
        lista = ler_arquivo(nome_arquivo)
    except TypeError:
        return []
    dados = {}        
    codigo = checar_codigo_e_retornar(nome_arquivo) 
    disciplina = input("Digite o nome na disciplina: ")
    dados['codigo'] = codigo
    dados['nome'] = disciplina
    lista.append(dados)
    salvar_arquivo(lista, nome_arquivo)

# Função para incluir nova turma.
def incluir_turma(nome_arquivo):
    dados = {}
    codigo = checar_codigo_e_retornar(nome_arquivo)
    print("Código do professor.")
    codigo_professor  = checar_codigo_valido(cadastro_professores)
    print("Código da disciplina.")
    codigo_disciplina = checar_codigo_valido(cadastro_disciplinas)
    dados['codigo'] = codigo
    dados['codigo do professor'] = codigo_professor
    dados['codigo da disciplina'] = codigo_disciplina
    lista_turma = ler_arquivo(nome_arquivo)
    lista_turma.append(dados)
    salvar_arquivo(lista_turma, nome_arquivo)

# Função para incluir matrículas:
def incluir_matriculas(nome_arquivo):
    matriculas = ler_arquivo(nome_arquivo)
    dados = {}
    print("Código da turma.")
    codigo_turma = checar_codigo_valido(cadastro_turmas)
    print("Código do estudante.")
    codigo_estudante = checar_codigo_valido(cadastro_estudantes)
    dados['codigo'] = codigo_turma
    dados['codigo do estudante'] = codigo_estudante
    matriculas.append(dados)
    salvar_arquivo(matriculas, nome_arquivo)


# Função para listar os cadastros de uma lista.
def listar_nome(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    if len(lista) == 0:
        print("A lista está vazia.")
    else:
        for i in range(len(lista)):
            print(lista[i])
        while True:
            retornar_menu_operacoes = input("\nRetornar para menu anterior? (s) \n> ").lower()
            if retornar_menu_operacoes in ["s"]:
                break
            print("\nDigite uma opção válida.")

# Função para atualizar um cadastro de estudante ou professor.
def atualizar_nome(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    cod_editar = int(input("Qual o código do cadastro que deseja editar? \n> "))
    for i, nome in enumerate(lista):
        if nome["codigo"] == cod_editar:
            while True:
                confirmar_edicao = input(f"Você deseja editar o cadastro de {nome['codigo']} - {nome['nome']}? (s/n) \n> ").lower()
                if confirmar_edicao in ["s", "n"]:
                    break
                print("Digite uma opção válida.")
            if confirmar_edicao == "s":
                # Abre uma edição automatica pro cadastro.
                nome["codigo"] = int(input("Digite o novo código: "))
                nome["nome"] = input("Digite o novo nome: ")
                nome["cpf"] = input("Digite o novo CPF: ")
                salvar_arquivo(lista, nome_arquivo)
                print(f"Cadastro atualizado. Os dados são {nome['codigo']} - {nome['nome']}, CPF nº {nome['cpf']}.")
            else:
                print("Cadastro não editado voltando para menu anterior.")

# Função para atualizar disciplinas
def atualizar_disciplina(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    cod_editar = int(input("Qual o código da disciplina que deseja editar? \n> "))
    for i, disciplina in enumerate(lista):
        if disciplina["codigo"] == cod_editar:
            while True:
                confirmar_edicao = input(f"Você deseja editar o cadastro de {disciplina['codigo']} - {disciplina['nome']}? (s/n) \n> ").lower()
                if confirmar_edicao in ["s", "n"]:
                    break
                print("Digite uma opção válida.")
            if confirmar_edicao == "s":
                # Abre uma edição automatica pro cadastro.
                disciplina["codigo"] = int(input("Digite o novo código: "))
                disciplina["nome"] = input("Digite o novo nome da disciplina: ")
                salvar_arquivo(lista, nome_arquivo)
                print(f"Cadastro atualizado. Os dados são {disciplina['codigo']} - {disciplina['nome']}.")
            else:
                print("Disciplina não editada voltando para menu anterior.")

# Função pra atualizar dados da turma.
def atualizar_turma(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    cod_editar = int(input("Qual o código da turma que deseja editar? \n> "))
    for i, nome in enumerate(lista):
        if nome["codigo"] == cod_editar:
            while True:
                confirmar_edicao = input(f"Você deseja editar o cadastro da turma {nome['codigo']}? (s/n) \n> ").lower()
                if confirmar_edicao in ["s", "n"]:
                    break
                print("Digite uma opção válida.")
            if confirmar_edicao == "s":
                # Abre uma edição automatica pro cadastro.
                nome["codigo"] = int(input("Digite o novo código: "))
                nome["codigo do professor"] = int(input("Digite o novo ou repita o código do professor: "))
                nome["codigo da disciplina"] = int(input("Digite o novo ou repita o código da disciplina: "))
                salvar_arquivo(lista, nome_arquivo)
                print(f"Cadastro atualizado. Os dados são:\n Código da turma: {nome['codigo']}\n Código do professor: {nome['codigo do professor']}\n Código da disciplina: {nome['codigo da disciplina']}.")
            else:
                print("Disciplina não editada voltando para menu anterior.")

# Função para atualizar dados da matrícula.
def atualizar_matricula(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    cod_editar = int(input("Qual o código da matricula que deseja editar? \n> "))
    for i, nome in enumerate(lista):
        if nome["codigo"] == cod_editar:
            while True:
                confirmar_edicao = input(
                    f"Você deseja editar a matricula {nome['codigo']}? (s/n) \n> ").lower()
                if confirmar_edicao in ["s", "n"]:
                    break
                print("Digite uma opção válida.")
            if confirmar_edicao == "s":
                # Abre uma edição automatica pro cadastro.
                nome["codigo"] = int(input("Digite o novo código da turma: "))
                nome["codigo do estudante"] = input("Digite o novo codigo do estudante: ")
                salvar_arquivo(lista, nome_arquivo)
                print(f"Cadastro atualizado. Os dados são {nome['codigo']} - {nome['codigo do estudante']}.")
            else:
                print("Disciplina não editada voltando para menu anterior.")

# Função para remover um cadastro.
def remover_nome(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    cod_excluir = int(input("Qual o código do cadastro que deseja excluir? \n> "))
    cod_encontrado = False

    for i, nome in enumerate(lista):
        if nome["codigo"] == cod_excluir:
            while True:
                confirmacao_exclusao = input(
                    f"Você deseja excluir o {nome['codigo']} - {nome['nome']}? (s/n) \n> ")
                if confirmacao_exclusao in ["s", "n"]:
                    break
                print("Digite uma opção válida.")
            if confirmacao_exclusao == "s":
                lista.pop(i)
                salvar_arquivo(lista, nome_arquivo)
                print(f"O cadastro de {nome['nome']} foi excluído.")
            else:
                print("Cadastro não excluído. Voltando para menu anterior.")

            # Modifica a variavel temporaria para quebrar o while e não mostrar a mensagem abaixo "digite um codigo valido"
            cod_encontrado = True
            break

    if not cod_encontrado:
        print("Digite um código válido.")

# Função pra remover matriculas, turmas e disciplinas
def remover_nao_pessoas(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    cod_excluir = int(input("Qual o código do aluno que deseja excluir? \n> "))
    cod_encontrado = False

    for i, nome in enumerate(lista):
        if nome['codigo'] == cod_excluir:
            while True:
                confirmacao_exclusao = input(
                    f"Você deseja excluir o {nome['codigo']}? (s/n) \n> ")
                if confirmacao_exclusao in ["s", "n"]:
                    break
                print("Digite uma opção válida.")
            if confirmacao_exclusao == "s":
                lista.pop(i)
                salvar_arquivo(lista, nome_arquivo)
                print(f"O cadastro {nome['codigo']} foi excluído.")
            else:
                print("Aluno não excluído. Voltando para menu anterior.")

            # Modifica a variavel temporaria para quebrar o while e não mostrar a mensagem abaixo "digite um codigo valido"
            cod_encontrado = True
            break

    if not cod_encontrado:
        print("Digite um código válido.")

# Função para salvar a lista no arquivo json. 
def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False)

# Função para ler o arquivo json e devolver uma lista.
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as f:
            lista_aberta = json.load(f)

            return lista_aberta
    except:
        return []

# Função para checar se o código escrito já foi usado.
def checar_codigo_e_retornar(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    while True:
        try:
            codigo = int(input("Digite o código: "))
            if any(item["codigo"] == codigo for item in lista):
                print("Este código já está em uso.")
            else:
                return codigo
        except ValueError:
            print("Digite um número válido.")
# Checar se o código existe e pode ser usado.
def checar_codigo_valido(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    while True:
        try:
            codigo = int(input("Digite o código: "))
            if any(item["codigo"] == codigo for item in lista):
                return codigo
            else:
                print("Nenhum cadastro encontrado com este código.")
        except ValueError:
            print("Digite um número válido.")

# Colocar os arquivos json em variaveis para serem usadas abaixo.
cadastro_estudantes = "cadastro_estudantes.json"
cadastro_professores = "cadastro_professores.json"
cadastro_disciplinas = "cadastro_disciplinas.json"
cadastro_turmas = "cadastro_turmas.json"
cadastro_matriculas = "cadastro_matriculas.json"

while True:
    mostrar_menu_principal()
    opcao_menu_principal = str(input("Informe a opção desejada: ")).lower()
    escolha_principal = converter_escolha_principal(opcao_menu_principal)
    # Retorna a escolha principal automaticamente indicando a opção escolhida.

    if escolha_principal == "ESTUDANTES":
        navegacao_menu_operacoes(cadastro_estudantes, escolha_principal)

    elif escolha_principal == "PROFESSORES":
        navegacao_menu_operacoes(cadastro_professores, escolha_principal)
        
    elif escolha_principal == "DISCIPLINAS":
        while True:
            print(f"***** [{escolha_principal}] *****\n Menu de operações")
            mostrar_menu_operacoes()
            opcao_menu_operacoes = str(
                input("Informe a opção desejada: ")).lower()
            escolha_operacoes = converter_escolha_operacoes(opcao_menu_operacoes)

            print(f"===== {escolha_operacoes} =====")

            if escolha_operacoes == "INCLUINDO":
                incluir_disciplina(cadastro_disciplinas)
            elif escolha_operacoes == "LISTANDO":
                listar_nome(cadastro_disciplinas)
            elif escolha_operacoes == "ATUALIZANDO":
                atualizar_disciplina(cadastro_disciplinas)
            elif escolha_operacoes == "EXCLUINDO":
                remover_nao_pessoas(cadastro_disciplinas)
            elif escolha_operacoes == "VOLTANDO":
                break
            else:
                print("Escolha uma opção válida.")
        
    elif escolha_principal == "TURMAS":
        while True:
            print(f"***** [{escolha_principal}] *****\n Menu de operações")
            mostrar_menu_operacoes()
            opcao_menu_operacoes = str(
                input("Informe a opção desejada: ")).lower()
            escolha_operacoes = converter_escolha_operacoes(opcao_menu_operacoes)

            print(f"===== {escolha_operacoes} =====")

            if escolha_operacoes == "INCLUINDO":
                incluir_turma(cadastro_turmas)
            elif escolha_operacoes == "LISTANDO":
                listar_nome(cadastro_turmas)
            elif escolha_operacoes == "ATUALIZANDO":
                atualizar_turma(cadastro_turmas)
            elif escolha_operacoes == "EXCLUINDO":
                remover_nao_pessoas(cadastro_turmas)
            elif escolha_operacoes == "VOLTANDO":
                break
            else:
                print("Escolha uma opção válida.")
        
    elif escolha_principal == "MATRICULAS":
        while True:
            print(f"***** [{escolha_principal}] *****\n Menu de operações")
            mostrar_menu_operacoes()
            opcao_menu_operacoes = str(
                input("Informe a opção desejada: ")).lower()
            escolha_operacoes = converter_escolha_operacoes(opcao_menu_operacoes)

            print(f"===== {escolha_operacoes} =====")
            
            if escolha_operacoes == "INCLUINDO":
                incluir_matriculas(cadastro_matriculas)
            elif escolha_operacoes == "LISTANDO":
                listar_nome(cadastro_matriculas)
            elif escolha_operacoes == "ATUALIZANDO":
                atualizar_matricula(cadastro_matriculas)
            elif escolha_operacoes == "EXCLUINDO":
                remover_nao_pessoas(cadastro_matriculas)
            elif escolha_operacoes == "VOLTANDO":
                break
            else:
                print("Escolha uma opção válida.")
        
    elif escolha_principal == "SAIR":
        print("Saindo do sistema.")
        break
    else:
        print("Escolha uma opção válida.")