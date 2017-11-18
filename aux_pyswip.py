#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 15:57:35 2017

@author: LuisClaudio
"""

def py_assert(pl_file, command):
    with open(pl_file, "a") as myfile:
        myfile.write('\n')
        myfile.write(command)
        #myfile.truncate()
        myfile.close()
        return 
    
def py_retract(pl_file, command):
    with open(pl_file,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if command not in line:
                f.write(line)
        f.truncate()
        f.close()
    return
    
def print_file(pl_file):
    f = open(pl_file,"r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        print i
    f.close()


def preenche_database(mapa_wumpus):
    i = 0
    j = 0
    with open('test.pl', "w") as myfile:
        myfile.write('Teste\n')
        for linha in mapa_wumpus:
            for fato in linha:
                if fato >= -5000 and fato <= -4950:
                    myfile.write('parede(%s,%s).\n' %(i, j))
                    
                elif fato >= 45 and fato <= 155:
                    myfile.write('inimigo(%s,%s,20,100).\n' %(i, j))
                elif fato >= 445 and fato <= 555:
                    myfile.write('inimigo(%s,%s,50,100).\n' %(i, j))
                elif fato >= -300 and fato <= -245:
                    myfile.write('buraco(%s,%s).\n' %(i, j))
                elif fato >= 8000:
                    myfile.write('ouro(%s,%s).\n' %(i, j))
                j = j + 1
            j = 0
            i = i + 1
        myfile.truncate()
        myfile.close()
    return 

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
py_retract('test.pl', "parede(13,13).")
py_assert('test.pl', "test_assert(13,13).")
py_assert('test.pl', "test_assert(13,13).")
print_file('test.pl')

