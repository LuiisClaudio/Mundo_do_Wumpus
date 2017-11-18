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
def py_retract_(pl_file, command):
    f = open(pl_file,"r+")
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != command:
            #print i
            #print command
            f.write(i)
    f.truncate()
    f.close()
    
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
#py_assert('database.pl', "fato(1,1).")
#py_retract('database.pl', "parede")
#print_file('database.pl')
