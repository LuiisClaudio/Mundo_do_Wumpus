# -*- coding: utf-8 -*-
from pyswip import Prolog
prolog = Prolog()
def define_simbolo(fato):
	if fato >= -5000 and fato <= -4950: #parede
		return '@'
	elif fato >= 45 and fato <= 155: #inimigo1
		return 'v'
	elif fato >= 445 and fato <= 555: #inimigo1
		return 'w'
	elif fato >= -300 and fato <= -245: #buraco
		return '#'
	elif fato >= 8000: #ouro
		return '$'
	elif fato >= -50 and fato <= -24: #entrada
		return 'E'
	return '?'

def print_list_line(lst):
    print_line = ''
    for i in lst:
        print_line += ' ' + define_simbolo(i)
    return print_line

def print_list_line2(lst):
    print_line = ''
    for i in lst:
        print_line += ' ' + str(i)
    return print_line

def preenche_tabuleiro():
    prolog.consult('database.pl')
    prolog.consult('check_interface.pl')
    prolog.consult('Mundo_do_Wumpus.pl')
    tab_tam = 14
    tab = []*tab_tam
    
    arqueiro = list(prolog.query("local_arqueiro(X, Y, D)"))
    poco = list(prolog.query("poco(X, Y)"))
    inimigo = list(prolog.query("inimigo(Z, W, X, Y)"))
    ouro = list(prolog.query("ouro(X, Y)"))
    parede = list(prolog.query("parede(X, Y)"))
    visitadas = list(prolog.query("visitadas(X, Y)"))
    #brisa = list(prolog.query("sentiu_brisa_poco(X, Y)"))
    #fedor = list(prolog.query("sentiu_fedor(X, Y)"))
    
    #print 'arqueiro', arqueiro
    #print 'poco', poco
    #print 'inimigo', inimigo
    #print 'ouro', ouro
    #print 'parede', parede
    #print 'visitadas', visitadas
    
    
    for i in range(tab_tam):
    	tab.append(['?']*tab_tam)
    for i in parede:
        tab[i.get('X')][i.get('Y')] = 'X'
    for i in visitadas:
        tab[i.get('X')][i.get('Y')] = '*' 
    for i in visitadas:
        x = int(i.get('X'))
        y = int(i.get('Y'))
        for j in poco:
            if i.get('X') == j.get('X') and  i.get('Y') == j.get('Y'):
                tab[x][y] = 'P'
                #print tab[x][y]
        for j in inimigo:
            if i.get('X') == j.get('X') and  i.get('Y') == j.get('Y'):
                tab[x][y] = 'I'
                #print tab[x][y]
        for j in ouro:
            if i.get('X') == j.get('X') and  i.get('Y') == j.get('Y'):
                tab[x][y] = 'O'
                #print tab[x][y]
        '''for j in brisa:
            if i.get('X') == j.get('X') and  i.get('Y') == j.get('Y'):
                tab[x][y] = 'B'
                #print tab[x][y]
        for j in fedor:
            if i.get('X') == j.get('X') and  i.get('Y') == j.get('Y'):
                tab[x][y] = 'F'
                #print tab[x][y]'''
                
    tab[arqueiro[0].get('X')][arqueiro[0].get('Y')] = 'A'

    return tab


def print_tabuleiro(tab):
    for linha in tab:
        print print_list_line2(linha)


