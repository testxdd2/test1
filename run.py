import os
import subprocess
import time


logo = """\033[33m
  _____ _____  _      ____   _____  _____ ______ _____  
 |_   _|  __ \| |    / __ \ / ____|/ ____|  ____|  __ \ 
   | | | |__) | |   | |  | | |  __| |  __| |__  | |__) |
   | | |  ___/| |   | |  | | | |_ | | |_ |  __| |  _  / 
  _| |_| |    | |___| |__| | |__| | |__| | |____| | \ \ 
 |_____|_|    |______\____/ \_____|\_____|______|_|  \_\
 
            By: Euronymou5
"""

def check():
    while True:
        with open('ip.txt') as ip:
            lines = ip.read().rstrip()
            if len(lines) != 0:
                print('\n\033[94m[!] IP de la victima encontrado')
                print(f'\n[~] IP: {cat ip.txt}')
        ip.close()                

def server():
    os.system("clear")
    print('[~] Iniciando servidor php...')
    var = input('[~] ¿Quieres editar el puerto? (Default: 8080) [Y/n]: ')
    if var == "Y" or var == "y":
        port = int(input('\n[~] Ingresa el puerto: ')
        os.system(f"php -S localhost:{port} > /dev/null 2>&1 &")
        check()
    elif var == "n" or var == "N":
        print('\n[~] Utilizando el puerto por default: 8080')
        os.system("php -S localhost:8080 > /dev/null 2>&1 &")
        check()
    else:
        print('\n[!] Error Debes de ingresar una opcion Y/n')
        time.sleep(2)
        server()

def menu():
    os.system("killall php")
    os.system("clear")
    print(logo)
    print('\n[1] Iniciar servidor php')
    print('[99] Salir')
    T = int(input('\n>> ')
    if  T == 1:
        server()
    elif T == 99:
        exit()
    else:
        print('\n[!] Error opcion invalida.')
        time.sleep(2)
        menu()