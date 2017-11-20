#!/usr/bin/env python2
# -*- coding: utf-8 -*-

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


def preenche_check(mapa_wumpus):
    i = 0
    j = 0
    with open('check.pl', "w") as myfile:
        for linha in mapa_wumpus:
            for fato in linha:
                if fato >= -5000 and fato <= -4950:
                    myfile.write('parede(%s,%s).\n' %(i, j))
                    
                elif fato >= 45 and fato <= 155:
                    myfile.write('inimigo(%s,%s,20,100).\n' %(i, j))
                elif fato >= 445 and fato <= 555:
                    myfile.write('inimigo(%s,%s,50,100).\n' %(i, j))
                elif fato >= -300 and fato <= -245:
                    myfile.write('poco(%s,%s).\n' %(i, j))
                elif fato >= 8000:
                    myfile.write('ouro(%s,%s).\n' %(i, j))
                j = j + 1
            j = 0
            i = i + 1
        myfile.truncate()
        myfile.close()
    i = 0
    j = 0
    with open('check_interface.pl', "w") as f:
        for linha in mapa_wumpus:
            for fato in linha:
                if fato >= -5000 and fato <= -4950:
                    f.write('parede(%s,%s).\n' %(i, j))
                    
                elif fato >= 45 and fato <= 155:
                    f.write('inimigo(%s,%s,20,100).\n' %(i, j))
                elif fato >= 445 and fato <= 555:
                    f.write('inimigo(%s,%s,50,100).\n' %(i, j))
                elif fato >= -300 and fato <= -245:
                    f.write('poco(%s,%s).\n' %(i, j))
                elif fato >= 8000:
                    f.write('ouro(%s,%s).\n' %(i, j))
                j = j + 1
            j = 0
            i = i + 1
        f.truncate()
        f.close()
    return 

#py_retract('test.pl', "parede(13,13).")
#py_assert('test.pl', "test_assert(13,13).")
#py_assert('test.pl', "test_assert(13,13).")
#print_file('test.pl')

