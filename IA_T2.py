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


#isso aqui precisa estar no database, e é um começo para o prolog
from pyswip import Prolog
prolog = Prolog()
tentou_andar=0
#prolog.consult('database.pl')
#prolog.consult('Mundo_do_Wumpus.pl')


def acha_coordenada_arqueiro():
    prolog.consult('database.pl')
    prolog.consult('Mundo_do_Wumpus.pl')
    local_atual = list(prolog.query("local_arqueiro(X,Y, D)"))
    if len(local_atual) == 0:
        return False, False, False
    x = local_atual[0].get("X")
    y = local_atual[0].get("Y")
    direcao = local_atual[0].get("D")
    return x,y,direcao
print acha_coordenada_arqueiro()
    
def ret_sentiu_brisa_poco(x, y):
    sente_brisa = list(prolog.query("sentiu_brisa_poco(%s,%s)"%(x, y)))
    if len(sente_brisa) == 0:
        return False
    return True

def assert_pode_ter_inimigo(x, y):
    if prolog.query("seguro(%s, %s)"%(x+1,y)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_inimigo(%s,%s)" %(x+1,y))
    if prolog.query("seguro(%s, %s)"%(x-1, y)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_inimigo(%s,%s)" %(x-1, y))
    if prolog.query("seguro(%s, %s)"%(x,y+1)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_inimigo(%s,%s)" %(x,y+1))
    if prolog.query("seguro(%s, %s)"%(x,y-1)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_inimigo(%s,%s)" %(x,y-1))
assert_pode_ter_inimigo(1,1)
def assert_pode_ter_poco(x, y):
    if prolog.query("seguro(%s, %s)"%(x+1,y)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_poco(%s,%s)" %(x+1,y))
    if prolog.query("seguro(%s, %s)"%(x-1, y)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_poco(%s,%s)" %(x-1, y))
    if prolog.query("seguro(%s, %s)"%(x,y+1)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_poco(%s,%s)" %(x,y+1))
    if prolog.query("seguro(%s, %s)"%(x,y-1)) != {}:
        print 'Entrei'
        prolog.assertz("pode_ter_poco(%s,%s)" %(x,y-1))
assert_pode_ter_poco(1,1)
        
def ret_sentiu_fedor(x, y):
    sentiu_fedor = list(prolog.query("sentiu_fedor(%s,%s)"%(x, y)))
    if len(sentiu_fedor) == 0:
        return False
    return True
def ret_sentiu_brilho(x, y):
    sentiu_brilho = list(prolog.query("ouro(%s,%s)"%(x, y)))
    if len(sentiu_brilho) == 0:
        return False
    return True

def detecta_parede(x,y):
    eh_parede = list(prolog.query("parede(%s,%s)" %(x,y)))
    if (len(eh_parede)==0):
            print 'n era parede'
            return False
    return True
            
def faz_percepcao():
    x, y, d = acha_coordenada_arqueiro()
    percebeu = list(prolog.query("sentiu_alguma_coisa(%s, %s)" %(x,y)))
    if len(percebeu) == 0:
        return False, False, False, False
    
    sentiu_brisa = ret_sentiu_brisa_poco(x,y)
    print 'Brisa ', sentiu_brisa 
    sentiu_fedor = ret_sentiu_fedor(x,y)
    print 'Fedor', sentiu_fedor
    sentiu_brilho = ret_sentiu_brilho(x, y)
    print 'Brilho', sentiu_brilho
    return True, sentiu_brisa, sentiu_fedor, sentiu_brilho

def cosulta_database(x, y):
    parede = list(prolog.query("parede(%s,%s)"%(x, y)))
    ouro = list(prolog.query("ouro(%s,%s)"%(x, y)))
    poco = list(prolog.query("poco(%s,%s)"%(x, y)))
    inimigo = list(prolog.query("inimigo(_,_,%s,%s)"%(x, y)))
    return parede, ouro, poco, inimigo
cosulta_database(1,1)
print faz_percepcao()
#pensando no q faço com ele
def agente(x,y, olhando_para):
    posx_atual = x
    posy_atual = y
    virado = olhando_para
    
#só a função q faz o bixo virar ingame
def movimento_virar(olhando_para,novo):
    '''
    Define uma função para modificar o 'campo de visão' do arqueiro.
    Pensando na ordem wasd, w=norte e tal.
    '''
    if novo == 'norte':
        olhando_para = 'norte'
        if novo == 'oeste':
            olhando_para = 'oeste'
            if novo == 'sul':
                olhando_para = 'sul'
                if novo == 'leste':
                    olhando_para = 'leste'
                    
#usa no 'tabuleiro' depois com o python lá em cima      ESSA FUNÇÃO É PRO PYTHON ACHO DEPOIS VAMO PRECISA DE ALGO ASSIM
def arqueiro_anda_py(X,Y,virado_para):
    newy = Y
    newx = X
    if virado_para == 'norte':
        newx = newx-1
    elif virado_para == 'sul':
        newx = newx+1
    elif virado_para == 'oeste':
        newy = newy-1
    elif virado_para == 'leste':
        newy = newy+1
        
    return newx, newy


'''
    checka o que o arqueiro está sentindo onde ele está, checka a direcao para 
    qual o arqueiro está andando, ve se é parede, se for um local seguro ele 
    completa o movimento, se não for ele muda de direção
'''
def munda_local_arqueiro(x, y, xx, yy, direcao):
    if(not detecta_parede(xx,yy)):
        prolog.query("retract(local_arqueiro(%s, %s, %s))" %(x,y,direcao))
        prolog.assertz("local_arqueiro(%s,%s, %s)" %(xx,yy, direcao))
        if ((len(list(prolog.query("visitadas(%s,%s)" %(xx,yy)))))==0):
            prolog.assertz("visitadas(%s,%s)" %(xx,yy))
        descobre_parede_adjacente(xx, yy)
        return True
    return False

def arqueiro_anda_while(x,y,direcao):
    tentou_andar = 0 
    max_repeticao = 1000
    cont_repeticao = 0
    
    while(True):
        percepcao, sentiu_brisa, sentiu_fedor, sentiu_brilho = faz_percepcao()
        if percepcao == True:
            print 'Faz os devidos asserts'
            
        if cont_repeticao >= max_repeticao:
            return 'Repeticao maxima'
        elif tentou_andar > 100:
            return 'Sai tentando andar'

        if (direcao == 'norte'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x-1,y))))>0):
                if munda_local_arqueiro(x,y,x-1, y, direcao) == True:
                    tentou_andar=0
                    print'andou norte'
            else:
                print'else para oeste'
                direcao = 'oeste' #arqueiro_anda(x,y,'oeste')
                tentou_andar=tentou_andar+1
        if(direcao == 'sul'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x+1,y))))>0):
                if munda_local_arqueiro(x,y,x+1, y, direcao) == True:
                    tentou_andar=0
                    print'andou sul'
            else:
                print'else para leste'
                direcao = 'leste' #arqueiro_anda(x,y, 'leste')
                tentou_andar=tentou_andar+1
        if(direcao == 'leste'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x,y+1))))>0):
                if munda_local_arqueiro(x,y,x, y+1, direcao) == True:
                    tentou_andar=0
                    print'andou leste'
            else:
                print'else para norte'
                direcao = 'norte' #arqueiro_anda(x,y,'norte')
                tentou_andar=tentou_andar+1
        if (direcao == 'oeste'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x,y-1))))>0):
                if munda_local_arqueiro(x,y,x, y-1, direcao) == True:
                    tentou_andar=0
                    print'andou oeste'
            else:
                print'else para sult'
                direcao = 'sul' #arqueiro_anda(x,y,'sul')
                tentou_andar=tentou_andar + 1
        cont_repeticao = cont_repeticao + 1
                
def arqueiro_anda(x,y,direcao):
    if tentou_andar > 100:
        return
    if (direcao == 'norte'):
        if (len(list(prolog.query("seguro(%s,%s)" %(x-1,y))))>0):
            if(not detecta_parede(x-1,y)):
                prolog.query("retract(local_arqueiro(%s, %s))" %(x,y))
                prolog.assertz("local_arqueiro(%s,%s)" %(x-1,y))
                if ((len(list(prolog.query("visitadas(%s,%s)" %(x-1,y)))))==0):
                    prolog.assertz("visitadas(%s,%s)" %(x-1,y))
                descobre_parede_adjacente(x-1,y)
                tentou_andar=0
                print'andou norte'
        else:
            print'else para oeste'
            arqueiro_anda(x,y,'oeste')
            tentou_andar=tentou_andar+1
    if(direcao == 'sul'):
        if (len(list(prolog.query("seguro(%s,%s)" %(x+1,y))))>0):
            if(not detecta_parede(x+1,y)):
                prolog.query("retract(local_arqueiro(%s, %s))" %(x,y))
                prolog.assertz("local_arqueiro(%s,%s)" %(x+1,y))
                if ((len(list(prolog.query("visitadas(%s,%s)" %(x+1,y)))))==0):
                    prolog.assertz("visitadas(%s,%s)" %(x+1,y))
                descobre_parede_adjacente(x+1,y)
                tentou_andar=0
                print'andou sul'
        else:
            print'else para leste'
            arqueiro_anda(x,y, 'leste')
            tentou_andar=tentou_andar+1
    if(direcao == 'leste'):
        if (len(list(prolog.query("seguro(%s,%s)" %(x,y+1))))>0):
            if(not detecta_parede(x,y+1)):
                prolog.query("retract(local_arqueiro(%s, %s))" %(x,y))
                prolog.assertz("local_arqueiro(%s,%s)" %(x,y+1))
                if ((len(list(prolog.query("visitadas(%s,%s)" %(x,y+1)))))==0):
                    prolog.assertz("visitadas(%s,%s)" %(x,y+1))
                descobre_parede_adjacente(x,y+1)
                tentou_andar=0
                print'andou leste'
        else:
            print'else para norte'
            arqueiro_anda(x,y,'norte')
            tentou_andar=tentou_andar+1
    if (direcao == 'oeste'):
        if (len(list(prolog.query("seguro(%s,%s)" %(x,y-1))))>0):
            if(not detecta_parede(x,y-1)):
                prolog.query("retract(local_arqueiro(%s, %s))" %(x,y))
                prolog.assertz("local_arqueiro(%s,%s)" %(x,y-1))
                if ((len(list(prolog.query("visitadas(%s,%s)" %(x,y-1)))))==0):
                    prolog.assertz("visitadas(%s,%s)" %(x,y-1))
                descobre_parede_adjacente(x,y-1)
                tentou_andar=0
                print'andou oeste'
        else:
            print'else para sult'
            arqueiro_anda(x,y,'sul')
            tentou_andar=tentou_andar+1
                
            
arqueiro_anda_while(5,6,'sul')
#função usada pela arqueiro_anda
#ela descobre paredes adjacentes ao arqueiro e coloca no db
def descobre_parede_adjacente(x,y):
    if(x==1):
        prolog.assertz("parede(%s, %s)" %(x-1,y))
    elif(x==12):
        prolog.assertz("parede(%s, %s)" %(x+1, y))
    if(y==1):
        prolog.assertz("parede(%s,%s)" %(x,y-1))
    elif(y==12):
        prolog.assertz("parede(%s,%s)"%(x,y+1))


###COPIA A FUNCAO
def percepcoes_ativa(x,y):
    percebeu = list(prolog.query("sentiu_alguma_coisa(%s, %s)" %(x,y)))
    if (len(percebeu)>0):
        print 'tem algo'
        percebeu2 = list(prolog.query("sentiu_brisa_poco(%s,%s)" %(x,y)))
        if len(percebeu2)>0:
            print 'xd2 '
            return 'tem_poco_adjacente'
        percebeu3 = list(prolog.query("sentiu_fedor(%s,%s)" %(x,y)))
        if len(percebeu3)>0:
            print 'tem fedor'
            return 'tem_inimigo_adjacente'
    else:
        eh_parede = list(prolog.query("parede(%s,%s)" %(x+1,y)))
        if (len(eh_parede)==0):
            print 'n era parede 1'
            #em baixo tratar depois de uma forma mais decente
            prolog.query("retract(seguro(%s,%s))" %(x+1,y))
            prolog.assertz("seguro(%s,%s)" %(x+1,y))
        eh_parede2 = list(prolog.query("parede(%s,%s)" %(x-1,y)))
        if (len(eh_parede2)==0):
            print 'n era parede2'
            #em baixo tratar depois de uma forma mais decente
            prolog.query("retract(seguro(%s,%s))" %(x-1,y))
            prolog.assertz("seguro(%s,%s)" %(x-1, y))
        eh_parede3 = list(prolog.query("parede(%s,%s)" %(x,y+1)))
        if (len(eh_parede3)==0):
            print 'n era parede3'
            #em baixo tratar depois de uma forma mais decente
            prolog.query("retract(seguro(%s,%s))" %(x,y-1))
            prolog.assertz("seguro(%s,%s)" %(x,y+1))
        eh_parede4 = list(prolog.query("parede(%s,%s)" %(x,y-1)))
        if (len(eh_parede4)==0):
            print 'n era parede4'
            #em baixo tratar depois de uma forma mais decente
            prolog.query("retract(seguro(%s,%s))" %(x,y-1))
            prolog.assertz("seguro(%s,%s)" %(x,y-1))
        

