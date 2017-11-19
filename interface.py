from IA_T2 import cria_caverna, preenche_tabuleiro

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

def print_tabuleiro():
    tab = preenche_tabuleiro()
    for linha in tab:
        print print_list_line2(linha)
print_tabuleiro()

