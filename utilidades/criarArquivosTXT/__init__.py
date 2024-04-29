def criar_arquivo(nome):
    '''

    @param nome: Deve Passar o nome do arquivo
    @return: Cria um arquivo txt com o nome escolhido

    '''
    try:
        arquivo = nome
        arquivo = open(f"{arquivo}.txt","r+")
        arquivo.close()
        if arquivo == FileNotFoundError:
            print("Arquivo não encontrado")
    except FileNotFoundError:
            arquivo = open(f"{arquivo}.txt", "w+")
            print("Arquivo criado com sucesso")
            arquivo.close()
