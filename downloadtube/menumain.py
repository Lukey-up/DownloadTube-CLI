import downloader
import search
from colorama import Fore
import timer
import DTUX
import localmovie

class menu:
    def MenuMain():
        print(Fore.CYAN + "[1] pesquisar \n[2] baixar video \n[3] seus videos \n[4] sair")
        try:
            op = int(input(Fore.WHITE + "insira uma opção:"))
        except Exception as err:
            print(Fore.RED + '[-] ERRO: selecione uma opção valia.')
            menu.MenuMain()
        if op == 1:
            DTUX.clear()
            search.sarch.pesquisa()
        elif op == 2:
             DTUX.clear()
             downloader.download.download()
        elif op == 3:
             DTUX.clear()
             localmovie.dire()
        elif op == 4:
            print('finalizando tarefas')
            timer.coutdown.go(1)
            DTUX.clear()
            print('tarefas finalizadas, o preograma fechara em 3s')
            timer.coutdown.go(3)
            DTUX.clear()
            quit()
        else:
            print(Fore.RED + '[-] ERRO: selecione uma opção valia.')
            timer.coutdown.go(2)
            DTUX.clear()
            menu.MenuMain()
