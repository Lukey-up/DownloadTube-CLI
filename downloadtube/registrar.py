from colorama import Fore
import menumain
import DTUX
import timer

class registrar:
    def registrar(a=None):
        print(200)
        print(Fore.LIGHTRED_EX + '[!] essa opição não esta disponivel.')
        timer.coutdown.go(5)
        DTUX.clear()
        menumain.menu.MenuMain()