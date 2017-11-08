import random
def cria_caverna():
    
    
    lista_locais_usados = []
    Tabuleiro = []
    coluna = []
    inimigos_20 = inimigos_50 = gold_ingodo = buracao =0 
    #esses sao para definir as paredes da caverna
    for i in range(14):
        coluna.append(-5000)
    Tabuleiro.append(coluna)
    for i in range(12):
        coluna = []
        coluna.append(-5000)
        for i in range (12):
            coluna.append(0)
        coluna.append(-5000)
        Tabuleiro.append(coluna)
        
        
    coluna = []
    for i in range(14):
        coluna.append(-5000)
    Tabuleiro.append(coluna)
    
    #colocar os inimigos, buracos e barras de ouros que valem mais do que dinheiro
    
    
    lista_locais_usados.append([1,1])
    new_local=[]
    

    Tabuleiro[1][1] = -50
    contador=0
    for i in Tabuleiro:
        
        print i
    #cria os inimigos que dao 20 de dano
    while(inimigos_20 <2):
        new_local=[]
        col_num = random.randint(1,12)
        lin_num = random.randint(1,12)
        new_local.append(col_num)
        new_local.append(lin_num)
        if new_local not in lista_locais_usados:
            copy_novo = new_local
            lista_locais_usados.append(copy_novo)
            print(lista_locais_usados)
            Tabuleiro[lin_num][col_num] = Tabuleiro[lin_num][col_num]+100
            inimigos_20 = inimigos_20+1
    # cria os inimigos que dao 50 de dano
    while(inimigos_50<2):
        new_local=[]
        col_num = random.randint(1,12)
        lin_num = random.randint(1,12)
        new_local.append(col_num)
        new_local.append(lin_num)
        if new_local not in lista_locais_usados:
            copy_novo = new_local
            lista_locais_usados.append(copy_novo)
            print(lista_locais_usados)
            Tabuleiro[lin_num][col_num] = Tabuleiro[lin_num][col_num]+500
            inimigos_50 = inimigos_50+1
    #cria os buracos
    while(buracao<8):
        new_local=[]
        col_num = random.randint(1,12)
        lin_num = random.randint(1,12)
        new_local.append(col_num)
        new_local.append(lin_num)
        if new_local not in lista_locais_usados:
            copy_novo = new_local
            lista_locais_usados.append(copy_novo)
            print(lista_locais_usados)
            Tabuleiro[lin_num][col_num] = Tabuleiro[lin_num][col_num]-300
            buracao = buracao+1
    #cria as barras de ouro que valem mais do que dinheiro
    while(gold_ingodo<3):
        new_local=[]
        col_num = random.randint(1,12)
        lin_num = random.randint(1,12)
        new_local.append(col_num)
        new_local.append(lin_num)
        if new_local not in lista_locais_usados:
            copy_novo = new_local
            lista_locais_usados.append(copy_novo)
            print(lista_locais_usados)
            Tabuleiro[lin_num][col_num] = Tabuleiro[lin_num][col_num]+8000
            gold_ingodo = gold_ingodo+1

    '''
    me ajudou a fazer os bixo e tal, deixa salvo pra ajudar depois
    while (contador <15):
        new_local=[]
        col_num = random.randint(1,12)
        lin_num = random.randint(1,12)
        new_local.append(col_num)
        new_local.append(lin_num)
        if new_local not in lista_locais_usados:
            copy_novo = new_local
            lista_locais_usados.append(copy_novo)
            print(lista_locais_usados)
            Tabuleiro[lin_num][col_num] = Tabuleiro[lin_num][col_num]+100
            contador = contador+1
    
                
    protótipo de brisa e as paradas, me ajudou a colocar as brisas e mal cheiros
    for i in range(13):
        for j in range(13):
            if Tabuleiro[i][j]>30:
                Tabuleiro[i-1][j] = Tabuleiro[i-1][j]+7
                Tabuleiro[i][j-1] = Tabuleiro[i][j-1]+7
                Tabuleiro[i+1][j] = Tabuleiro[i+1][j]+7
                Tabuleiro[i][j+1] = Tabuleiro[i][j+1]+7
    '''        

    for i in range(13):
        for j in range(13):
            if Tabuleiro[i][j] >-400 and Tabuleiro[i][j] < -100:
                Tabuleiro[i-1][j] = Tabuleiro[i-1][j]+13
                Tabuleiro[i][j-1] = Tabuleiro[i][j-1]+13
                Tabuleiro[i+1][j] = Tabuleiro[i+1][j]+13
                Tabuleiro[i][j+1] = Tabuleiro[i][j+1]+13
                
            if Tabuleiro[i][j] >80 and Tabuleiro[i][j] < 700:
                Tabuleiro[i-1][j] = Tabuleiro[i-1][j]+7
                Tabuleiro[i][j-1] = Tabuleiro[i][j-1]+7
                Tabuleiro[i+1][j] = Tabuleiro[i+1][j]+7
                Tabuleiro[i][j+1] = Tabuleiro[i][j+1]+7
                
    for i in Tabuleiro:
        print i
    print 'Buracos:' ,buracao , '\tInimigos com 20 de dano:', inimigos_20, '\tInimigos com 50 de dano:', inimigos_50, '\tGold:', gold_ingodo 

cria_caverna()



#pensando no q faço com ele
def agente(x,y, olhando_para):
    posx_atual = x
    posy_atual = y
    virado = olhando_para
    

def movimento_virar(olhando_para,novo):
    '''
    Define uma função para modificar o 'campo de visão' do arqueiro.
    Pensando na ordem wasd, w=norte e tal.
    '''
    if novo == 'norte':
        olhando_para = [1,0,0,0]
        if novo == 'oeste':
            olhando_para = [0,1,0,0]
            if novo == 'sul':
                olhando_para = [0,0,1,0]
                if novo == 'leste':
                    olhando_para = [0,0,0,1]
