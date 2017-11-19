# -*- coding: utf-8 -*-
import random


from aux_pyswip import py_assert, py_retract, preenche_database
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
    preenche_database(Tabuleiro)
cria_caverna()

#isso aqui precisa estar no database, e é um começo para o prolog]
from pyswip import Prolog
prolog = Prolog()
tentou_andar=0
prolog.consult('Mundo_do_Wumpus.pl')
prolog.consult('database.pl')

def caiu_poco():
    prolog.consult('database.pl') 
    x, y, direcao = acha_coordenada_arqueiro()
    print x, y
    poco = list(prolog.query('poco(%s,%s)'%(x,y)))
    if len(poco) == 0:
        return False
    atualiza_ponto(-1000)
    return True

def atualiza_energia(energia):
    prolog.consult('database.pl')
    energias = list(prolog.query('energia(E)'))
    if len(energias) == 0:
        py_assert('database.pl', 'energia(%s).' %(energia))
        return False
    py_retract('database.pl', 'energia(%s).' %(energias[0].get('E')))
    energia_nova = energias[0].get('E') + energia
    py_assert('database.pl', 'energia(%s).' %(energia_nova))
    
def atualiza_ponto(ponto):
    prolog.consult('database.pl')
    pontuacao = list(prolog.query('pontuacao(P)'))
    if len(pontuacao) == 0:
        py_assert('database.pl', 'pontuacao(%s).' %(ponto))
        return False
    py_retract('database.pl', 'pontuacao(%s).' %(pontuacao[0].get('P')))
    pontos = pontuacao[0].get('P') + ponto
    py_assert('database.pl', 'pontuacao(%s).' %(pontos))
    
def pega_ouro():
    prolog.consult('database.pl') 
    x, y, direcao = acha_coordenada_arqueiro()
    ouro = list(prolog.query('ouro(%s,%s)'%(x,y)))
    print len(ouro)
    if len(ouro) == 0:
        return False
    py_retract('database.pl', 'ouro(%s,%s).' %(x, y))
    atualiza_ponto(1000)
    return True

def direcao_certa(x, y, xx, yy, direcao):
    if direcao == 'norte':
        if xx < x:
            return True
        return False
    elif direcao == 'sul':
        if xx > x:
            return True
        return False
    elif direcao == 'oeste':
        if yy < y:
            return True
        return False
    elif direcao == 'leste':
        if yy > y:
            return True
        return False
def inimigo_dano(x, y):
    prolog.consult('database.pl')
    inimigo = list(prolog.query('inimigo(D,V,%s,%s)'%(x,y)))
    atualiza_ponto((-1)*inimigo[0].get('D'))
    
def faz_dano(x, y, dano):
    prolog.consult('database.pl')
    inimigo = list(prolog.query('inimigo(D,V,%s,%s)'%(x,y)))
    vida_inimigo = inimigo[0].get('V') - dano
    print vida_inimigo
    py_retract('database.pl','inimigo(%s,%s,%s,%s).'%(inimigo[0].get('D'),inimigo[0].get('V'),x,y) )
    if vida_inimigo <= 0:
        return True
    py_assert('database.pl', 'inimigo(%s,%s,%s,%s).'%(inimigo[0].get('D'),vida_inimigo,x,y) )
    return False

def atira():
    atualiza_ponto(-10)
    prolog.consult('database.pl')
    x, y, direcao = acha_coordenada_arqueiro()
    inimigo = list(prolog.query("inimigo(D, V, X,Y)"))
    for i in inimigo:
        if x == i.get('X') and y == i.get('Y'):
            print 'Mesma coordenada na funcao de atirar'
            return
        elif x == i.get('X') or x == i.get('Y'):     
            if direcao_certa(x, y, i.get('X'), i.get('Y'), direcao) == True:
                print 'Entrou'
                faz_dano(i.get('X'), i.get('Y'), random.randint(20,50))
    return False

def acha_coordenada_arqueiro():
    prolog.consult('database.pl')
    local_atual = list(prolog.query("local_arqueiro(X,Y, D)"))
    if len(local_atual) == 0:
        return False, False, False
    x = local_atual[0].get("X")
    y = local_atual[0].get("Y")
    direcao = local_atual[0].get("D")
    return x,y,direcao
#print acha_coordenada_arqueiro()
    
def ret_sentiu_brisa_poco(x, y):
    prolog.consult('database.pl')
    sente_brisa = list(prolog.query("sentiu_brisa_poco(%s,%s)"%(x, y)))
    if len(sente_brisa) == 0:
        return False
    return True

def assert_pode_ter_inimigo(x, y):
    prolog.consult('database.pl')
    if prolog.query("seguro(%s, %s)"%(x+1,y)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_inimigo(%s,%s)." %(x+1,y))
    if prolog.query("seguro(%s, %s)"%(x-1, y)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_inimigo(%s,%s)." %(x-1, y))
    if prolog.query("seguro(%s, %s)"%(x,y+1)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_inimigo(%s,%s)." %(x,y+1))
    if prolog.query("seguro(%s, %s)"%(x,y-1)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_inimigo(%s,%s)." %(x,y-1))
#assert_pode_ter_inimigo(1,1)


def assert_pode_ter_poco(x, y):
    prolog.consult('database.pl')
    if prolog.query("seguro(%s, %s)"%(x+1,y)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_poco(%s,%s)." %(x+1,y))
    if prolog.query("seguro(%s, %s)"%(x-1, y)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_poco(%s,%s)." %(x-1, y))
    if prolog.query("seguro(%s, %s)"%(x,y+1)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_poco(%s,%s)." %(x,y+1))
    if prolog.query("seguro(%s, %s)"%(x,y-1)) != {}:
        #print 'Entrei'
        py_assert('database.pl',"pode_ter_poco(%s,%s)." %(x,y-1))
#assert_pode_ter_poco(1,1)
        
def ret_sentiu_fedor(x, y):
    prolog.consult('database.pl')
    sentiu_fedor = list(prolog.query("sentiu_fedor(%s,%s)"%(x, y)))
    if len(sentiu_fedor) == 0:
        return False
    return True

def ret_sentiu_brilho(x, y):
    prolog.consult('database.pl')
    sentiu_brilho = list(prolog.query("ouro(%s,%s)"%(x, y)))
    if len(sentiu_brilho) == 0:
        return False
    return True

def detecta_parede(x,y):
    prolog.consult('database.pl')
    eh_parede = list(prolog.query("parede(%s,%s)" %(x,y)))
    if (len(eh_parede)==0):
            print 'n era parede'
            return False   
    return True
            
def faz_percepcao():
    'entrou na percepcao'
    prolog.consult('database.pl')
    x, y, d = acha_coordenada_arqueiro()
    percebeu = list(prolog.query("sentiu_alguma_coisa(%s, %s)" %(x,y)))
    if len(percebeu) == 0:
        #print 'percebeu nada' ,x ,y
        return False, False, False, False
    print 'PERCEBEU ALGUMA COISA NESSA PORRA'
    sentiu_brisa = ret_sentiu_brisa_poco(x,y)
    #print 'Brisa ', sentiu_brisa 
    sentiu_fedor = ret_sentiu_fedor(x,y)
    #print 'Fedor', sentiu_fedor
    sentiu_brilho = ret_sentiu_brilho(x, y)
    #print 'Brilho', sentiu_brilho
    return True, sentiu_brisa, sentiu_fedor, sentiu_brilho

def cosulta_database(x, y):
    prolog.consult('database.pl')
    parede = list(prolog.query("parede(%s,%s)"%(x, y)))
    ouro = list(prolog.query("ouro(%s,%s)"%(x, y)))
    poco = list(prolog.query("poco(%s,%s)"%(x, y)))
    inimigo = list(prolog.query("inimigo(_,_,%s,%s)"%(x, y)))
    return parede, ouro, poco, inimigo

#cosulta_database(1,1)
#print faz_percepcao()
#pensando no q faço com ele
def agente(x,y, olhando_para):
    posx_atual = x
    posy_atual = y
    virado = olhando_para
    
#só a função q faz o bixo virar ingame
def movimento_virar(olhando_para):
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
    return novo
                    
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
        py_retract('database.pl',"local_arqueiro")
        py_assert('database.pl',"local_arqueiro(%s,%s,%s)." %(xx,yy, direcao))
        prolog.consult('database.pl')
        if ((len(list(prolog.query("visitadas(%s,%s)" %(xx,yy)))))==0):
            py_assert('database.pl',"visitadas(%s,%s)." %(xx,yy))
        descobre_parede_adjacente(xx, yy)
        return True
    return False


'''
  ********************
  Função de andar 
  Pensei em chamar uma vez para cada passo, cada vez ele checka o adjacente que ta virado se é seguro/parede e tenta andar.
  
  
  ********************
 
'''
def arqueiro_anda_while():
    rand_direcao = 1
    tentou_andar = 0 
    max_repeticao = 4
    cont_repeticao = 0

    x,y,direcao = acha_coordenada_arqueiro()
    #print list(prolog.query("seguro(2,1)")), "(2,1) seguro acho"
    #print list(prolog.query("seguro(1,2)")) , "(1,2) seguro acho"
    percepcao, sentiu_brisa, sentiu_fedor, sentiu_brilho = faz_percepcao()
    if percepcao == False:
        print 'Faz os devidos asserts'
        #ADJACENTES SÃO SEGUROS PARA ANDAR DESDE QUE NÃO SEJAM PAREDE
        if (not detecta_parede(x+1,y)):
            py_assert('database.pl',"seguro(%s,%s)."%(x+1,y))

        if (not detecta_parede(x-1,y)):
            py_assert('database.pl',"seguro(%s,%s)."%(x-1,y))

        if (not detecta_parede(x,y+1)):
            py_assert('database.pl',"seguro(%s,%s)."%(x,y+1))

        if (not detecta_parede(x,y-1)):
            py_assert('database.pl',"seguro(%s,%s)."%(x,y-1))
            
    turn = 0
    while(True):

        print x,'   ', y,  'sao as coord' , direcao , 'é a direcao'
        #if cont_repeticao >= max_repeticao:
            #return 'Repeticao maxima'
        #elif tentou_andar > 3:
            #return 'Sai tentando andar'
        prolog.consult('database.pl')
        #print list(prolog.query("adjacente(1,2, X,Y)"))
        #print list(prolog.query("seguro(X,Y)")), 'lista segura'
        #print list(prolog.query("explorar(1,Y)")), 'explora'
        if (direcao == 'norte'): #checka a direção 
            if (len(list(prolog.query("seguro(%s,%s)" %(x-1,y))))>0):  #ve se é seguro andar para a direção
                if (len(list(prolog.query("visitadas(%s,%s)" %(x-1,y))))>0): #checka se já visitou o local em que  tenta andar
                    turn = turn + 1                                            #CASO SIM ELE GIRA
                    print 'ja passei aqui norte' , turn
                    
                    '''
                        /\ tenta andar -> já visitou /\   turn +1 = 1
                        < tenta anda -> já visitou/dangerous < turn +1 =2
                        \/ tenta anda -> já visitou/dangerous \/ turn +1 =3
                        > tenta anda -> ja visitou/dangerous > turn+1 = 4
                        /\ >>>>>>>>>>>> 5 TEM QUE IR
                    '''
                    if turn > 4:#
                        if munda_local_arqueiro(x,y,x-1, y, direcao) == True:
                            tentou_andar=0
                            turn = 0
                            print'andou norte depois de girar peão do baú\n'
                            return True
                    else:
                        rand_direcao = random.randint(1,2)
                        if rand_direcao == 1:
                            print'virou oeste', turn
                            direcao = 'oeste' #arqueiro_anda(x,y,'oeste')
                        else:
                            print'virou leste', turn
                            direcao = 'leste' #arqueiro_anda(x,y,'leste')
                else:
                    if munda_local_arqueiro(x,y,x-1, y, direcao) == True:
                        tentou_andar=0
                        turn = 0
                        print  turn ,'andou norte\n'
                        return True
            else:
                rand_direcao = random.randint(1,2)
                tentou_andar=tentou_andar+1
                if rand_direcao == 1:
                    print'virou oeste', turn+1
                    turn = turn + 1
                    direcao = 'oeste' #arqueiro_anda(x,y,'oeste')
                else:
                    print'virou leste', turn+1
                    turn = turn + 1
                    direcao = 'leste' #arqueiro_anda(x,y,'leste')
                    
                
        elif(direcao == 'sul'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x+1,y))))>0):
                if (len(list(prolog.query("visitadas(%s,%s)" %(x+1,y))))>0):
                    print 'ja passei aqui sul' , turn
                    turn = turn + 1
                    if turn > 4:
                        if munda_local_arqueiro(x,y,x+1, y, direcao) == True:
                            tentou_andar=0
                            print'andou sul depois de girar peão do baú\n'
                            return True
                    else:
                        rand_direcao = random.randint(1,2)
                        if rand_direcao == 1:
                            print'virou leste', turn
                            direcao = 'leste' #arqueiro_anda(x,y,'leste')
                        else:
                            print 'virou oeste', turn
                            direcao = 'oeste'#arqueiro_anda(x,y,'oeste')
                        
                else:
                        if munda_local_arqueiro(x,y,x+1, y, direcao) == True:
                            tentou_andar=0
                            turn = 0
                            print'andou sul\n'
                            return True
                        
            else:
                rand_direcao = random.randint(1,2)
                if rand_direcao == 1:
                    print'virou leste', turn+1
                    turn = turn + 1
                    direcao = 'leste' #arqueiro_anda(x,y, 'leste')
                    tentou_andar=tentou_andar+1
                else:
                    print'virou oeste', turn+1
                    turn = turn + 1
                    direcao = 'oeste' #arqueiro_anda(x,y, 'leste')
                    tentou_andar=tentou_andar+1
                
        elif(direcao == 'leste'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x,y+1))))>0):
                if (len(list(prolog.query("visitadas(%s,%s)" %(x,y+1))))>0):
                    print 'ja passei aqui leste' , turn
                    turn = turn + 1
                    if turn > 4:
                        if munda_local_arqueiro(x,y,x, y+1, direcao) == True:
                            tentou_andar=0
                            turn =0
                            print'andou leste depois de girar peão do baú\n'
                            return True
                    else:
                        rand_direcao = random.randint(1,2)
                        if rand_direcao == 1:
                            print 'virou norte', turn
                            direcao = 'norte'
                        else:
                            print 'virou sul', turn
                            direcao = 'sul'
                
                else:
                    if munda_local_arqueiro(x,y,x, y+1, direcao) == True:
                        tentou_andar=0
                        turn =0
                        print'andou leste\n'
                        return True
                
            else:
                rand_direcao = random.randint(1,2)
                if rand_direcao == 1:
                    print'virou norte', turn+1
                    turn = turn + 1
                    direcao = 'norte'  #arqueiro_anda(x,y,'norte')
                    tentou_andar=tentou_andar+1
                else:
                    print'virou sul', turn+1
                    turn = turn + 1
                    direcao = 'sul'  #arqueiro_anda(x,y,'norte')
                    tentou_andar=tentou_andar+1
                
        elif (direcao == 'oeste'):
            if (len(list(prolog.query("seguro(%s,%s)" %(x,y-1))))>0):
                if (len(list(prolog.query("visitadas(%s,%s)" %(x,y-1))))>0):
                    print 'ja passei aqui oeste' , turn
                    turn = turn + 1
                    if turn > 4:
                        if munda_local_arqueiro(x,y,x, y-1, direcao) == True:
                            tentou_andar=0
                            turn = 0
                            print'andou oeste'
                            print '\n'
                            return True
                    else:
                        rand_direcao = random.randint(1,2)
                        if rand_direcao == 1:
                            print 'virou sul'
                            direcao = 'sul'
                        else:
                            print 'virou norte'
                            direcao = 'norte'
                else:
                    if munda_local_arqueiro(x,y,x, y-1, direcao) == True:
                        tentou_andar=0
                        turn = 0
                        print'andou oeste'
                        print '\n'
                        return True
            else:
                rand_direcao = random.randint(1,2)
                if rand_direcao == 1:
                    print'virou sul', turn+1
                    turn = turn + 1
                    direcao = 'sul'     #arqueiro_anda(x,y,'sul')
                    tentou_andar=tentou_andar + 1
                else:
                    print'virou norte', turn+1
                    turn = turn + 1
                    direcao = 'norte'     #arqueiro_anda(x,y,'sul')
                    tentou_andar=tentou_andar + 1
        #print 'SEI LA MANO TA MT LOCO\n'
        cont_repeticao = cont_repeticao + 1
        


#função usada pela arqueiro_anda
#ela descobre paredes adjacentes ao arqueiro e coloca no db
def descobre_parede_adjacente(x,y):
    if(x==1):
        py_assert('database.pl',"parede(%s, %s)." %(x-1,y))
    elif(x==12):
        py_assert('database.pl',"parede(%s, %s)." %(x+1, y))
    if(y==1):
        py_assert('database.pl',"parede(%s,%s)." %(x,y-1))
    elif(y==12):
        py_assert('database.pl',"parede(%s,%s)."%(x,y+1))
    return True

'''
***************************************
AQUI EM BAIXO FICAM OS TESTES DO CÓDIGO 
***************************************
'''

#atira()
#pega_ouro()
#inimigo_dano(10, 2)
#print caiu_poco()
atualiza_ponto(10)

py_assert('database.pl',"local_arqueiro(1,1,norte).")
py_assert('database.pl', "visitadas(1,1).")
for i in range(40):
    prolog.consult('database.pl')
    print arqueiro_anda_while()
    print i
    print
