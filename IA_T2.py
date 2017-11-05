def cria_caverna():
    
    
    lista_locais_usados = []
    Tabuleiro = []
    coluna = []
    #esses são para definir as paredes da caverna
    for i in range(14):
        coluna.append(1)
    Tabuleiro.append(coluna.copy())
    coluna = []
    coluna.append(1)
    for i in range (12):
        coluna.append(0)
    coluna.append(1)
    for i in range(12):
        Tabuleiro.append(coluna.copy())
        
    coluna = []
    for i in range(14):
        coluna.append(1)
    Tabuleiro.append(coluna.copy())
    
    #colocar os inimigos, buracos e barras de ouros que valem mais do que dinheiro
    
    
    lista_locais_usados.append([1,1])
    new_local=[]
    

    Tabuleiro[1][1] = -20
    contador=0
    while (contador <15):
        new_local=[]
        col_num = random.randint(1,12)
        lin_num = random.randint(1,12)
        new_local.append(col_num)
        new_local.append(lin_num)
        if new_local not in lista_locais_usados:
            copy_novo = new_local.copy()
            lista_locais_usados.append(copy_novo)
            print(lista_locais_usados)
            Tabuleiro[lin_num][col_num] = contador+100
            contador = contador+1
    
            
    #protótipo de brisa e as paradas
    for i in range(13):
        for j in range(13):
            if Tabuleiro[i][j]>30:
                Tabuleiro[i-1][j] = Tabuleiro[i-1][j]+7
                Tabuleiro[i][j-1] = Tabuleiro[i][j-1]+7
                Tabuleiro[i+1][j] = Tabuleiro[i+1][j]+7
                Tabuleiro[i][j+1] = Tabuleiro[i][j+1]+7
            
            
    for i in Tabuleiro:
        
        print(i)

cria_caverna()
