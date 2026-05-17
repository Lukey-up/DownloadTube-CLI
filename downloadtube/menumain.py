import downloader
import search
from colorama import Fore

class menu:
    def MenuMain():
        print()
        print(Fore.CYAN + "[1] pesquisar \n[2] baixar video \n[3] sair")
        op = int(input(Fore.WHITE + "insira uma opção:"))
        if op == 1:
            search.sarch.pesquisa()
        elif op == 2:
            downloader.download.download()
        elif op == 3:
            quit
