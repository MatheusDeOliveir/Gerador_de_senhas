from geradores import *
import time
import os


while True:
    caracteres = list()
    print ("Deseja gerar uma senha?\n[1] - Sim\n[2] - Sair\n")
    entrada = input ('')
    
    if entrada.startswith('1'):
        caracteres.append(caractere_especial())
        caracteres.append(caractere_especial())
        caracteres.append(digito())        
        caracteres.append(digito())
        caracteres.append(letra_maiuscula())        
        caracteres.append(letra_maiuscula()) 
        caracteres.append(letra_minuscula())       
        caracteres.append(letra_minuscula())       
        sn = gerar_senha(caracteres)
        print (sn)       
        
        
        
    elif entrada.startswith('2'):
        print ('saindo...\n')
        time.sleep(2)
        os.system('cls')
        break
    else:
        print ("Opção inválida. \n")
        time.sleep(0.5)
        os.system("cls")
        continue