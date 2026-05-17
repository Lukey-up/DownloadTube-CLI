from menumain import menu
from login import login
from registrar import registrar
from colorama import Fore, init


class start:
    def start():
        print(Fore.WHITE + "bem vindo ou downloadertube!! \ncrie uma conta para começar ou faça lognin")
        print(Fore.CYAN + "[1] login \n[2] registra-se \n[3] continuar anonimo.")
        opcao = int(input(Fore.WHITE + "selecione uma opção:"))
    
        if opcao == str:
            print( Fore.RED + '[!] ERRO: digite um número.')
        elif opcao == 1:
            login.login()
        elif opcao == 2:
            registrar.registrar()
        elif opcao == 3:
            menu.MenuMain()
        else:
            print(Fore.RED + '[!] ERRO:sem seleção.')
